# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

V_3D_EIGS_TO_DT_METADATA = Metadata(
    id="98b84d719a888cbd2dac99e875b46da6e2d809e9",
    name="3dEigsToDT",
    container_image_type="docker",
    container_image_index="index.docker.io",
    container_image_tag="afni/afni:latest",
)


class V3dEigsToDtOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_eigs_to_dt(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    dt_brik_output: OutputPathType
    """Output diffusion tensor (DT) file in AFNI format (BRIK)"""
    dt_head_output: OutputPathType
    """Output diffusion tensor (DT) file in AFNI format (HEAD)"""


def v_3d_eigs_to_dt(
    eig_vals: str,
    eig_vecs: str,
    prefix: str,
    mask: InputPathType | None = None,
    flip_x: bool = False,
    flip_y: bool = False,
    flip_z: bool = False,
    scale_eigs: float | int | None = None,
    runner: Runner | None = None,
) -> V3dEigsToDtOutputs:
    """
    3dEigsToDT by Taylor PA, Saad ZS.
    
    Convert set of DTI eigenvectors and eigenvalues to a diffusion tensor, with
    optional value-scaling and vector-flipping.
    
    More information:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/3dEigsToDT.html
    
    Args:
        eig_vals: Searchable descriptor for finding all three required\
            eigenvalue files. It should list all three eigenvalue files in\
            descending order of magnitude.
        eig_vecs: Searchable descriptor for finding all three required\
            eigenvector files. It should list all three eigenvector files in order\
            matching the eigenvalue files.
        prefix: Prefix for the output file name. It is recommended to include a\
            'DT' label in it.
        mask: Optional mask within which to calculate uncertainty. If not\
            provided, the data should be masked already.
        flip_x: Change sign of the first element of eigenvectors.
        flip_y: Change sign of the second element of eigenvectors.
        flip_z: Change sign of the third element of eigenvectors.
        scale_eigs: Rescale the eigenvalues by dividing by a number X > 0.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dEigsToDtOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_EIGS_TO_DT_METADATA)
    cargs = []
    cargs.append("3dEigsToDT")
    cargs.append("-eig_vals")
    cargs.append(eig_vals)
    cargs.append("-eig_vecs")
    cargs.append(eig_vecs)
    cargs.append("-prefix")
    cargs.append(prefix)
    if mask is not None:
        cargs.extend(["-mask", execution.input_file(mask)])
    if flip_x:
        cargs.append("-flip_x")
    if flip_y:
        cargs.append("-flip_y")
    if flip_z:
        cargs.append("-flip_z")
    if scale_eigs is not None:
        cargs.extend(["-scale_eigs", str(scale_eigs)])
    ret = V3dEigsToDtOutputs(
        root=execution.output_file("."),
        dt_brik_output=execution.output_file(f"{prefix}_DT+orig.BRIK"),
        dt_head_output=execution.output_file(f"{prefix}_DT+orig.HEAD"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dEigsToDtOutputs",
    "V_3D_EIGS_TO_DT_METADATA",
    "v_3d_eigs_to_dt",
]
