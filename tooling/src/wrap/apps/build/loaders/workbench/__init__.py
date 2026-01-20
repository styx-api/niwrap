"""Loader for Connectome Workbench command definitions."""

import hashlib
import json

import styx.ir.core as ir

from wrap.apps.build.loaders.workbench import model as wb


def _normalize_option_name(name: str) -> str:
    """Remove leading dash from option name."""
    return name.removeprefix("-")


def _hash_json(obj: dict) -> str:
    """Generate a SHA1 hash from a JSON-serializable object."""
    json_str = json.dumps(obj, sort_keys=True)
    return hashlib.sha1(json_str.encode()).hexdigest()


def _wb_media_types(wb_type: str) -> list[str]:
    """Convert Workbench type to media type list."""
    if wb_type not in wb.TYPE_ANY_FILE:
        raise ValueError(f"Expected file type, got: {wb_type}")
    return [f"workbench/{wb_type}"]


def _make_param_type(wb_type: str):
    """Convert Workbench parameter type to IR type."""
    match wb_type:
        case wb.TYPE_STRING:
            return ir.Param.String()
        case wb.TYPE_FLOATING_POINT:
            return ir.Param.Float()
        case wb.TYPE_INTEGER:
            return ir.Param.Int()
        case wb.TYPE_BOOLEAN:
            return ir.Param.Bool(value_true=["true"], value_false=["false"])
        case _ if wb_type in wb.TYPE_ANY_FILE:
            return ir.Param.File(media_types=_wb_media_types(wb_type))
        case _:
            raise ValueError(f"Unknown Workbench type: {wb_type}")


class _Loader:
    """Stateful loader that tracks parameter IDs."""

    def __init__(self) -> None:
        self._id_counter = 0

    def _next_id(self) -> int:
        id_ = self._id_counter
        self._id_counter += 1
        return id_

    def _load_param(self, obj: wb.Parameter) -> ir.Param:
        """Convert a Workbench parameter to IR."""
        return ir.Param(
            base=ir.Param.Base(
                id_=self._next_id(),
                name=obj.short_name,
                docs=ir.Documentation(description=obj.description),
            ),
            body=_make_param_type(obj.type),
            nullable=False,
        )

    def _load_output(self, obj: wb.Output) -> tuple[ir.Param, ir.Output]:
        """Convert a Workbench output to IR param and output."""
        param = ir.Param(
            base=ir.Param.Base(
                id_=self._next_id(),
                name=obj.short_name,
                docs=ir.Documentation(description=obj.description),
            ),
            body=ir.Param.String(),
            nullable=False,
        )

        output = ir.Output(
            id_=self._next_id(),
            name=param.base.name,
            tokens=[ir.OutputParamReference(ref_id=param.base.id_)],
            docs=param.base.docs,
            media_types=_wb_media_types(obj.type),
        )

        return param, output

    def _load_option(self, obj: wb.Option, repeatable: bool = False) -> ir.Param:
        """Convert a Workbench option to IR."""
        docs = ir.Documentation(description=obj.description)
        name = _normalize_option_name(obj.option_switch)

        args: list[ir.CmdArg] = [ir.CmdArg([obj.option_switch])]
        outputs: list[ir.Output] = []

        for obj_param in obj.params:
            args.append(ir.CmdArg([self._load_param(obj_param)]))

        for obj_output in obj.outputs:
            param, output = self._load_output(obj_output)
            args.append(ir.CmdArg([param]))
            outputs.append(output)

        for obj_option in obj.options:
            args.append(ir.CmdArg([self._load_option(obj_option, repeatable=False)]))

        for obj_option in obj.repeatable_options:
            args.append(ir.CmdArg([self._load_option(obj_option, repeatable=True)]))

        return ir.Param(
            base=ir.Param.Base(
                id_=self._next_id(),
                name=name,
                outputs=outputs,
                docs=docs,
            ),
            body=ir.Param.Struct(
                name=name,
                groups=[ir.ConditionalGroup(args)],
                docs=docs,
            ),
            nullable=True,
            default_value=ir.Param.SetToNone,
            list_=ir.Param.List() if repeatable else None,
        )

    def load(self, obj: wb.WorkbenchCommand, hash_: str) -> ir.App:
        """Convert a Workbench command to IR."""
        docs = ir.Documentation(
            description=f"{obj.short_description}.\n\n{obj.help_text}"
        )
        name = _normalize_option_name(obj.command)

        groups: list[ir.ConditionalGroup] = []
        outputs: list[ir.Output] = []

        # Command prefix: wb_command <command>
        groups.append(
            ir.ConditionalGroup(
                [
                    ir.CmdArg(tokens=["wb_command"]),
                    ir.CmdArg(tokens=[obj.command]),
                ]
            )
        )

        # Positional parameters (each in its own group to preserve order)
        for obj_param in obj.params:
            groups.append(
                ir.ConditionalGroup([ir.CmdArg([self._load_param(obj_param)])])
            )

        # Output parameters (also positional, preserve order)
        for obj_output in obj.outputs:
            param, output = self._load_output(obj_output)
            groups.append(ir.ConditionalGroup([ir.CmdArg([param])]))
            outputs.append(output)

        # Options (order doesn't matter, can share a group)
        option_args: list[ir.CmdArg] = []

        for obj_option in obj.options:
            option_args.append(
                ir.CmdArg([self._load_option(obj_option, repeatable=False)])
            )

        for obj_option in obj.repeatable_options:
            option_args.append(
                ir.CmdArg([self._load_option(obj_option, repeatable=True)])
            )

        if option_args:
            groups.append(ir.ConditionalGroup(option_args))

        return ir.App(
            uid=f"{hash_}.workbench",
            command=ir.Param(
                base=ir.Param.Base(
                    id_=self._next_id(),
                    name=name,
                    outputs=outputs,
                    docs=docs,
                ),
                body=ir.Param.Struct(
                    name=name,
                    groups=groups,
                    docs=docs,
                ),
            ),
        )


def load_workbench(obj: dict) -> ir.App:
    """Load a Workbench command definition from a dictionary."""
    hash_ = _hash_json(obj)
    command = wb.WorkbenchCommand.model_validate(obj)
    return _Loader().load(command, hash_)
