# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

TO3D_METADATA = Metadata(
    id="e0b1a8079bd8c845d68df128a96c8155a51e0e19.boutiques",
    name="to3d",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class To3dOutputs(typing.NamedTuple):
    """
    Output object returned when calling `to3d(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    headfile: OutputPathType | None
    """Output AFNI HEAD file"""
    brikfile: OutputPathType | None
    """Output AFNI BRIK file"""
    outfile_outliers: OutputPathType | None
    """Outlier count file"""


def to3d(
    input_files: list[InputPathType],
    type_: typing.Literal["spgr", "fse", "epan", "anat", "ct", "spct", "pet", "mra", "bmap", "diff", "omri", "abuc", "fim", "fith", "fico", "fitt", "fift", "fizt", "fict", "fibt", "fibn", "figt", "fipt", "fbuc"] | None = None,
    statpar: list[float] | None = None,
    prefix: str | None = None,
    session: str | None = None,
    geomparent: InputPathType | None = None,
    anatparent: InputPathType | None = None,
    nosave_flag: bool = False,
    nowritebrik_flag: bool = False,
    view: typing.Literal["orig", "acpc", "tlrc"] | None = None,
    time_zt: list[str] | None = None,
    time_tz: list[str] | None = None,
    tr_units: typing.Literal["ms", "msec", "s", "sec", "Hz", "Hertz"] | None = None,
    torg: float | None = None,
    x_fov: str | None = None,
    y_fov: str | None = None,
    z_fov: str | None = None,
    x_slab: str | None = None,
    y_slab: str | None = None,
    z_slab: str | None = None,
    zorigin: float | None = None,
    data_type: typing.Literal["short", "float", "byte", "complex"] | None = None,
    global_scaling_factor: float | None = None,
    nofloatscan_flag: bool = False,
    in1_flag: bool = False,
    orient: str | None = None,
    skip_outliers_flag: bool = False,
    text_outliers_flag: bool = False,
    save_outliers: str | None = None,
    assume_dicom_mosaic_flag: bool = False,
    oblique_origin_flag: bool = False,
    reverse_list_flag: bool = False,
    use_last_elem_flag: bool = False,
    use_old_mosaic_code_flag: bool = False,
    ushort2float_flag: bool = False,
    verbose_flag: bool = False,
    gamma: float | None = None,
    ncolors: float | None = None,
    xtwarns_flag: bool = False,
    quit_on_err_flag: bool = False,
    runner: Runner | None = None,
) -> To3dOutputs:
    """
    Creates 3D datasets for use with AFNI from 2D image files.
    
    Author: AFNI Team
    
    URL: https://afni.nimh.nih.gov/pub/dist/doc/program_help/to3d.html
    
    Args:
        input_files: Input 2D image files.
        type_: Declare images to contain data of a given type.
        statpar: Supply auxiliary statistical parameters.
        prefix: Prefix of the output 3D dataset.
        session: Session directory for output 3D dataset.
        geomparent: Read geometry data from dataset file.
        anatparent: Take anatomy parent from dataset file.
        nosave_flag: Suppress autosave of 3D dataset.
        nowritebrik_flag: Suppress saving of the BRIK file.
        view: Set the dataset's viewing coordinates.
        time_zt: Specify time dependent dataset (z-axis first, then t-axis).
        time_tz: Specify time dependent dataset (t-axis first, then z-axis).
        tr_units: Specify TR units.
        torg: Set time origin of dataset.
        x_fov: Specify size and orientation of the x-axis extent.
        y_fov: Specify size and orientation of the y-axis extent.
        z_fov: Specify size and orientation of the z-axis extent.
        x_slab: Specify x-axis slab.
        y_slab: Specify y-axis slab.
        z_slab: Specify z-axis slab.
        zorigin: Set the center of the first slice offset in z-axis.
        data_type: Set voxel data to be stored as given data type.
        global_scaling_factor: Global scaling factor.
        nofloatscan_flag: Do not scan for illegal floating point values.
        in1_flag: Read and process images one slice at a time.
        orient: Set the orientation of the 3D volumes.
        skip_outliers_flag: Skip the outlier check for 3D+time datasets.
        text_outliers_flag: Only print out the outlier check results in text\
            form.
        save_outliers: Save the outliers count into a 1D file.
        assume_dicom_mosaic_flag: Assume any Siemens DICOM file is a potential\
            MOSAIC image.
        oblique_origin_flag: Assume origin and orientation from oblique\
            transformation matrix.
        reverse_list_flag: Reverse the input file list.
        use_last_elem_flag: Search DICOM images for the last occurrence of each\
            element.
        use_old_mosaic_code_flag: Do not use the Dec 2010 updates to Siemens\
            mosaic code.
        ushort2float_flag: Convert input shorts to float and add 2^16 to any\
            negatives.
        verbose_flag: Show debugging information for reading DICOM files.
        gamma: Gamma correction factor for the monitor.
        ncolors: Number of gray levels for the image displays.
        xtwarns_flag: Turn on display of Xt warning messages.
        quit_on_err_flag: Do not launch interactive to3d mode if input has\
            error.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `To3dOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(TO3D_METADATA)
    cargs = []
    cargs.append("to3d")
    cargs.extend([execution.input_file(f) for f in input_files])
    if type_ is not None:
        cargs.extend([
            "-type",
            type_
        ])
    if statpar is not None:
        cargs.extend([
            "-statpar",
            *map(str, statpar)
        ])
    if prefix is not None:
        cargs.extend([
            "-prefix",
            prefix
        ])
    if session is not None:
        cargs.extend([
            "-session",
            session
        ])
    if geomparent is not None:
        cargs.extend([
            "-geomparent",
            execution.input_file(geomparent)
        ])
    if anatparent is not None:
        cargs.extend([
            "-anatparent",
            execution.input_file(anatparent)
        ])
    if nosave_flag:
        cargs.append("-nosave")
    if nowritebrik_flag:
        cargs.append("-nowritebrik")
    if view is not None:
        cargs.extend([
            "-view",
            view
        ])
    if time_zt is not None:
        cargs.extend([
            "-time:zt",
            *time_zt
        ])
    if time_tz is not None:
        cargs.extend([
            "-time:tz",
            *time_tz
        ])
    if tr_units is not None:
        cargs.extend([
            "-t",
            tr_units
        ])
    if torg is not None:
        cargs.extend([
            "-Torg",
            str(torg)
        ])
    if x_fov is not None:
        cargs.extend([
            "-xFOV",
            x_fov
        ])
    if y_fov is not None:
        cargs.extend([
            "-yFOV",
            y_fov
        ])
    if z_fov is not None:
        cargs.extend([
            "-zFOV",
            z_fov
        ])
    if x_slab is not None:
        cargs.extend([
            "-xSLAB",
            x_slab
        ])
    if y_slab is not None:
        cargs.extend([
            "-ySLAB",
            y_slab
        ])
    if z_slab is not None:
        cargs.extend([
            "-zSLAB",
            z_slab
        ])
    if zorigin is not None:
        cargs.extend([
            "-zorigin",
            str(zorigin)
        ])
    if data_type is not None:
        cargs.extend([
            "-datum",
            data_type
        ])
    if global_scaling_factor is not None:
        cargs.extend([
            "-gsfac",
            str(global_scaling_factor)
        ])
    if nofloatscan_flag:
        cargs.append("-nofloatscan")
    if in1_flag:
        cargs.append("-in:1")
    if orient is not None:
        cargs.extend([
            "-orient",
            orient
        ])
    if skip_outliers_flag:
        cargs.append("-skip_outliers")
    if text_outliers_flag:
        cargs.append("-text_outliers")
    if save_outliers is not None:
        cargs.extend([
            "-save_outliers",
            save_outliers
        ])
    if assume_dicom_mosaic_flag:
        cargs.append("-assume_dicom_mosaic")
    if oblique_origin_flag:
        cargs.append("-oblique_origin")
    if reverse_list_flag:
        cargs.append("-reverse_list")
    if use_last_elem_flag:
        cargs.append("-use_last_elem")
    if use_old_mosaic_code_flag:
        cargs.append("-use_old_mosaic_code")
    if ushort2float_flag:
        cargs.append("-ushort2float")
    if verbose_flag:
        cargs.append("-verb")
    if gamma is not None:
        cargs.extend([
            "-gamma",
            str(gamma)
        ])
    if ncolors is not None:
        cargs.extend([
            "-ncolors",
            str(ncolors)
        ])
    if xtwarns_flag:
        cargs.append("-xtwarns")
    if quit_on_err_flag:
        cargs.append("-quit_on_err")
    ret = To3dOutputs(
        root=execution.output_file("."),
        headfile=execution.output_file(prefix + ".HEAD") if (prefix is not None) else None,
        brikfile=execution.output_file(prefix + ".BRIK") if (prefix is not None) else None,
        outfile_outliers=execution.output_file(save_outliers) if (save_outliers is not None) else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "TO3D_METADATA",
    "To3dOutputs",
    "to3d",
]
