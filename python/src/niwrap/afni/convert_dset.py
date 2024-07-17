# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

CONVERT_DSET_METADATA = Metadata(
    id="adb86474eb07d762a2e017655ea129d8417f8ff2",
    name="ConvertDset",
)


class ConvertDsetOutputs(typing.NamedTuple):
    """
    Output object returned when calling `convert_dset(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    converted_dataset: OutputPathType | None
    """Converted dataset output"""


def convert_dset(
    output_type: list[typing.Literal["niml_asc", "niml_bi", "1D", "1Dp", "1Dpt", "gii", "gii_asc", "gii_b64", "gii_b64gz", "1D_stderr", "1D_stdout", "niml_stderr", "niml_stdout", "1Dp_stdout", "1Dp_stderr", "1Dpt_stdout", "1Dpt_stderr"]],
    input_dataset: InputPathType,
    input_type: typing.Literal["niml", "1D", "dx"] | None = None,
    output_prefix: str | None = None,
    dset_labels: str | None = None,
    add_node_index: bool = False,
    node_index_file: InputPathType | None = None,
    node_select_file: InputPathType | None = None,
    prepend_node_index: bool = False,
    pad_to_node: str | None = None,
    labelize: InputPathType | None = None,
    graphize: bool = False,
    graph_nodelist: str | None = None,
    graph_full_nodelist: InputPathType | None = None,
    graph_named_nodelist: str | None = None,
    graph_xyz_lpi: bool = False,
    graph_edgelist: InputPathType | None = None,
    onegraph: bool = False,
    multigraph: bool = False,
    split: int | None = None,
    no_history: bool = False,
    runner: Runner | None = None,
) -> ConvertDsetOutputs:
    """
    ConvertDset by Ziad S. Saad SSCC/NIMH/NIH.
    
    Converts a surface dataset from one format to another.
    
    Args:
        output_type: Type of output datasets.
        input_dataset: Input dataset to be converted.
        input_type: Type of input datasets.
        output_prefix: Output prefix for dataset.
        dset_labels: Label the columns (sub-bricks) of the output dataset.
        add_node_index: Add a node index element if one does not exist in the\
            input dataset.
        node_index_file: File containing node indices.
        node_select_file: File specifying the nodes to keep in the output.
        prepend_node_index: Add a node index column to the data.
        pad_to_node: Output a full dataset from node 0 to MAX_INDEX.
        labelize: Turn the dataset into a labeled set per the colormap in CMAP.
        graphize: Turn the dataset into a SUMA graph dataset.
        graph_nodelist: Two files specifying the indices and the coordinates of\
            the graph's nodes.
        graph_full_nodelist: Similar to -graph_nodelist_1D but without need for\
            NODEINDLIST.1D.
        graph_named_nodelist: Two files specifying graph node indices, string\
            labels, and their coordinates.
        graph_xyz_lpi: Coordinates in NodeList.1D are in LPI instead of RAI.
        graph_edgelist: Indices of graph nodes defining edge.
        onegraph: Expect input dataset to be one square matrix defining the\
            graph (default).
        multigraph: Expect each column in input dataset to define an entire\
            graph.
        split: Split a multi-column dataset into about N output datasets.
        no_history: Do not include a history element in the output.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `ConvertDsetOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(CONVERT_DSET_METADATA)
    cargs = []
    cargs.append("ConvertDset")
    cargs.extend(["-o_", *output_type])
    cargs.append("-input")
    cargs.extend(["-input", execution.input_file(input_dataset)])
    if input_type is not None:
        cargs.extend(["-i_", input_type])
    if output_prefix is not None:
        cargs.extend(["-prefix", output_prefix])
    cargs.append("[MANDATORY_PARAMS]")
    cargs.append("[OPTIONAL_PARAMS]")
    ret = ConvertDsetOutputs(
        root=execution.output_file("."),
        converted_dataset=execution.output_file(f"{output_prefix}", optional=True) if output_prefix is not None else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "CONVERT_DSET_METADATA",
    "ConvertDsetOutputs",
    "convert_dset",
]
