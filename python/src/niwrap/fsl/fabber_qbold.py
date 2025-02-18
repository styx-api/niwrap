# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

FABBER_QBOLD_METADATA = Metadata(
    id="2e600bbcac1e7e271e2d687cec37980ee3a87346.boutiques",
    name="fabber_qbold",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)
FabberQboldParameters = typing.TypedDict('FabberQboldParameters', {
    "__STYX_TYPE__": typing.Literal["fabber_qbold"],
    "output_dir": str,
    "method": str,
    "model": str,
    "data": InputPathType,
    "data_n": typing.NotRequired[InputPathType | None],
    "data_order": typing.NotRequired[str | None],
    "mask": typing.NotRequired[InputPathType | None],
    "mt_n": typing.NotRequired[float | None],
    "suppdata": typing.NotRequired[InputPathType | None],
    "listmethods": bool,
    "listmodels": bool,
    "listparams": bool,
    "descparams": bool,
    "listoutputs": bool,
    "evaluate": typing.NotRequired[str | None],
    "evaluate_params": typing.NotRequired[str | None],
    "evaluate_nt": typing.NotRequired[float | None],
    "simple_output": bool,
    "overwrite": bool,
    "link_latest": bool,
    "loadmodels": typing.NotRequired[InputPathType | None],
    "dump_param_names": bool,
    "save_model_fit": bool,
    "save_residuals": bool,
    "save_model_extras": bool,
    "save_mvn": bool,
    "save_mean": bool,
    "save_std": bool,
    "save_var": bool,
    "save_zstat": bool,
    "save_noise_mean": bool,
    "save_noise_std": bool,
    "save_free_energy": bool,
    "optfile": typing.NotRequired[InputPathType | None],
    "debug": bool,
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
        "fabber_qbold": fabber_qbold_cargs,
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
        "fabber_qbold": fabber_qbold_outputs,
    }.get(t)


class FabberQboldOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fabber_qbold(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    paramnames_file: OutputPathType
    """File containing the names of the model parameters"""
    model_fit_file: OutputPathType
    """4D volume of the model prediction"""
    residuals_file: OutputPathType
    """4D volume of the residuals"""
    model_extras_file: OutputPathType
    """Additional model-specific timeseries data"""
    mvn_file: OutputPathType
    """File containing the final MVN distributions"""
    mean_file: OutputPathType
    """File containing the parameter means"""
    std_file: OutputPathType
    """File containing the parameter standard deviations"""
    var_file: OutputPathType
    """File containing the parameter variances"""
    zstat_file: OutputPathType
    """File containing the parameter Zstats"""
    noise_mean_file: OutputPathType
    """File containing the noise means"""
    noise_std_file: OutputPathType
    """File containing the noise standard deviations"""
    free_energy_file: OutputPathType
    """File containing the free energy, if calculated"""
    logfile: OutputPathType
    """Logfile of the execution"""


def fabber_qbold_params(
    output_dir: str,
    method: str,
    model: str,
    data: InputPathType,
    data_n: InputPathType | None = None,
    data_order: str | None = "interleave",
    mask: InputPathType | None = None,
    mt_n: float | None = None,
    suppdata: InputPathType | None = None,
    listmethods: bool = False,
    listmodels: bool = False,
    listparams: bool = False,
    descparams: bool = False,
    listoutputs: bool = False,
    evaluate: str | None = None,
    evaluate_params: str | None = None,
    evaluate_nt: float | None = None,
    simple_output: bool = False,
    overwrite: bool = False,
    link_latest: bool = False,
    loadmodels: InputPathType | None = None,
    dump_param_names: bool = False,
    save_model_fit: bool = False,
    save_residuals: bool = False,
    save_model_extras: bool = False,
    save_mvn: bool = False,
    save_mean: bool = False,
    save_std: bool = False,
    save_var: bool = False,
    save_zstat: bool = False,
    save_noise_mean: bool = False,
    save_noise_std: bool = False,
    save_free_energy: bool = False,
    optfile: InputPathType | None = None,
    debug: bool = False,
) -> FabberQboldParameters:
    """
    Build parameters.
    
    Args:
        output_dir: Directory for output files (including logfile).
        method: Use this inference method.
        model: Use this forward model.
        data: Specify a single input data file.
        data_n: Specify multiple data files for n=1, 2, 3...
        data_order: If multiple data files are specified, how they will be\
            handled: concatenate = one after the other, interleave = first record\
            from each file, then second, etc.
        mask: Mask file. Inference will only be performed where mask value > 0.
        mt_n: List of masked time points, indexed from 1. These will be ignored\
            in the parameter updates.
        suppdata: 'Supplemental' timeseries data, required for some models.
        listmethods: List all known inference methods.
        listmodels: List all known forward models.
        listparams: List model parameters (requires model configuration options\
            to be given).
        descparams: Descript model parameters (name, description, units) -\
            requires model configuration options to be given. Note that not all\
            models provide parameter descriptions.
        listoutputs: List additional model outputs (requires model\
            configuration options to be given).
        evaluate: Evaluate model. Set to name of output required or blank for\
            default output. Requires model configuration options, --evaluate-params\
            and --evaluate-nt.
        evaluate_params: List of parameter values for evaluation.
        evaluate_nt: Number of time points for evaluation - must be consistent\
            with model options where appropriate.
        simple_output: Instead of usual standard output, simply output series\
            of lines each giving progress as percentage.
        overwrite: If set will overwrite existing output. If not set, new\
            output directories will be created by appending '+' to the directory\
            name.
        link_latest: Try to create a link to the most recent output directory\
            with the prefix _latest.
        loadmodels: Load models dynamically from the specified filename, which\
            should be a DLL/shared library.
        dump_param_names: Write the file paramnames.txt containing the names of\
            the model parameters.
        save_model_fit: Output the model prediction as a 4d volume.
        save_residuals: Output the residuals (difference between the data and\
            the model prediction).
        save_model_extras: Output any additional model-specific timeseries data.
        save_mvn: Output the final MVN distributions.
        save_mean: Output the parameter means.
        save_std: Output the parameter standard deviations.
        save_var: Output the parameter variances.
        save_zstat: Output the parameter Zstats.
        save_noise_mean: Output the noise means. The noise distribution\
            inferred is the precision of a Gaussian noise source.
        save_noise_std: Output the noise standard deviations.
        save_free_energy: Output the free energy, if calculated.
        optfile: File containing additional options, one per line, in the same\
            form as specified on the command line.
        debug: Output large amounts of debug information. ONLY USE WITH VERY\
            SMALL NUMBERS OF VOXELS.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "fabber_qbold",
        "output_dir": output_dir,
        "method": method,
        "model": model,
        "data": data,
        "listmethods": listmethods,
        "listmodels": listmodels,
        "listparams": listparams,
        "descparams": descparams,
        "listoutputs": listoutputs,
        "simple_output": simple_output,
        "overwrite": overwrite,
        "link_latest": link_latest,
        "dump_param_names": dump_param_names,
        "save_model_fit": save_model_fit,
        "save_residuals": save_residuals,
        "save_model_extras": save_model_extras,
        "save_mvn": save_mvn,
        "save_mean": save_mean,
        "save_std": save_std,
        "save_var": save_var,
        "save_zstat": save_zstat,
        "save_noise_mean": save_noise_mean,
        "save_noise_std": save_noise_std,
        "save_free_energy": save_free_energy,
        "debug": debug,
    }
    if data_n is not None:
        params["data_n"] = data_n
    if data_order is not None:
        params["data_order"] = data_order
    if mask is not None:
        params["mask"] = mask
    if mt_n is not None:
        params["mt_n"] = mt_n
    if suppdata is not None:
        params["suppdata"] = suppdata
    if evaluate is not None:
        params["evaluate"] = evaluate
    if evaluate_params is not None:
        params["evaluate_params"] = evaluate_params
    if evaluate_nt is not None:
        params["evaluate_nt"] = evaluate_nt
    if loadmodels is not None:
        params["loadmodels"] = loadmodels
    if optfile is not None:
        params["optfile"] = optfile
    return params


def fabber_qbold_cargs(
    params: FabberQboldParameters,
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
    cargs.append("fabber_qbold")
    cargs.extend([
        "--output",
        params.get("output_dir")
    ])
    cargs.extend([
        "--method",
        params.get("method")
    ])
    cargs.extend([
        "--model",
        params.get("model")
    ])
    cargs.extend([
        "--data",
        execution.input_file(params.get("data"))
    ])
    if params.get("data_n") is not None:
        cargs.extend([
            "--data<n>",
            execution.input_file(params.get("data_n"))
        ])
    if params.get("data_order") is not None:
        cargs.extend([
            "--data-order",
            params.get("data_order")
        ])
    if params.get("mask") is not None:
        cargs.extend([
            "--mask",
            execution.input_file(params.get("mask"))
        ])
    if params.get("mt_n") is not None:
        cargs.extend([
            "--mt<n>",
            str(params.get("mt_n"))
        ])
    if params.get("suppdata") is not None:
        cargs.extend([
            "--suppdata",
            execution.input_file(params.get("suppdata"))
        ])
    if params.get("listmethods"):
        cargs.append("--listmethods")
    if params.get("listmodels"):
        cargs.append("--listmodels")
    if params.get("listparams"):
        cargs.append("--listparams")
    if params.get("descparams"):
        cargs.append("--descparams")
    if params.get("listoutputs"):
        cargs.append("--listoutputs")
    if params.get("evaluate") is not None:
        cargs.extend([
            "--evaluate",
            params.get("evaluate")
        ])
    if params.get("evaluate_params") is not None:
        cargs.extend([
            "--evaluate-params",
            params.get("evaluate_params")
        ])
    if params.get("evaluate_nt") is not None:
        cargs.extend([
            "--evaluate-nt",
            str(params.get("evaluate_nt"))
        ])
    if params.get("simple_output"):
        cargs.append("--simple-output")
    if params.get("overwrite"):
        cargs.append("--overwrite")
    if params.get("link_latest"):
        cargs.append("--link-to-latest")
    if params.get("loadmodels") is not None:
        cargs.extend([
            "--loadmodels",
            execution.input_file(params.get("loadmodels"))
        ])
    if params.get("dump_param_names"):
        cargs.append("--dump-param-names")
    if params.get("save_model_fit"):
        cargs.append("--save-model-fit")
    if params.get("save_residuals"):
        cargs.append("--save-residuals")
    if params.get("save_model_extras"):
        cargs.append("--save-model-extras")
    if params.get("save_mvn"):
        cargs.append("--save-mvn")
    if params.get("save_mean"):
        cargs.append("--save-mean")
    if params.get("save_std"):
        cargs.append("--save-std")
    if params.get("save_var"):
        cargs.append("--save-var")
    if params.get("save_zstat"):
        cargs.append("--save-zstat")
    if params.get("save_noise_mean"):
        cargs.append("--save-noise-mean")
    if params.get("save_noise_std"):
        cargs.append("--save-noise-std")
    if params.get("save_free_energy"):
        cargs.append("--save-free-energy")
    if params.get("optfile") is not None:
        cargs.extend([
            "--optfile",
            execution.input_file(params.get("optfile"))
        ])
    if params.get("debug"):
        cargs.append("--debug")
    return cargs


def fabber_qbold_outputs(
    params: FabberQboldParameters,
    execution: Execution,
) -> FabberQboldOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = FabberQboldOutputs(
        root=execution.output_file("."),
        paramnames_file=execution.output_file(params.get("output_dir") + "/paramnames.txt"),
        model_fit_file=execution.output_file(params.get("output_dir") + "/model_fit.nii.gz"),
        residuals_file=execution.output_file(params.get("output_dir") + "/residuals.nii.gz"),
        model_extras_file=execution.output_file(params.get("output_dir") + "/model_extras.nii.gz"),
        mvn_file=execution.output_file(params.get("output_dir") + "/mvn.nii.gz"),
        mean_file=execution.output_file(params.get("output_dir") + "/mean.nii.gz"),
        std_file=execution.output_file(params.get("output_dir") + "/std.nii.gz"),
        var_file=execution.output_file(params.get("output_dir") + "/var.nii.gz"),
        zstat_file=execution.output_file(params.get("output_dir") + "/zstat.nii.gz"),
        noise_mean_file=execution.output_file(params.get("output_dir") + "/noise_mean.nii.gz"),
        noise_std_file=execution.output_file(params.get("output_dir") + "/noise_std.nii.gz"),
        free_energy_file=execution.output_file(params.get("output_dir") + "/free_energy.nii.gz"),
        logfile=execution.output_file(params.get("output_dir") + "/logfile.txt"),
    )
    return ret


def fabber_qbold_execute(
    params: FabberQboldParameters,
    execution: Execution,
) -> FabberQboldOutputs:
    """
    Fabber - a flexible BaYesian modeling framework for FMRI and MRI analysis.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `FabberQboldOutputs`).
    """
    cargs = fabber_qbold_cargs(params, execution)
    ret = fabber_qbold_outputs(params, execution)
    params = execution.params(params)
    execution.run(cargs)
    return ret


def fabber_qbold(
    output_dir: str,
    method: str,
    model: str,
    data: InputPathType,
    data_n: InputPathType | None = None,
    data_order: str | None = "interleave",
    mask: InputPathType | None = None,
    mt_n: float | None = None,
    suppdata: InputPathType | None = None,
    listmethods: bool = False,
    listmodels: bool = False,
    listparams: bool = False,
    descparams: bool = False,
    listoutputs: bool = False,
    evaluate: str | None = None,
    evaluate_params: str | None = None,
    evaluate_nt: float | None = None,
    simple_output: bool = False,
    overwrite: bool = False,
    link_latest: bool = False,
    loadmodels: InputPathType | None = None,
    dump_param_names: bool = False,
    save_model_fit: bool = False,
    save_residuals: bool = False,
    save_model_extras: bool = False,
    save_mvn: bool = False,
    save_mean: bool = False,
    save_std: bool = False,
    save_var: bool = False,
    save_zstat: bool = False,
    save_noise_mean: bool = False,
    save_noise_std: bool = False,
    save_free_energy: bool = False,
    optfile: InputPathType | None = None,
    debug: bool = False,
    runner: Runner | None = None,
) -> FabberQboldOutputs:
    """
    Fabber - a flexible BaYesian modeling framework for FMRI and MRI analysis.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        output_dir: Directory for output files (including logfile).
        method: Use this inference method.
        model: Use this forward model.
        data: Specify a single input data file.
        data_n: Specify multiple data files for n=1, 2, 3...
        data_order: If multiple data files are specified, how they will be\
            handled: concatenate = one after the other, interleave = first record\
            from each file, then second, etc.
        mask: Mask file. Inference will only be performed where mask value > 0.
        mt_n: List of masked time points, indexed from 1. These will be ignored\
            in the parameter updates.
        suppdata: 'Supplemental' timeseries data, required for some models.
        listmethods: List all known inference methods.
        listmodels: List all known forward models.
        listparams: List model parameters (requires model configuration options\
            to be given).
        descparams: Descript model parameters (name, description, units) -\
            requires model configuration options to be given. Note that not all\
            models provide parameter descriptions.
        listoutputs: List additional model outputs (requires model\
            configuration options to be given).
        evaluate: Evaluate model. Set to name of output required or blank for\
            default output. Requires model configuration options, --evaluate-params\
            and --evaluate-nt.
        evaluate_params: List of parameter values for evaluation.
        evaluate_nt: Number of time points for evaluation - must be consistent\
            with model options where appropriate.
        simple_output: Instead of usual standard output, simply output series\
            of lines each giving progress as percentage.
        overwrite: If set will overwrite existing output. If not set, new\
            output directories will be created by appending '+' to the directory\
            name.
        link_latest: Try to create a link to the most recent output directory\
            with the prefix _latest.
        loadmodels: Load models dynamically from the specified filename, which\
            should be a DLL/shared library.
        dump_param_names: Write the file paramnames.txt containing the names of\
            the model parameters.
        save_model_fit: Output the model prediction as a 4d volume.
        save_residuals: Output the residuals (difference between the data and\
            the model prediction).
        save_model_extras: Output any additional model-specific timeseries data.
        save_mvn: Output the final MVN distributions.
        save_mean: Output the parameter means.
        save_std: Output the parameter standard deviations.
        save_var: Output the parameter variances.
        save_zstat: Output the parameter Zstats.
        save_noise_mean: Output the noise means. The noise distribution\
            inferred is the precision of a Gaussian noise source.
        save_noise_std: Output the noise standard deviations.
        save_free_energy: Output the free energy, if calculated.
        optfile: File containing additional options, one per line, in the same\
            form as specified on the command line.
        debug: Output large amounts of debug information. ONLY USE WITH VERY\
            SMALL NUMBERS OF VOXELS.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FabberQboldOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FABBER_QBOLD_METADATA)
    params = fabber_qbold_params(output_dir=output_dir, method=method, model=model, data=data, data_n=data_n, data_order=data_order, mask=mask, mt_n=mt_n, suppdata=suppdata, listmethods=listmethods, listmodels=listmodels, listparams=listparams, descparams=descparams, listoutputs=listoutputs, evaluate=evaluate, evaluate_params=evaluate_params, evaluate_nt=evaluate_nt, simple_output=simple_output, overwrite=overwrite, link_latest=link_latest, loadmodels=loadmodels, dump_param_names=dump_param_names, save_model_fit=save_model_fit, save_residuals=save_residuals, save_model_extras=save_model_extras, save_mvn=save_mvn, save_mean=save_mean, save_std=save_std, save_var=save_var, save_zstat=save_zstat, save_noise_mean=save_noise_mean, save_noise_std=save_noise_std, save_free_energy=save_free_energy, optfile=optfile, debug=debug)
    return fabber_qbold_execute(params, execution)


__all__ = [
    "FABBER_QBOLD_METADATA",
    "FabberQboldOutputs",
    "FabberQboldParameters",
    "fabber_qbold",
    "fabber_qbold_params",
]
