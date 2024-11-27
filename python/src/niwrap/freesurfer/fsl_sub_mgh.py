# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

FSL_SUB_MGH_METADATA = Metadata(
    id="b225e0584e88c37a1a9ef9c5295eb2118fddc2cc.boutiques",
    name="fsl_sub_mgh",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class FslSubMghOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fsl_sub_mgh(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def fsl_sub_mgh(
    estimated_time: int | None = None,
    queue_name: str | None = "long.q",
    architecture: str | None = None,
    job_priority: int | None = 0,
    email_address: str | None = "root@fmrib.ox.ac.uk",
    hold_job: str | None = None,
    task_file: InputPathType | None = None,
    job_name: str | None = None,
    log_dir: str | None = None,
    mail_options: str | None = None,
    flags_in_scripts: bool = False,
    verbose: bool = False,
    shell_path: str | None = None,
    runner: Runner | None = None,
) -> FslSubMghOutputs:
    """
    Wrapper for job control system such as SGE, modified for compatibility with the
    PBS queueing system.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        estimated_time: Estimated job length in minutes, used to auto-set queue\
            name.
        queue_name: Queue name. Possible values are 'verylong.q', 'long.q' and\
            'short.q'. Default is 'long.q'.
        architecture: Architecture [e.g., darwin or lx24-amd64].
        job_priority: Job priority [0:-1024]. Default is 0.
        email_address: Email address to send notifications. Default is\
            root@fmrib.ox.ac.uk.
        hold_job: Job ID to place a hold on this task until completion.
        task_file: Task file of commands to execute in parallel.
        job_name: Specify job name as it will appear on the queue.
        log_dir: Output directory for log files.
        mail_options: Change the SGE mail options.
        flags_in_scripts: Use flags embedded in scripts to set SGE queuing\
            options.
        verbose: Verbose mode.
        shell_path: Change the PBS shell option.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FslSubMghOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FSL_SUB_MGH_METADATA)
    cargs = []
    cargs.append("fsl_sub_mgh")
    if estimated_time is not None:
        cargs.extend([
            "-T",
            str(estimated_time)
        ])
    if queue_name is not None:
        cargs.extend([
            "-q",
            queue_name
        ])
    if architecture is not None:
        cargs.extend([
            "-a",
            architecture
        ])
    if job_priority is not None:
        cargs.extend([
            "-p",
            str(job_priority)
        ])
    if email_address is not None:
        cargs.extend([
            "-M",
            email_address
        ])
    if hold_job is not None:
        cargs.extend([
            "-j",
            hold_job
        ])
    if task_file is not None:
        cargs.extend([
            "-t",
            execution.input_file(task_file)
        ])
    if job_name is not None:
        cargs.extend([
            "-N",
            job_name
        ])
    if log_dir is not None:
        cargs.extend([
            "-l",
            log_dir
        ])
    if mail_options is not None:
        cargs.extend([
            "-m",
            mail_options
        ])
    if flags_in_scripts:
        cargs.append("-F")
    if verbose:
        cargs.append("-v")
    if shell_path is not None:
        cargs.extend([
            "-s",
            shell_path
        ])
    cargs.append("<COMMAND>")
    ret = FslSubMghOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "FSL_SUB_MGH_METADATA",
    "FslSubMghOutputs",
    "fsl_sub_mgh",
]
