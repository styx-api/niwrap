# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

FABBER_ASL_METADATA = Metadata(
    id="647be30118b780fbc6ab5e74dac57d1cebe1cb75.boutiques",
    name="fabber_asl",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)


class FabberAslOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fabber_asl(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    logfile: OutputPathType
    """Log file of Fabber output"""
    modelfit: OutputPathType
    """Model fit output"""
    residuals: OutputPathType
    """Residuals output"""
    model_extras: OutputPathType
    """Model specific timeseries data"""
    mvn: OutputPathType
    """MVN distributions"""
    means: OutputPathType
    """Parameter means"""
    stds: OutputPathType
    """Parameter standard deviations"""
    variances: OutputPathType
    """Parameter variances"""
    zstats: OutputPathType
    """Parameter Zstats"""
    noise_means: OutputPathType
    """Noise means"""
    noise_stds: OutputPathType
    """Noise standard deviations"""
    free_energy: OutputPathType
    """Free energy"""


def fabber_asl(
    output: str,
    method: str,
    model: str,
    data: InputPathType,
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
    link_to_latest: bool = False,
    loadmodels: InputPathType | None = None,
    mask: InputPathType | None = None,
    suppdata: InputPathType | None = None,
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
    optfile: str | None = None,
    debug: bool = False,
    runner: Runner | None = None,
) -> FabberAslOutputs:
    """
    Fabber is a tool for automated model fitting of time series data.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        output: Directory for output files (including logfile).
        method: Use this inference method.
        model: Use this forward model.
        data: Specify a single input data file.
        listmethods: List all known inference methods.
        listmodels: List all known forward models.
        listparams: List model parameters (requires model configuration options\
            to be given).
        descparams: Describe model parameters (name, description, units) -\
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
        link_to_latest: Try to create a link to the most recent output\
            directory with the prefix _latest.
        loadmodels: Load models dynamically from the specified filename, which\
            should be a DLL/shared library.
        mask: Mask file. Inference will only be performed where mask value > 0.
        suppdata: 'Supplemental' timeseries data, required for some models.
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
        NamedTuple of outputs (described in `FabberAslOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FABBER_ASL_METADATA)
    cargs = []
    cargs.append("fabber_asl")
    if listmethods:
        cargs.append("--listmethods")
    if listmodels:
        cargs.append("--listmodels")
    if listparams:
        cargs.append("--listparams")
    if descparams:
        cargs.append("--descparams")
    if listoutputs:
        cargs.append("--listoutputs")
    if evaluate is not None:
        cargs.append(evaluate)
    if evaluate_params is not None:
        cargs.append(evaluate_params)
    if evaluate_nt is not None:
        cargs.append(str(evaluate_nt))
    if simple_output:
        cargs.append("--simple-output")
    cargs.append(output)
    if overwrite:
        cargs.append("--overwrite")
    if link_to_latest:
        cargs.append("--link-to-latest")
    cargs.append(method)
    cargs.append(model)
    if loadmodels is not None:
        cargs.append(execution.input_file(loadmodels))
    cargs.append(execution.input_file(data))
    if mask is not None:
        cargs.append(execution.input_file(mask))
    if suppdata is not None:
        cargs.append(execution.input_file(suppdata))
    if dump_param_names:
        cargs.append("--dump-param-names")
    if save_model_fit:
        cargs.append("--save-model-fit")
    if save_residuals:
        cargs.append("--save-residuals")
    if save_model_extras:
        cargs.append("--save-model-extras")
    if save_mvn:
        cargs.append("--save-mvn")
    if save_mean:
        cargs.append("--save-mean")
    if save_std:
        cargs.append("--save-std")
    if save_var:
        cargs.append("--save-var")
    if save_zstat:
        cargs.append("--save-zstat")
    if save_noise_mean:
        cargs.append("--save-noise-mean")
    if save_noise_std:
        cargs.append("--save-noise-std")
    if save_free_energy:
        cargs.append("--save-free-energy")
    if optfile is not None:
        cargs.append(optfile)
    if debug:
        cargs.append("--debug")
    ret = FabberAslOutputs(
        root=execution.output_file("."),
        logfile=execution.output_file(output + "/logfile.txt"),
        modelfit=execution.output_file(output + "/model_fit.nii.gz"),
        residuals=execution.output_file(output + "/residuals.nii.gz"),
        model_extras=execution.output_file(output + "/extras.nii.gz"),
        mvn=execution.output_file(output + "/mvn.nii.gz"),
        means=execution.output_file(output + "/means.nii.gz"),
        stds=execution.output_file(output + "/stds.nii.gz"),
        variances=execution.output_file(output + "/variances.nii.gz"),
        zstats=execution.output_file(output + "/zstats.nii.gz"),
        noise_means=execution.output_file(output + "/noise_means.nii.gz"),
        noise_stds=execution.output_file(output + "/noise_stds.nii.gz"),
        free_energy=execution.output_file(output + "/free_energy.nii.gz"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "FABBER_ASL_METADATA",
    "FabberAslOutputs",
    "fabber_asl",
]
