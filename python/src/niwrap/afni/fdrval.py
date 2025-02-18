# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

FDRVAL_METADATA = Metadata(
    id="f92df9dc9c7bd351f5f06439c97a5434e22b31b8.boutiques",
    name="fdrval",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
FdrvalParameters = typing.TypedDict('FdrvalParameters', {
    "__STYX_TYPE__": typing.Literal["fdrval"],
    "dset": InputPathType,
    "sub": float,
    "val_list": list[float],
    "pval": bool,
    "ponly": bool,
    "qonly": bool,
    "qinput": bool,
    "inverse": bool,
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
        "fdrval": fdrval_cargs,
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
        "fdrval": fdrval_outputs,
    }.get(t)


class FdrvalOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fdrval(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output: OutputPathType
    """Computed q-values or p-values for the given thresholds"""


def fdrval_params(
    dset: InputPathType,
    sub: float,
    val_list: list[float],
    pval: bool = False,
    ponly: bool = False,
    qonly: bool = False,
    qinput: bool = False,
    inverse: bool = False,
) -> FdrvalParameters:
    """
    Build parameters.
    
    Args:
        dset: Input dataset.
        sub: Sub-brick number.
        val_list: List of threshold values.
        pval: Output the p-value (on the same line, after q).
        ponly: Don't output q-values, just p-values.
        qonly: Don't output p-values, just q-values.
        qinput: The 'val' inputs are taken to be q-values and then the outputs\
            are the corresponding statistical thresholds.
        inverse: Inverse of the usual operation. 'Val' inputs must be between 0\
            and 1 (exclusive). Cannot be used with '-ponly' or '-pval'.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "fdrval",
        "dset": dset,
        "sub": sub,
        "val_list": val_list,
        "pval": pval,
        "ponly": ponly,
        "qonly": qonly,
        "qinput": qinput,
        "inverse": inverse,
    }
    return params


def fdrval_cargs(
    params: FdrvalParameters,
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
    cargs.append("fdrval")
    cargs.append(execution.input_file(params.get("dset")))
    cargs.append(str(params.get("sub")))
    cargs.extend(map(str, params.get("val_list")))
    if params.get("pval"):
        cargs.append("-pval")
    if params.get("ponly"):
        cargs.append("-ponly")
    if params.get("qonly"):
        cargs.append("-qonly")
    if params.get("qinput"):
        cargs.append("-qinput")
    if params.get("inverse"):
        cargs.append("-inverse")
    return cargs


def fdrval_outputs(
    params: FdrvalParameters,
    execution: Execution,
) -> FdrvalOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = FdrvalOutputs(
        root=execution.output_file("."),
        output=execution.output_file("stdout.txt"),
    )
    return ret


def fdrval_execute(
    params: FdrvalParameters,
    execution: Execution,
) -> FdrvalOutputs:
    """
    Computes q-values from FDR curve data stored in dataset headers.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `FdrvalOutputs`).
    """
    cargs = fdrval_cargs(params, execution)
    ret = fdrval_outputs(params, execution)
    params = execution.params(params)
    execution.run(cargs)
    return ret


def fdrval(
    dset: InputPathType,
    sub: float,
    val_list: list[float],
    pval: bool = False,
    ponly: bool = False,
    qonly: bool = False,
    qinput: bool = False,
    inverse: bool = False,
    runner: Runner | None = None,
) -> FdrvalOutputs:
    """
    Computes q-values from FDR curve data stored in dataset headers.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        dset: Input dataset.
        sub: Sub-brick number.
        val_list: List of threshold values.
        pval: Output the p-value (on the same line, after q).
        ponly: Don't output q-values, just p-values.
        qonly: Don't output p-values, just q-values.
        qinput: The 'val' inputs are taken to be q-values and then the outputs\
            are the corresponding statistical thresholds.
        inverse: Inverse of the usual operation. 'Val' inputs must be between 0\
            and 1 (exclusive). Cannot be used with '-ponly' or '-pval'.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FdrvalOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FDRVAL_METADATA)
    params = fdrval_params(dset=dset, sub=sub, val_list=val_list, pval=pval, ponly=ponly, qonly=qonly, qinput=qinput, inverse=inverse)
    return fdrval_execute(params, execution)


__all__ = [
    "FDRVAL_METADATA",
    "FdrvalOutputs",
    "FdrvalParameters",
    "fdrval",
    "fdrval_params",
]
