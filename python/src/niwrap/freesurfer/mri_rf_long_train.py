# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRI_RF_LONG_TRAIN_METADATA = Metadata(
    id="ca8cfed56cb5ee7d0c2ebca92a97eb2150fb4bb6.boutiques",
    name="mri_rf_long_train",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class MriRfLongTrainOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_rf_long_train(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_rfa_file: OutputPathType
    """The output RFA file generated by the tool"""


def mri_rf_long_train(
    seg_dir: str,
    xform: str,
    subjects: list[str],
    output_rfa: str,
    mask: str | None = None,
    node_spacing: float | None = None,
    prior_spacing: float | None = None,
    input_data: list[str] | None = None,
    check: bool = False,
    runner: Runner | None = None,
) -> MriRfLongTrainOutputs:
    """
    Trains GCA data with multiple subjects for FreeSurfer.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        seg_dir: Path to the segmentation volume directory, relative to\
            $subject/mri.
        xform: Atlas transform path relative to $subject/mri/transforms.
        subjects: List of subjects for training.
        output_rfa: Output RFA filename.
        mask: Volume name to use as a mask, path relative to $subject/mri.
        node_spacing: Spacing of classifiers in canonical space.
        prior_spacing: Spacing of class priors in canonical space.
        input_data: Specify training data, path relative to $subject/mri. Can\
            specify multiple inputs. Defaults to 'orig' if not specified.
        check: Conduct sanity-check of labels for obvious edit errors.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriRfLongTrainOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_RF_LONG_TRAIN_METADATA)
    cargs = []
    cargs.append("mri_rf_long_train")
    cargs.extend([
        "-seg",
        seg_dir
    ])
    cargs.extend([
        "-xform",
        xform
    ])
    if mask is not None:
        cargs.extend([
            "-mask",
            mask
        ])
    if node_spacing is not None:
        cargs.extend([
            "-node_spacing",
            str(node_spacing)
        ])
    if prior_spacing is not None:
        cargs.extend([
            "-prior_spacing",
            str(prior_spacing)
        ])
    if input_data is not None:
        cargs.extend([
            "-input",
            *input_data
        ])
    if check:
        cargs.append("-check")
    cargs.extend(subjects)
    cargs.append(output_rfa)
    ret = MriRfLongTrainOutputs(
        root=execution.output_file("."),
        output_rfa_file=execution.output_file(output_rfa + ".rfa"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MRI_RF_LONG_TRAIN_METADATA",
    "MriRfLongTrainOutputs",
    "mri_rf_long_train",
]
