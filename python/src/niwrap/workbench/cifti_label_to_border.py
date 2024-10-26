# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

CIFTI_LABEL_TO_BORDER_METADATA = Metadata(
    id="cfa090287e94127e183f28bd42aeab765397cb2c.boutiques",
    name="cifti-label-to-border",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)


class CiftiLabelToBorderBorderOutputs(typing.NamedTuple):
    """
    Output object returned when calling `list[CiftiLabelToBorderBorder] | None(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    border_out: OutputPathType
    """the output border file"""


@dataclasses.dataclass
class CiftiLabelToBorderBorder:
    """
    specify output file for a surface structure.
    """
    surface: InputPathType
    """the surface to use for neighbor and structure information"""
    border_out: str
    """the output border file"""
    
    def run(
        self,
        execution: Execution,
    ) -> list[str]:
        """
        Build command line arguments. This method is called by the main command.
        
        Args:
            execution: The execution object.
        Returns:
            Command line arguments
        """
        cargs = []
        cargs.append("-border")
        cargs.append(execution.input_file(self.surface))
        cargs.append(self.border_out)
        return cargs
    
    def outputs(
        self,
        execution: Execution,
    ) -> CiftiLabelToBorderBorderOutputs:
        """
        Collect output file paths.
        
        Args:
            execution: The execution object.
        Returns:
            NamedTuple of outputs (described in `CiftiLabelToBorderBorderOutputs`).
        """
        ret = CiftiLabelToBorderBorderOutputs(
            root=execution.output_file("."),
            border_out=execution.output_file(self.border_out),
        )
        return ret


class CiftiLabelToBorderOutputs(typing.NamedTuple):
    """
    Output object returned when calling `cifti_label_to_border(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    border: typing.List[CiftiLabelToBorderBorderOutputs] | None
    """Outputs from `CiftiLabelToBorderBorder`.This is a list of outputs with
    the same length and order as the inputs."""


def cifti_label_to_border(
    cifti_in: InputPathType,
    opt_placement_fraction: float | None = None,
    opt_column_column: str | None = None,
    border: list[CiftiLabelToBorderBorder] | None = None,
    runner: Runner | None = None,
) -> CiftiLabelToBorderOutputs:
    """
    Draw borders around cifti labels.
    
    For each surface, takes the labels on the matching structure and draws
    borders around the labels. Use -column to only draw borders around one label
    map.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
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
        cargs.extend([
            "-placement",
            str(opt_placement_fraction)
        ])
    if opt_column_column is not None:
        cargs.extend([
            "-column",
            opt_column_column
        ])
    if border is not None:
        cargs.extend([a for c in [s.run(execution) for s in border] for a in c])
    ret = CiftiLabelToBorderOutputs(
        root=execution.output_file("."),
        border=[i.outputs(execution) if hasattr(i, "outputs") else None for i in border] if border else None,
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
