# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

TEST_ORIENTATION_PLANES_FROM_PARCELLATION_METADATA = Metadata(
    id="4ec44f64124a848bb9ff90699fb3e68885365ff6.boutiques",
    name="testOrientationPlanesFromParcellation",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


TestOrientationPlanesFromParcellationParameters = typing.TypedDict('TestOrientationPlanesFromParcellationParameters', {
    "__STYX_TYPE__": typing.Literal["testOrientationPlanesFromParcellation"],
    "input_file": InputPathType,
    "output_file": str,
    "bb_flag": bool,
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
        "testOrientationPlanesFromParcellation": test_orientation_planes_from_parcellation_cargs,
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


class TestOrientationPlanesFromParcellationOutputs(typing.NamedTuple):
    """
    Output object returned when calling `test_orientation_planes_from_parcellation(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def test_orientation_planes_from_parcellation_params(
    input_file: InputPathType,
    output_file: str,
    bb_flag: bool = False,
) -> TestOrientationPlanesFromParcellationParameters:
    """
    Build parameters.
    
    Args:
        input_file: Input file for the parcellation data.
        output_file: Output file for the orientation planes results.
        bb_flag: Flag to use bounding box in the computation.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "testOrientationPlanesFromParcellation",
        "input_file": input_file,
        "output_file": output_file,
        "bb_flag": bb_flag,
    }
    return params


def test_orientation_planes_from_parcellation_cargs(
    params: TestOrientationPlanesFromParcellationParameters,
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
    cargs.append("testOrientationPlanesFromParcellation")
    cargs.extend([
        "-i",
        execution.input_file(params.get("input_file"))
    ])
    cargs.extend([
        "-o",
        params.get("output_file")
    ])
    if params.get("bb_flag"):
        cargs.append("-bb")
    return cargs


def test_orientation_planes_from_parcellation_outputs(
    params: TestOrientationPlanesFromParcellationParameters,
    execution: Execution,
) -> TestOrientationPlanesFromParcellationOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = TestOrientationPlanesFromParcellationOutputs(
        root=execution.output_file("."),
    )
    return ret


def test_orientation_planes_from_parcellation_execute(
    params: TestOrientationPlanesFromParcellationParameters,
    execution: Execution,
) -> TestOrientationPlanesFromParcellationOutputs:
    """
    Tests orientation planes from a given parcellation using FreeSurfer.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `TestOrientationPlanesFromParcellationOutputs`).
    """
    params = execution.params(params)
    cargs = test_orientation_planes_from_parcellation_cargs(params, execution)
    ret = test_orientation_planes_from_parcellation_outputs(params, execution)
    execution.run(cargs)
    return ret


def test_orientation_planes_from_parcellation(
    input_file: InputPathType,
    output_file: str,
    bb_flag: bool = False,
    runner: Runner | None = None,
) -> TestOrientationPlanesFromParcellationOutputs:
    """
    Tests orientation planes from a given parcellation using FreeSurfer.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_file: Input file for the parcellation data.
        output_file: Output file for the orientation planes results.
        bb_flag: Flag to use bounding box in the computation.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `TestOrientationPlanesFromParcellationOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(TEST_ORIENTATION_PLANES_FROM_PARCELLATION_METADATA)
    params = test_orientation_planes_from_parcellation_params(
        input_file=input_file,
        output_file=output_file,
        bb_flag=bb_flag,
    )
    return test_orientation_planes_from_parcellation_execute(params, execution)


__all__ = [
    "TEST_ORIENTATION_PLANES_FROM_PARCELLATION_METADATA",
    "TestOrientationPlanesFromParcellationOutputs",
    "TestOrientationPlanesFromParcellationParameters",
    "test_orientation_planes_from_parcellation",
    "test_orientation_planes_from_parcellation_params",
]
