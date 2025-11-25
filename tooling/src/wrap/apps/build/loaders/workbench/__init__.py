import hashlib
import json

import styx.ir.core as ir

from wrap.apps.build.loaders.workbench import model as wb

# utilities


def _option_name_normalize(s: str) -> str:
    return s.removeprefix("-")


def _hash_from_json(o: dict) -> str:
    """Generate a hash from a json serializable object."""
    json_str = json.dumps(o, sort_keys=True)
    return hashlib.sha1(json_str.encode()).hexdigest()


# conversion


def _wb_media_types(wb_type: str) -> list[str]:
    # TODO: Should resolve these to universal media types supported by wb
    assert wb_type in wb.TYPE_ANY_FILE
    return [f"workbench/{wb_type}"]


def _make_type(obj: wb.Parameter):
    param_type = obj.type

    if param_type == wb.TYPE_STRING:
        return ir.Param.String()
    if param_type in wb.TYPE_ANY_FILE:
        return ir.Param.File(
            media_types=_wb_media_types(param_type),
        )
    if param_type == wb.TYPE_FLOATING_POINT:
        return ir.Param.Float()
    if param_type == wb.TYPE_INTEGER:
        return ir.Param.Int()
    if param_type == wb.TYPE_BOOLEAN:
        # TODO: is this correct? what uses this?
        return ir.Param.Bool(
            value_true=["true"],
            value_false=["false"],
        )
    raise ValueError(f"Unknown type: {param_type}")


class _Loader:
    def __init__(self):
        self._id_counter = 0

    def _next_id(self) -> int:
        _id = self._id_counter
        self._id_counter += 1
        return _id

    def _make_param(self, obj: wb.Parameter):
        return ir.Param(
            base=ir.Param.Base(
                id_=self._next_id(),
                name=obj.short_name,
                docs=ir.Documentation(
                    description=obj.description,
                ),
            ),
            body=_make_type(obj),
            nullable=False,
        )

    def _make_output(self, obj: wb.Output):
        param = ir.Param(
            base=ir.Param.Base(
                id_=self._next_id(),
                name=obj.short_name,
                docs=ir.Documentation(
                    description=obj.description,
                ),
            ),
            body=ir.Param.String(),  # !
            nullable=False,
        )

        output = ir.Output(
            id_=self._next_id(),
            name=param.base.name,
            tokens=[
                ir.OutputParamReference(
                    ref_id=param.base.id_,
                )
            ],
            docs=param.base.docs,
            media_types=_wb_media_types(obj.type),
        )

        return param, output

    def _make_option(self, obj: wb.Option, repeatable: bool = False):
        docs = ir.Documentation(
            description=obj.description,
        )

        groups: list[ir.ConditionalGroup] = []
        args: list[ir.CmdArg] = [ir.CmdArg([obj.option_switch])]
        groups.append(ir.ConditionalGroup(args))
        outputs: list[ir.Output] = []

        for obj_param in obj.params:
            param = self._make_param(obj_param)

            args.append(ir.CmdArg([param]))

        for obj_output in obj.outputs:
            param, output = self._make_output(obj_output)

            args.append(ir.CmdArg([param]))
            outputs.append(output)

        for obj_option in obj.options:
            param = self._make_option(obj_option, repeatable=False)

            args.append(ir.CmdArg([param]))

        for obj_option in obj.repeatable_options:
            param = self._make_option(obj_option, repeatable=True)

            args.append(ir.CmdArg([param]))

        return ir.Param(
            base=ir.Param.Base(
                id_=self._next_id(),
                name=_option_name_normalize(obj.option_switch),
                outputs=outputs,
                docs=docs,
            ),
            body=ir.Param.Struct(
                name=_option_name_normalize(obj.option_switch),
                groups=groups,
                docs=docs,
            ),
            nullable=True,
            default_value=ir.Param.SetToNone,
            list_=ir.Param.List() if repeatable else None,
        )

    def load(self, obj: wb.WorkbenchCommand, hash: str) -> ir.App:
        docs = ir.Documentation(
            description=f"{obj.short_description}.\n\n{obj.help_text}"
        )

        groups: list[ir.ConditionalGroup] = []
        args: list[ir.CmdArg] = [
            ir.CmdArg(tokens=["wb_command"]),
            ir.CmdArg(tokens=[obj.command]),
        ]
        groups.append(ir.ConditionalGroup(args))
        args = []  # Start new group for actual command
        groups.append(ir.ConditionalGroup(args))
        outputs: list[ir.Output] = []

        for obj_param in obj.params:
            param = self._make_param(obj_param)

            groups.append(ir.ConditionalGroup([ir.CmdArg([param])]))

        for obj_output in obj.outputs:
            param, output = self._make_output(obj_output)

            args.append(ir.CmdArg([param]))
            outputs.append(output)

        for obj_option in obj.options:
            param = self._make_option(obj_option, repeatable=False)

            args.append(ir.CmdArg([param]))

        for obj_option in obj.repeatable_options:
            param = self._make_option(obj_option, repeatable=True)

            args.append(ir.CmdArg([param]))

        return ir.App(
            uid=f"{hash}.workbench",
            command=ir.Param(
                base=ir.Param.Base(
                    id_=self._next_id(),
                    name=_option_name_normalize(obj.command),
                    outputs=outputs,
                    docs=docs,
                ),
                body=ir.Param.Struct(
                    name=_option_name_normalize(obj.command),
                    groups=groups,
                    docs=docs,
                ),
            ),
        )


# entrypoint


def load_workbench(obj: dict) -> ir.App:
    hash = _hash_from_json(obj)
    return _Loader().load(wb.WorkbenchCommand.model_validate(obj), hash)
