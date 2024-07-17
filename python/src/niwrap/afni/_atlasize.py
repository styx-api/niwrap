# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

_ATLASIZE_METADATA = Metadata(
    id="483bdad1090c674b90ceeba07ec9ecf6a59c7a28",
    name="@Atlasize",
    container_image_type="docker",
    container_image_index="index.docker.io",
    container_image_tag="afni/afni:latest",
)


class AtlasizeOutputs(typing.NamedTuple):
    """
    Output object returned when calling `_atlasize(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    niml_file: OutputPathType | None
    """Generated NIML file for the atlas"""


def _atlasize(
    dset: InputPathType | None = None,
    space: str | None = None,
    lab_file: list[str] | None = None,
    lab_file_delim: str | None = None,
    longnames: float | int | None = None,
    last_longname_col: float | int | None = None,
    atlas_type: str | None = None,
    atlas_description: str | None = None,
    atlas_name: str | None = None,
    auto_backup: bool = False,
    centers: bool = False,
    centertype: str | None = None,
    centermask: InputPathType | None = None,
    skip_novoxels: bool = False,
    h_web: bool = False,
    h_view: bool = False,
    all_opts: bool = False,
    h_find: str | None = None,
    runner: Runner | None = None,
) -> AtlasizeOutputs:
    """
    @Atlasize by AFNI development team.
    
    Script to turn a volumetric dataset into an AFNI atlas.
    
    Args:
        dset: Make DSET an atlas.
        space: Mark DSET as being in space SPACE.
        lab_file: Labels and keys are in text file FILE. cLAB is the index of\
            column containing labels, vVAL is the index of column containing keys\
            (1st column is indexed at 0).
        lab_file_delim: Set column delimiter for -lab_file option. Default is '\
            ' (space), but you can set your own. ';' for example.
        longnames: Additionally, allow for another column of long names for\
            regions, e.g., amygdala for AMY. cLONGNAME is the starting column for\
            the long name continuing to the last name of the output.
        last_longname_col: Limit long names to nth column.
        atlas_type: Set the atlas type where TP is 'S' for subject-based and\
            'G' for group-based atlases, respectively.
        atlas_description: A description for the atlas. Default is 'My Atlas'.
        atlas_name: Name for the atlas. Default name is based on prefix of\
            DSET.
        auto_backup: Back up the dataset if it already exists in the custom\
            atlas directory and allows an overwrite.
        centers: Add center of mass coordinates to atlas.
        centertype: Choose Icent, Dcent, or cm for different ways to compute\
            centers.
        centermask: Calculate center of mass locations for each ROI using a\
            subset of voxels. Useful for atlases with identical labels in both\
            hemispheres.
        skip_novoxels: Skip regions without any voxels in the dataset.
        h_web: Open webpage with help for this program.
        h_view: Open -help output in a GUI editor.
        all_opts: List all of the options for this script.
        h_find: Search for lines containing WORD in -help output. Search is\
            approximate.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `AtlasizeOutputs`).
    """
    runner = runner or get_global_runner()
    if lab_file is not None and not (len(lab_file) <= 3): 
        raise ValueError(f"Length of 'lab_file' must be less than 3 but was {len(lab_file)}")
    execution = runner.start_execution(_ATLASIZE_METADATA)
    cargs = []
    cargs.append("@Atlasize")
    cargs.append("[-dset")
    cargs.append("DSET]")
    cargs.append("[-space")
    cargs.append("SPACE]")
    cargs.append("[-lab_file")
    cargs.append("FILE")
    cargs.append("cLAB")
    cargs.append("cVAL]")
    cargs.append("[-lab_file_delim")
    cargs.append("COL_DELIM]")
    cargs.append("[-longnames")
    cargs.append("cLONGNAME]")
    cargs.append("[-last_longname_col")
    cargs.append("cLASTLONGNAME]")
    cargs.append("[-atlas_type")
    cargs.append("TP]")
    cargs.append("[-atlas_description")
    cargs.append("DESCRP]")
    cargs.append("[-atlas_name")
    cargs.append("NAME]")
    cargs.append("[-auto_backup]")
    cargs.append("[-centers]")
    cargs.append("[-centertype")
    cargs.append("TYPE]")
    cargs.append("[-centermask")
    cargs.append("DSET]")
    cargs.append("[-skip_novoxels]")
    cargs.append("[-h_web]")
    cargs.append("[-hweb]")
    cargs.append("[-h_view]")
    cargs.append("[-hview]")
    cargs.append("[-all_opts]")
    cargs.append("[-h_find")
    cargs.append("WORD]")
    ret = AtlasizeOutputs(
        root=execution.output_file("."),
        niml_file=execution.output_file(f"{pathlib.Path(dset).name}.niml", optional=True) if dset is not None else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "AtlasizeOutputs",
    "_ATLASIZE_METADATA",
    "_atlasize",
]
