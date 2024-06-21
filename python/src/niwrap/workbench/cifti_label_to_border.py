# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import dataclasses
import pathlib
import typing

CIFTI_LABEL_TO_BORDER_METADATA = Metadata(
    id="6a7d1472f72b510ad24775b65efa03b5cc7046ce",
    name="cifti-label-to-border",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class CiftiLabelToBorderBorderOutputs(typing.NamedTuple):
    """
    Output object returned when calling `CiftiLabelToBorderBorder.run(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    border_out: OutputPathType
    """the output border file"""


@dataclasses.dataclass
class CiftiLabelToBorderBorder:
    """
    specify output file for a surface structure
    """
    border_out: InputPathType
    """the output border file"""
    
    def run(
        self,
        execution: Execution,
    ) -> list[str]:
        """
        Build command line arguments. This method is called by the main command.
        
        Args:
            self: The sub-command object.
            execution: The execution object.
        Returns:
            
        """
        cargs = []
        cargs.append(execution.input_file(self.border_out))
        return cargs
    
    def outputs(
        self,
        execution: Execution,
    ) -> CiftiLabelToBorderBorderOutputs:
        """
        Collect output file paths.
        
        Args:
            self: The sub-command object.
            execution: The execution object.
        Returns:
            NamedTuple of outputs (described in `CiftiLabelToBorderBorderOutputs`).
        """
        ret = CiftiLabelToBorderBorderOutputs(
            root=execution.output_file("."),
            border_out=execution.output_file(f"{pathlib.Path(self.border_out).name}"),
        )
        return ret


class CiftiLabelToBorderOutputs(typing.NamedTuple):
    """
    Output object returned when calling `cifti_label_to_border(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    border: typing.List[CiftiLabelToBorderBorderOutputs]
    """Subcommand outputs"""


def cifti_label_to_border(
    cifti_in: InputPathType,
    opt_placement_fraction: float | int | None = None,
    opt_column_column: str | None = None,
    border: list[CiftiLabelToBorderBorder] = None,
    runner: Runner = None,
) -> CiftiLabelToBorderOutputs:
    """
    cifti-label-to-border by Washington University School of Medicin.
    
    Draw borders around cifti labels.
    
    For each surface, takes the labels on the matching structure and draws
    borders around the labels. Use -column to only draw borders around one label
    map.
    
    Args:
        cifti_in: the input cifti dlabel file.
        opt_placement_fraction: set how far along the edge border points are\
            drawn: fraction along edge from inside vertex (default 0.33).
        opt_column_column: select a single column: the column number or name.
        border: specify output file for a surface structure.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `CiftiLabelToBorderOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(CIFTI_LABEL_TO_BORDER_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-cifti-label-to-border")
    cargs.append(execution.input_file(cifti_in))
    if opt_placement_fraction is not None:
        cargs.extend(["-placement", str(opt_placement_fraction)])
    if opt_column_column is not None:
        cargs.extend(["-column", opt_column_column])
    if border is not None:
        cargs.extend(["-border", *[a for c in [s.run(execution) for s in border] for a in c]])
    ret = CiftiLabelToBorderOutputs(
        root=execution.output_file("."),
        border=[i.outputs(execution) for i in border] if border else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "CIFTI_LABEL_TO_BORDER_METADATA",
    "CiftiLabelToBorderBorder",
    "CiftiLabelToBorderBorderOutputs",
    "CiftiLabelToBorderOutputs",
    "cifti_label_to_border",
]
