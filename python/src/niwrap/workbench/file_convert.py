# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import dataclasses
import pathlib
import typing

FILE_CONVERT_METADATA = Metadata(
    id="01473a5246f8539040c3e81b60f8afa6d07c03ec",
    name="file-convert",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


@dataclasses.dataclass
class FileConvertBorderVersionConvert:
    """
    write a border file with a different version
    """
    border_in: InputPathType
    """the input border file"""
    out_version: int
    """the format version to write as, 1 or 3 (2 doesn't exist)"""
    border_out: str
    """output - the output border file"""
    opt_surface_surface: InputPathType | None = None
    """must be specified if the input is version 1: use this surface file for
    structure and number of vertices, ignore borders on other structures"""
    
    def run(
        self,
        execution: Execution,
    ) -> list[str]:
        """
        Build command line arguments. This method is called by the main command.
        
        Args:
            self: The sub-command object.
            execution: The execution object.
        Returns:
            
        """
        cargs = []
        cargs.append(execution.input_file(self.border_in))
        cargs.append(str(self.out_version))
        cargs.append(self.border_out)
        if self.opt_surface_surface is not None:
            cargs.extend(["-surface", execution.input_file(self.opt_surface_surface)])
        return cargs


@dataclasses.dataclass
class FileConvertNiftiVersionConvert:
    """
    write a nifti file with a different version
    """
    input_: str
    """the input nifti file"""
    version: int
    """the nifti version to write as"""
    output: str
    """output - the output nifti file"""
    
    def run(
        self,
        execution: Execution,
    ) -> list[str]:
        """
        Build command line arguments. This method is called by the main command.
        
        Args:
            self: The sub-command object.
            execution: The execution object.
        Returns:
            
        """
        cargs = []
        cargs.append(self.input_)
        cargs.append(str(self.version))
        cargs.append(self.output)
        return cargs


@dataclasses.dataclass
class FileConvertCiftiVersionConvert:
    """
    write a cifti file with a different version
    """
    cifti_in: InputPathType
    """the input cifti file"""
    version: str
    """the cifti version to write as"""
    cifti_out: str
    """output - the output cifti file"""
    
    def run(
        self,
        execution: Execution,
    ) -> list[str]:
        """
        Build command line arguments. This method is called by the main command.
        
        Args:
            self: The sub-command object.
            execution: The execution object.
        Returns:
            
        """
        cargs = []
        cargs.append(execution.input_file(self.cifti_in))
        cargs.append(self.version)
        cargs.append(self.cifti_out)
        return cargs


class FileConvertOutputs(typing.NamedTuple):
    """
    Output object returned when calling `file_convert(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def file_convert(
    border_version_convert: FileConvertBorderVersionConvert | None = None,
    nifti_version_convert: FileConvertNiftiVersionConvert | None = None,
    cifti_version_convert: FileConvertCiftiVersionConvert | None = None,
    runner: Runner = None,
) -> FileConvertOutputs:
    """
    file-convert by Washington University School of Medicin.
    
    Change version of file format.
    
    You may only specify one top-level option.
    
    Args:
        border_version_convert: write a border file with a different version.
        nifti_version_convert: write a nifti file with a different version.
        cifti_version_convert: write a cifti file with a different version.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FileConvertOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FILE_CONVERT_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-file-convert")
    if border_version_convert is not None:
        cargs.extend(["-border-version-convert", *border_version_convert.run(execution)])
    if nifti_version_convert is not None:
        cargs.extend(["-nifti-version-convert", *nifti_version_convert.run(execution)])
    if cifti_version_convert is not None:
        cargs.extend(["-cifti-version-convert", *cifti_version_convert.run(execution)])
    ret = FileConvertOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "FILE_CONVERT_METADATA",
    "FileConvertBorderVersionConvert",
    "FileConvertCiftiVersionConvert",
    "FileConvertNiftiVersionConvert",
    "FileConvertOutputs",
    "file_convert",
]
