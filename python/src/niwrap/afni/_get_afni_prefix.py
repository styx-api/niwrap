# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

_GET_AFNI_PREFIX_METADATA = Metadata(
    id="44ef5cc72fb89d74dd895b167cbf05f68fd48f15",
    name="@GetAfniPrefix",
    container_image_type="docker",
    container_image_index="hub.docker.com",
    container_image_tag="afni/afni_latest",
)


class GetAfniPrefixOutputs(typing.NamedTuple):
    """
    Output object returned when calling `_get_afni_prefix(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def _get_afni_prefix(
    name: InputPathType,
    suffix: str | None = None,
    runner: Runner | None = None,
) -> GetAfniPrefixOutputs:
    """
    @GetAfniPrefix by Ziad Saad.
    
    A tool to extract AFNI prefix from a given file path.
    
    More information:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/@GetAfniPrefix.html
    
    Args:
        name: Input file path for which the AFNI prefix will be extracted.
        suffix: Suffix string to append to the returned prefix.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `GetAfniPrefixOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(_GET_AFNI_PREFIX_METADATA)
    cargs = []
    cargs.append("@GetAfniPrefix")
    cargs.append(execution.input_file(name))
    if suffix is not None:
        cargs.append(suffix)
    ret = GetAfniPrefixOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "GetAfniPrefixOutputs",
    "_GET_AFNI_PREFIX_METADATA",
    "_get_afni_prefix",
]
