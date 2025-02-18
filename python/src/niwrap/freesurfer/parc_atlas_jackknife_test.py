# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

PARC_ATLAS_JACKKNIFE_TEST_METADATA = Metadata(
    id="c3bca782ff73ffb7144b8a68ae203b8cb4791e7f.boutiques",
    name="parc_atlas_jackknife_test",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
ParcAtlasJackknifeTestParameters = typing.TypedDict('ParcAtlasJackknifeTestParameters', {
    "__STYX_TYPE__": typing.Literal["parc_atlas_jackknife_test"],
    "register": bool,
    "reg_dist": typing.NotRequired[str | None],
    "reg_append": typing.NotRequired[str | None],
    "reg_copy": typing.NotRequired[str | None],
    "train": bool,
    "classify": bool,
    "test": bool,
    "all": bool,
    "subjects_dir": typing.NotRequired[str | None],
    "freesurfer_home": typing.NotRequired[str | None],
    "binaries_path": typing.NotRequired[str | None],
    "dontrun": bool,
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
        "parc_atlas_jackknife_test": parc_atlas_jackknife_test_cargs,
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
        "parc_atlas_jackknife_test": parc_atlas_jackknife_test_outputs,
    }.get(t)


class ParcAtlasJackknifeTestOutputs(typing.NamedTuple):
    """
    Output object returned when calling `parc_atlas_jackknife_test(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    jackknife_output: OutputPathType
    """Output files written to the directory named 'jackknife'."""


def parc_atlas_jackknife_test_params(
    register: bool = False,
    reg_dist: str | None = None,
    reg_append: str | None = None,
    reg_copy: str | None = None,
    train: bool = False,
    classify: bool = False,
    test: bool = False,
    all_: bool = False,
    subjects_dir: str | None = None,
    freesurfer_home: str | None = None,
    binaries_path: str | None = None,
    dontrun: bool = False,
) -> ParcAtlasJackknifeTestParameters:
    """
    Build parameters.
    
    Args:
        register: Run mris_register: creates .sphere.reg files.
        reg_dist: Run mris_register with '-dist <arg>' flag.
        reg_append: Append <string> to end of ?h.sphere.reg.
        reg_copy: Copy ?h.sphere.reg<string> ?h.sphere.reg.
        train: Run mris_ca_train: creates .gcs files.
        classify: Run mris_ca_label: creates .annot files.
        test: Run mris_compute_parc_overlap.
        all_: Run train, classify, and test.
        subjects_dir: Override default subjects directory.
        freesurfer_home: Source a new FREESURFER_HOME.
        binaries_path: Specify override path to binaries.
        dontrun: Don't execute the commands.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "parc_atlas_jackknife_test",
        "register": register,
        "train": train,
        "classify": classify,
        "test": test,
        "all": all_,
        "dontrun": dontrun,
    }
    if reg_dist is not None:
        params["reg_dist"] = reg_dist
    if reg_append is not None:
        params["reg_append"] = reg_append
    if reg_copy is not None:
        params["reg_copy"] = reg_copy
    if subjects_dir is not None:
        params["subjects_dir"] = subjects_dir
    if freesurfer_home is not None:
        params["freesurfer_home"] = freesurfer_home
    if binaries_path is not None:
        params["binaries_path"] = binaries_path
    return params


def parc_atlas_jackknife_test_cargs(
    params: ParcAtlasJackknifeTestParameters,
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
    cargs.append("parc_atlas_jackknife_test")
    if params.get("register"):
        cargs.append("-register")
    if params.get("reg_dist") is not None:
        cargs.extend([
            "-reg_dist",
            params.get("reg_dist")
        ])
    if params.get("reg_append") is not None:
        cargs.extend([
            "-reg_append",
            params.get("reg_append")
        ])
    if params.get("reg_copy") is not None:
        cargs.extend([
            "-reg_copy",
            params.get("reg_copy")
        ])
    if params.get("train"):
        cargs.append("-train")
    if params.get("classify"):
        cargs.append("-classify")
    if params.get("test"):
        cargs.append("-test")
    if params.get("all"):
        cargs.append("-all")
    if params.get("subjects_dir") is not None:
        cargs.extend([
            "-sd",
            params.get("subjects_dir")
        ])
    if params.get("freesurfer_home") is not None:
        cargs.extend([
            "-fshome",
            params.get("freesurfer_home")
        ])
    if params.get("binaries_path") is not None:
        cargs.extend([
            "-binhome",
            params.get("binaries_path")
        ])
    if params.get("dontrun"):
        cargs.append("-dontrun")
    return cargs


def parc_atlas_jackknife_test_outputs(
    params: ParcAtlasJackknifeTestParameters,
    execution: Execution,
) -> ParcAtlasJackknifeTestOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = ParcAtlasJackknifeTestOutputs(
        root=execution.output_file("."),
        jackknife_output=execution.output_file("jackknife/*"),
    )
    return ret


def parc_atlas_jackknife_test_execute(
    params: ParcAtlasJackknifeTestParameters,
    execution: Execution,
) -> ParcAtlasJackknifeTestOutputs:
    """
    Tool for conducting a jackknife accuracy test using FreeSurfer atlases.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `ParcAtlasJackknifeTestOutputs`).
    """
    cargs = parc_atlas_jackknife_test_cargs(params, execution)
    ret = parc_atlas_jackknife_test_outputs(params, execution)
    params = execution.params(params)
    execution.run(cargs)
    return ret


def parc_atlas_jackknife_test(
    register: bool = False,
    reg_dist: str | None = None,
    reg_append: str | None = None,
    reg_copy: str | None = None,
    train: bool = False,
    classify: bool = False,
    test: bool = False,
    all_: bool = False,
    subjects_dir: str | None = None,
    freesurfer_home: str | None = None,
    binaries_path: str | None = None,
    dontrun: bool = False,
    runner: Runner | None = None,
) -> ParcAtlasJackknifeTestOutputs:
    """
    Tool for conducting a jackknife accuracy test using FreeSurfer atlases.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        register: Run mris_register: creates .sphere.reg files.
        reg_dist: Run mris_register with '-dist <arg>' flag.
        reg_append: Append <string> to end of ?h.sphere.reg.
        reg_copy: Copy ?h.sphere.reg<string> ?h.sphere.reg.
        train: Run mris_ca_train: creates .gcs files.
        classify: Run mris_ca_label: creates .annot files.
        test: Run mris_compute_parc_overlap.
        all_: Run train, classify, and test.
        subjects_dir: Override default subjects directory.
        freesurfer_home: Source a new FREESURFER_HOME.
        binaries_path: Specify override path to binaries.
        dontrun: Don't execute the commands.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `ParcAtlasJackknifeTestOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(PARC_ATLAS_JACKKNIFE_TEST_METADATA)
    params = parc_atlas_jackknife_test_params(register=register, reg_dist=reg_dist, reg_append=reg_append, reg_copy=reg_copy, train=train, classify=classify, test=test, all_=all_, subjects_dir=subjects_dir, freesurfer_home=freesurfer_home, binaries_path=binaries_path, dontrun=dontrun)
    return parc_atlas_jackknife_test_execute(params, execution)


__all__ = [
    "PARC_ATLAS_JACKKNIFE_TEST_METADATA",
    "ParcAtlasJackknifeTestOutputs",
    "ParcAtlasJackknifeTestParameters",
    "parc_atlas_jackknife_test",
    "parc_atlas_jackknife_test_params",
]
