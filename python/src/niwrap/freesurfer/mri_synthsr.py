# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRI_SYNTHSR_METADATA = Metadata(
    id="eb82e2176f14f70334dc8bcaf770b81e214106e0.boutiques",
    name="mri_synthsr",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MriSynthsrParameters = typing.TypedDict('MriSynthsrParameters', {
    "__STYX_TYPE__": typing.Literal["mri_synthsr"],
    "input": str,
    "output": str,
    "ct": bool,
    "disable_sharpening": bool,
    "disable_flipping": bool,
    "lowfield": bool,
    "v1": bool,
    "threads": typing.NotRequired[float | None],
    "cpu": bool,
    "model": typing.NotRequired[str | None],
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
        "mri_synthsr": mri_synthsr_cargs,
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
    }.get(t)


class MriSynthsrOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_synthsr(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def mri_synthsr_params(
    input_: str,
    output: str,
    ct: bool = False,
    disable_sharpening: bool = False,
    disable_flipping: bool = False,
    lowfield: bool = False,
    v1: bool = False,
    threads: float | None = None,
    cpu: bool = False,
    model: str | None = None,
) -> MriSynthsrParameters:
    """
    Build parameters.
    
    Args:
        input_: Image(s) to super-resolve. Can be a path to an image or to a\
            folder.
        output: Output(s), i.e., synthetic 1mm MP-RAGE(s). Must be a folder if\
            input is a folder.
        ct: Use this flag for CT scans in Hounsfield scale, it clips\
            intensities to [0,80].
        disable_sharpening: Use this flag to disable unsharp masking.
        disable_flipping: Use this flag to disable flipping augmentation at\
            test time.
        lowfield: Use model for low-field scans (e.g., acquired with\
            Hyperfine's Swoop scanner).
        v1: Use version 1 model from July 2021.
        threads: Number of cores to be used. Default is 1.
        cpu: Enforce running with CPU rather than GPU.
        model: Use a different model file.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mri_synthsr",
        "input": input_,
        "output": output,
        "ct": ct,
        "disable_sharpening": disable_sharpening,
        "disable_flipping": disable_flipping,
        "lowfield": lowfield,
        "v1": v1,
        "cpu": cpu,
    }
    if threads is not None:
        params["threads"] = threads
    if model is not None:
        params["model"] = model
    return params


def mri_synthsr_cargs(
    params: MriSynthsrParameters,
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
    cargs.append("mri_synthsr")
    cargs.append(params.get("input"))
    cargs.append(params.get("output"))
    if params.get("ct"):
        cargs.append("--ct")
    if params.get("disable_sharpening"):
        cargs.append("--disable_sharpening")
    if params.get("disable_flipping"):
        cargs.append("--disable_flipping")
    if params.get("lowfield"):
        cargs.append("--lowfield")
    if params.get("v1"):
        cargs.append("--v1")
    if params.get("threads") is not None:
        cargs.extend([
            "--threads",
            str(params.get("threads"))
        ])
    if params.get("cpu"):
        cargs.append("--cpu")
    if params.get("model") is not None:
        cargs.extend([
            "--model",
            params.get("model")
        ])
    return cargs


def mri_synthsr_outputs(
    params: MriSynthsrParameters,
    execution: Execution,
) -> MriSynthsrOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MriSynthsrOutputs(
        root=execution.output_file("."),
    )
    return ret


def mri_synthsr_execute(
    params: MriSynthsrParameters,
    execution: Execution,
) -> MriSynthsrOutputs:
    """
    Implementation of SynthSR that generates a synthetic 1mm MP-RAGE from a scan of
    any contrast and resolution.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MriSynthsrOutputs`).
    """
    cargs = mri_synthsr_cargs(params, execution)
    ret = mri_synthsr_outputs(params, execution)
    params = execution.params(params)
    execution.run(cargs)
    return ret


def mri_synthsr(
    input_: str,
    output: str,
    ct: bool = False,
    disable_sharpening: bool = False,
    disable_flipping: bool = False,
    lowfield: bool = False,
    v1: bool = False,
    threads: float | None = None,
    cpu: bool = False,
    model: str | None = None,
    runner: Runner | None = None,
) -> MriSynthsrOutputs:
    """
    Implementation of SynthSR that generates a synthetic 1mm MP-RAGE from a scan of
    any contrast and resolution.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_: Image(s) to super-resolve. Can be a path to an image or to a\
            folder.
        output: Output(s), i.e., synthetic 1mm MP-RAGE(s). Must be a folder if\
            input is a folder.
        ct: Use this flag for CT scans in Hounsfield scale, it clips\
            intensities to [0,80].
        disable_sharpening: Use this flag to disable unsharp masking.
        disable_flipping: Use this flag to disable flipping augmentation at\
            test time.
        lowfield: Use model for low-field scans (e.g., acquired with\
            Hyperfine's Swoop scanner).
        v1: Use version 1 model from July 2021.
        threads: Number of cores to be used. Default is 1.
        cpu: Enforce running with CPU rather than GPU.
        model: Use a different model file.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriSynthsrOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_SYNTHSR_METADATA)
    params = mri_synthsr_params(input_=input_, output=output, ct=ct, disable_sharpening=disable_sharpening, disable_flipping=disable_flipping, lowfield=lowfield, v1=v1, threads=threads, cpu=cpu, model=model)
    return mri_synthsr_execute(params, execution)


__all__ = [
    "MRI_SYNTHSR_METADATA",
    "MriSynthsrOutputs",
    "MriSynthsrParameters",
    "mri_synthsr",
    "mri_synthsr_params",
]
