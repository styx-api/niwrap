# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

BIANCA_PERIVENT_DEEP_METADATA = Metadata(
    id="b4075edf8e76b937e80559712e3fd8686875ca35",
    name="bianca_perivent_deep",
    container_image_type="docker",
    container_image_tag="mcin/fsl:6.0.5",
)


class BiancaPeriventDeepOutputs(typing.NamedTuple):
    """
    Output object returned when calling `bianca_perivent_deep(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    perivent_map: OutputPathType
    """Binary image of periventricular WMH"""
    deepwm_map: OutputPathType
    """Binary image of deep WMH"""
    wmh_volumes: OutputPathType
    """Text file with volumes of total, periventricular, and deep WMHs (if DO_STATS is 2)"""


def bianca_perivent_deep(
    thresholded_binarised_wmh_map: InputPathType,
    ventricles_mask: InputPathType,
    minclustersize: float | int,
    do_stats: int,
    outputdir: str,
    runner: Runner | None = None,
) -> BiancaPeriventDeepOutputs:
    """
    bianca_perivent_deep by BIANCA Development Team.
    
    Separates WMH into periventricular and deep WMH, saves two separate binary
    images, and calculates volume of total and separate WMHs.
    
    Args:
        thresholded_binarised_wmh_map: Thresholded and binarized WMH map\
            (output of BIANCA thresholded and binarized).
        ventricles_mask: Ventricles mask you created using the exclusion mask\
            script. If T1 and FLAIR were not in the same space, ventricle mask\
            needs to be registered to FLAIR (and binarized).
        minclustersize: Minimum cluster (volume) size in voxels to consider.\
            Use 0 for no cluster thresholding.
        do_stats: Option to calculate volumes: 0 to only produce images without\
            volume calculation, 1 to calculate volumes for total, periventricular\
            and deep WMH and display on the screen, 2 to calculate volumes and save\
            them in a file.
        outputdir: Directory to save the output files.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `BiancaPeriventDeepOutputs`).
    """
    runner = runner or get_global_runner()
    if not (0 <= do_stats <= 2): 
        raise ValueError(f"'do_stats' must be between 0 <= x <= 2 but was {do_stats}")
    execution = runner.start_execution(BIANCA_PERIVENT_DEEP_METADATA)
    cargs = []
    cargs.append("bianca_perivent_deep")
    cargs.append(execution.input_file(thresholded_binarised_wmh_map))
    cargs.append(execution.input_file(ventricles_mask))
    cargs.append(str(minclustersize))
    cargs.append(str(do_stats))
    cargs.append(outputdir)
    ret = BiancaPeriventDeepOutputs(
        root=execution.output_file("."),
        perivent_map=execution.output_file(f"{outputdir}/perivent_map.nii.gz"),
        deepwm_map=execution.output_file(f"{outputdir}/deepwm_map.nii.gz"),
        wmh_volumes=execution.output_file(f"{outputdir}/WMH_tot_pvent_deep_10mm.txt", optional=True),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "BIANCA_PERIVENT_DEEP_METADATA",
    "BiancaPeriventDeepOutputs",
    "bianca_perivent_deep",
]
