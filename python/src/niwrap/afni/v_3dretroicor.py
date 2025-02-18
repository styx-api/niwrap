# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V_3DRETROICOR_METADATA = Metadata(
    id="0b8e3bbd9eaa6f16498a0393158cdcd367502347.boutiques",
    name="3dretroicor",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
V3dretroicorParameters = typing.TypedDict('V3dretroicorParameters', {
    "__STYX_TYPE__": typing.Literal["3dretroicor"],
    "ignore": typing.NotRequired[float | None],
    "prefix": typing.NotRequired[str | None],
    "card": typing.NotRequired[InputPathType | None],
    "cardphase": typing.NotRequired[str | None],
    "threshold": typing.NotRequired[float | None],
    "resp": typing.NotRequired[InputPathType | None],
    "respphase": typing.NotRequired[str | None],
    "order": typing.NotRequired[float | None],
    "dataset": InputPathType,
})


def dyn_cargs(
    t: str,
) -> typing.Any:
    """
    Get build cargs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build cargs function.
    """
    return {
        "3dretroicor": v_3dretroicor_cargs,
    }.get(t)


def dyn_outputs(
    t: str,
) -> typing.Any:
    """
    Get build outputs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build outputs function.
    """
    return {
        "3dretroicor": v_3dretroicor_outputs,
    }.get(t)


class V3dretroicorOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3dretroicor(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    corrected_dataset: OutputPathType | None
    """Corrected dataset output."""
    output_cardiac_phase: OutputPathType | None
    """Cardiac phase output file."""
    output_resp_phase: OutputPathType | None
    """Respiratory phase output file."""


def v_3dretroicor_params(
    dataset: InputPathType,
    ignore: float | None = None,
    prefix: str | None = None,
    card: InputPathType | None = None,
    cardphase: str | None = None,
    threshold: float | None = None,
    resp: InputPathType | None = None,
    respphase: str | None = None,
    order: float | None = None,
) -> V3dretroicorParameters:
    """
    Build parameters.
    
    Args:
        dataset: 3D+time dataset to process.
        ignore: The number of initial timepoints to ignore in the input. These\
            points will be passed through uncorrected.
        prefix: Prefix for new, corrected dataset.
        card: 1D cardiac data file for cardiac correction.
        cardphase: Filename for 1D cardiac phase output.
        threshold: Threshold for detection of R-wave peaks in input. Make sure\
            it's above the background noise level; try 3/4 or 4/5 times range plus\
            minimum.
        resp: 1D respiratory waveform data for correction.
        respphase: Filename for 1D respiratory phase output.
        order: The order of the correction. Higher-order terms yield little\
            improvement according to Glover et al.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "3dretroicor",
        "dataset": dataset,
    }
    if ignore is not None:
        params["ignore"] = ignore
    if prefix is not None:
        params["prefix"] = prefix
    if card is not None:
        params["card"] = card
    if cardphase is not None:
        params["cardphase"] = cardphase
    if threshold is not None:
        params["threshold"] = threshold
    if resp is not None:
        params["resp"] = resp
    if respphase is not None:
        params["respphase"] = respphase
    if order is not None:
        params["order"] = order
    return params


def v_3dretroicor_cargs(
    params: V3dretroicorParameters,
    execution: Execution,
) -> list[str]:
    """
    Build command-line arguments from parameters.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Command-line arguments.
    """
    cargs = []
    cargs.append("3dretroicor")
    if params.get("ignore") is not None:
        cargs.extend([
            "-ignore",
            str(params.get("ignore"))
        ])
    if params.get("prefix") is not None:
        cargs.extend([
            "-prefix",
            params.get("prefix")
        ])
    if params.get("card") is not None:
        cargs.extend([
            "-card",
            execution.input_file(params.get("card"))
        ])
    if params.get("cardphase") is not None:
        cargs.extend([
            "-cardphase",
            params.get("cardphase")
        ])
    if params.get("threshold") is not None:
        cargs.extend([
            "-threshold",
            str(params.get("threshold"))
        ])
    if params.get("resp") is not None:
        cargs.extend([
            "-resp",
            execution.input_file(params.get("resp"))
        ])
    if params.get("respphase") is not None:
        cargs.extend([
            "-respphase",
            params.get("respphase")
        ])
    if params.get("order") is not None:
        cargs.extend([
            "-order",
            str(params.get("order"))
        ])
    cargs.append(execution.input_file(params.get("dataset")))
    return cargs


def v_3dretroicor_outputs(
    params: V3dretroicorParameters,
    execution: Execution,
) -> V3dretroicorOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V3dretroicorOutputs(
        root=execution.output_file("."),
        corrected_dataset=execution.output_file(params.get("prefix") + ".nii.gz") if (params.get("prefix") is not None) else None,
        output_cardiac_phase=execution.output_file(params.get("cardphase")) if (params.get("cardphase") is not None) else None,
        output_resp_phase=execution.output_file(params.get("respphase")) if (params.get("respphase") is not None) else None,
    )
    return ret


def v_3dretroicor_execute(
    params: V3dretroicorParameters,
    execution: Execution,
) -> V3dretroicorOutputs:
    """
    Performs Retrospective Image Correction for physiological motion effects using a
    modified RETROICOR algorithm.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V3dretroicorOutputs`).
    """
    cargs = v_3dretroicor_cargs(params, execution)
    ret = v_3dretroicor_outputs(params, execution)
    params = execution.params(params)
    execution.run(cargs)
    return ret


def v_3dretroicor(
    dataset: InputPathType,
    ignore: float | None = None,
    prefix: str | None = None,
    card: InputPathType | None = None,
    cardphase: str | None = None,
    threshold: float | None = None,
    resp: InputPathType | None = None,
    respphase: str | None = None,
    order: float | None = None,
    runner: Runner | None = None,
) -> V3dretroicorOutputs:
    """
    Performs Retrospective Image Correction for physiological motion effects using a
    modified RETROICOR algorithm.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        dataset: 3D+time dataset to process.
        ignore: The number of initial timepoints to ignore in the input. These\
            points will be passed through uncorrected.
        prefix: Prefix for new, corrected dataset.
        card: 1D cardiac data file for cardiac correction.
        cardphase: Filename for 1D cardiac phase output.
        threshold: Threshold for detection of R-wave peaks in input. Make sure\
            it's above the background noise level; try 3/4 or 4/5 times range plus\
            minimum.
        resp: 1D respiratory waveform data for correction.
        respphase: Filename for 1D respiratory phase output.
        order: The order of the correction. Higher-order terms yield little\
            improvement according to Glover et al.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dretroicorOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3DRETROICOR_METADATA)
    params = v_3dretroicor_params(ignore=ignore, prefix=prefix, card=card, cardphase=cardphase, threshold=threshold, resp=resp, respphase=respphase, order=order, dataset=dataset)
    return v_3dretroicor_execute(params, execution)


__all__ = [
    "V3dretroicorOutputs",
    "V3dretroicorParameters",
    "V_3DRETROICOR_METADATA",
    "v_3dretroicor",
    "v_3dretroicor_params",
]
