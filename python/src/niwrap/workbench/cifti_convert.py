# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

CIFTI_CONVERT_METADATA = Metadata(
    id="f620818fd4e7449f16b3a3864a16b31df547c1e9.boutiques",
    name="cifti-convert",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)


@dataclasses.dataclass
class CiftiConvertToGiftiExt:
    """
    convert to GIFTI external binary.
    """
    cifti_in: InputPathType
    """the input cifti file"""
    gifti_out: str
    """output - the output gifti file"""
    
    def run(
        self,
        execution: Execution,
    ) -> list[str]:
        """
        Build command line arguments. This method is called by the main command.
        
        Args:
            execution: The execution object.
        Returns:
            Command line arguments
        """
        cargs = []
        cargs.append("-to-gifti-ext")
        cargs.append(execution.input_file(self.cifti_in))
        cargs.append(self.gifti_out)
        return cargs


@dataclasses.dataclass
class CiftiConvertResetTimepoints:
    """
    reset the mapping along rows to timepoints, taking length from the gifti
    file.
    """
    timestep: float
    """the desired time between frames"""
    timestart: float
    """the desired time offset of the initial frame"""
    opt_unit_unit: str | None = None
    """use a unit other than time: unit identifier (default SECOND)"""
    
    def run(
        self,
        execution: Execution,
    ) -> list[str]:
        """
        Build command line arguments. This method is called by the main command.
        
        Args:
            execution: The execution object.
        Returns:
            Command line arguments
        """
        cargs = []
        cargs.append("-reset-timepoints")
        cargs.append(str(self.timestep))
        cargs.append(str(self.timestart))
        if self.opt_unit_unit is not None:
            cargs.extend([
                "-unit",
                self.opt_unit_unit
            ])
        return cargs


@dataclasses.dataclass
class CiftiConvertReplaceBinary:
    """
    replace data with a binary file.
    """
    binary_in: str
    """the binary file that contains replacement data"""
    opt_flip_endian: bool = False
    """byteswap the binary file"""
    opt_transpose: bool = False
    """transpose the binary file"""
    
    def run(
        self,
        execution: Execution,
    ) -> list[str]:
        """
        Build command line arguments. This method is called by the main command.
        
        Args:
            execution: The execution object.
        Returns:
            Command line arguments
        """
        cargs = []
        cargs.append("-replace-binary")
        cargs.append(self.binary_in)
        if self.opt_flip_endian:
            cargs.append("-flip-endian")
        if self.opt_transpose:
            cargs.append("-transpose")
        return cargs


class CiftiConvertFromGiftiExtOutputs(typing.NamedTuple):
    """
    Output object returned when calling `CiftiConvertFromGiftiExt | None(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    cifti_out: OutputPathType
    """the output cifti file"""


@dataclasses.dataclass
class CiftiConvertFromGiftiExt:
    """
    convert a GIFTI made with this command back into a CIFTI.
    """
    gifti_in: str
    """the input gifti file"""
    cifti_out: str
    """the output cifti file"""
    reset_timepoints: CiftiConvertResetTimepoints | None = None
    """reset the mapping along rows to timepoints, taking length from the gifti
    file"""
    opt_reset_scalars: bool = False
    """reset mapping along rows to scalars, taking length from the gifti file"""
    opt_column_reset_scalars: bool = False
    """reset mapping along columns to scalar (useful for changing number of
    series in a sdseries file)"""
    replace_binary: CiftiConvertReplaceBinary | None = None
    """replace data with a binary file"""
    
    def run(
        self,
        execution: Execution,
    ) -> list[str]:
        """
        Build command line arguments. This method is called by the main command.
        
        Args:
            execution: The execution object.
        Returns:
            Command line arguments
        """
        cargs = []
        cargs.append("-from-gifti-ext")
        cargs.append(self.gifti_in)
        cargs.append(self.cifti_out)
        if self.reset_timepoints is not None:
            cargs.extend(self.reset_timepoints.run(execution))
        if self.opt_reset_scalars:
            cargs.append("-reset-scalars")
        if self.opt_column_reset_scalars:
            cargs.append("-column-reset-scalars")
        if self.replace_binary is not None:
            cargs.extend(self.replace_binary.run(execution))
        return cargs
    
    def outputs(
        self,
        execution: Execution,
    ) -> CiftiConvertFromGiftiExtOutputs:
        """
        Collect output file paths.
        
        Args:
            execution: The execution object.
        Returns:
            NamedTuple of outputs (described in `CiftiConvertFromGiftiExtOutputs`).
        """
        ret = CiftiConvertFromGiftiExtOutputs(
            root=execution.output_file("."),
            cifti_out=execution.output_file(self.cifti_out),
        )
        return ret


class CiftiConvertToNiftiOutputs(typing.NamedTuple):
    """
    Output object returned when calling `CiftiConvertToNifti | None(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    nifti_out: OutputPathType
    """the output nifti file"""


@dataclasses.dataclass
class CiftiConvertToNifti:
    """
    convert to NIFTI1.
    """
    cifti_in: InputPathType
    """the input cifti file"""
    nifti_out: str
    """the output nifti file"""
    opt_smaller_file: bool = False
    """use better-fitting dimension lengths"""
    opt_smaller_dims: bool = False
    """minimize the largest dimension, for tools that don't like large
    indices"""
    
    def run(
        self,
        execution: Execution,
    ) -> list[str]:
        """
        Build command line arguments. This method is called by the main command.
        
        Args:
            execution: The execution object.
        Returns:
            Command line arguments
        """
        cargs = []
        cargs.append("-to-nifti")
        cargs.append(execution.input_file(self.cifti_in))
        cargs.append(self.nifti_out)
        if self.opt_smaller_file:
            cargs.append("-smaller-file")
        if self.opt_smaller_dims:
            cargs.append("-smaller-dims")
        return cargs
    
    def outputs(
        self,
        execution: Execution,
    ) -> CiftiConvertToNiftiOutputs:
        """
        Collect output file paths.
        
        Args:
            execution: The execution object.
        Returns:
            NamedTuple of outputs (described in `CiftiConvertToNiftiOutputs`).
        """
        ret = CiftiConvertToNiftiOutputs(
            root=execution.output_file("."),
            nifti_out=execution.output_file(self.nifti_out),
        )
        return ret


@dataclasses.dataclass
class CiftiConvertResetTimepoints_:
    """
    reset the mapping along rows to timepoints, taking length from the nifti
    file.
    """
    timestep: float
    """the desired time between frames"""
    timestart: float
    """the desired time offset of the initial frame"""
    opt_unit_unit: str | None = None
    """use a unit other than time: unit identifier (default SECOND)"""
    
    def run(
        self,
        execution: Execution,
    ) -> list[str]:
        """
        Build command line arguments. This method is called by the main command.
        
        Args:
            execution: The execution object.
        Returns:
            Command line arguments
        """
        cargs = []
        cargs.append("-reset-timepoints")
        cargs.append(str(self.timestep))
        cargs.append(str(self.timestart))
        if self.opt_unit_unit is not None:
            cargs.extend([
                "-unit",
                self.opt_unit_unit
            ])
        return cargs


class CiftiConvertFromNiftiOutputs(typing.NamedTuple):
    """
    Output object returned when calling `CiftiConvertFromNifti | None(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    cifti_out: OutputPathType
    """the output cifti file"""


@dataclasses.dataclass
class CiftiConvertFromNifti:
    """
    convert a NIFTI (1 or 2) file made with this command back into CIFTI.
    """
    nifti_in: InputPathType
    """the input nifti file"""
    cifti_template: InputPathType
    """a cifti file with the dimension(s) and mapping(s) that should be used"""
    cifti_out: str
    """the output cifti file"""
    reset_timepoints: CiftiConvertResetTimepoints_ | None = None
    """reset the mapping along rows to timepoints, taking length from the nifti
    file"""
    opt_reset_scalars: bool = False
    """reset mapping along rows to scalars, taking length from the nifti file"""
    
    def run(
        self,
        execution: Execution,
    ) -> list[str]:
        """
        Build command line arguments. This method is called by the main command.
        
        Args:
            execution: The execution object.
        Returns:
            Command line arguments
        """
        cargs = []
        cargs.append("-from-nifti")
        cargs.append(execution.input_file(self.nifti_in))
        cargs.append(execution.input_file(self.cifti_template))
        cargs.append(self.cifti_out)
        if self.reset_timepoints is not None:
            cargs.extend(self.reset_timepoints.run(execution))
        if self.opt_reset_scalars:
            cargs.append("-reset-scalars")
        return cargs
    
    def outputs(
        self,
        execution: Execution,
    ) -> CiftiConvertFromNiftiOutputs:
        """
        Collect output file paths.
        
        Args:
            execution: The execution object.
        Returns:
            NamedTuple of outputs (described in `CiftiConvertFromNiftiOutputs`).
        """
        ret = CiftiConvertFromNiftiOutputs(
            root=execution.output_file("."),
            cifti_out=execution.output_file(self.cifti_out),
        )
        return ret


@dataclasses.dataclass
class CiftiConvertToText:
    """
    convert to a plain text file.
    """
    cifti_in: InputPathType
    """the input cifti file"""
    text_out: str
    """output - the output text file"""
    opt_col_delim_delim_string: str | None = None
    """choose string to put between elements in a row: the string to use
    (default is a tab character)"""
    
    def run(
        self,
        execution: Execution,
    ) -> list[str]:
        """
        Build command line arguments. This method is called by the main command.
        
        Args:
            execution: The execution object.
        Returns:
            Command line arguments
        """
        cargs = []
        cargs.append("-to-text")
        cargs.append(execution.input_file(self.cifti_in))
        cargs.append(self.text_out)
        if self.opt_col_delim_delim_string is not None:
            cargs.extend([
                "-col-delim",
                self.opt_col_delim_delim_string
            ])
        return cargs


@dataclasses.dataclass
class CiftiConvertResetTimepoints_2:
    """
    reset the mapping along rows to timepoints, taking length from the text
    file.
    """
    timestep: float
    """the desired time between frames"""
    timestart: float
    """the desired time offset of the initial frame"""
    opt_unit_unit: str | None = None
    """use a unit other than time: unit identifier (default SECOND)"""
    
    def run(
        self,
        execution: Execution,
    ) -> list[str]:
        """
        Build command line arguments. This method is called by the main command.
        
        Args:
            execution: The execution object.
        Returns:
            Command line arguments
        """
        cargs = []
        cargs.append("-reset-timepoints")
        cargs.append(str(self.timestep))
        cargs.append(str(self.timestart))
        if self.opt_unit_unit is not None:
            cargs.extend([
                "-unit",
                self.opt_unit_unit
            ])
        return cargs


class CiftiConvertFromTextOutputs(typing.NamedTuple):
    """
    Output object returned when calling `CiftiConvertFromText | None(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    cifti_out: OutputPathType
    """the output cifti file"""


@dataclasses.dataclass
class CiftiConvertFromText:
    """
    convert from plain text to cifti.
    """
    text_in: str
    """the input text file"""
    cifti_template: InputPathType
    """a cifti file with the dimension(s) and mapping(s) that should be used"""
    cifti_out: str
    """the output cifti file"""
    opt_col_delim_delim_string: str | None = None
    """specify string that is between elements in a row: the string to use
    (default is any whitespace)"""
    reset_timepoints: CiftiConvertResetTimepoints_2 | None = None
    """reset the mapping along rows to timepoints, taking length from the text
    file"""
    opt_reset_scalars: bool = False
    """reset mapping along rows to scalars, taking length from the text file"""
    
    def run(
        self,
        execution: Execution,
    ) -> list[str]:
        """
        Build command line arguments. This method is called by the main command.
        
        Args:
            execution: The execution object.
        Returns:
            Command line arguments
        """
        cargs = []
        cargs.append("-from-text")
        cargs.append(self.text_in)
        cargs.append(execution.input_file(self.cifti_template))
        cargs.append(self.cifti_out)
        if self.opt_col_delim_delim_string is not None:
            cargs.extend([
                "-col-delim",
                self.opt_col_delim_delim_string
            ])
        if self.reset_timepoints is not None:
            cargs.extend(self.reset_timepoints.run(execution))
        if self.opt_reset_scalars:
            cargs.append("-reset-scalars")
        return cargs
    
    def outputs(
        self,
        execution: Execution,
    ) -> CiftiConvertFromTextOutputs:
        """
        Collect output file paths.
        
        Args:
            execution: The execution object.
        Returns:
            NamedTuple of outputs (described in `CiftiConvertFromTextOutputs`).
        """
        ret = CiftiConvertFromTextOutputs(
            root=execution.output_file("."),
            cifti_out=execution.output_file(self.cifti_out),
        )
        return ret


class CiftiConvertOutputs(typing.NamedTuple):
    """
    Output object returned when calling `cifti_convert(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    from_gifti_ext: CiftiConvertFromGiftiExtOutputs | None
    """Outputs from `CiftiConvertFromGiftiExt`."""
    to_nifti: CiftiConvertToNiftiOutputs | None
    """Outputs from `CiftiConvertToNifti`."""
    from_nifti: CiftiConvertFromNiftiOutputs | None
    """Outputs from `CiftiConvertFromNifti`."""
    from_text: CiftiConvertFromTextOutputs | None
    """Outputs from `CiftiConvertFromText`."""


def cifti_convert(
    to_gifti_ext: CiftiConvertToGiftiExt | None = None,
    from_gifti_ext: CiftiConvertFromGiftiExt | None = None,
    to_nifti: CiftiConvertToNifti | None = None,
    from_nifti: CiftiConvertFromNifti | None = None,
    to_text: CiftiConvertToText | None = None,
    from_text: CiftiConvertFromText | None = None,
    runner: Runner | None = None,
) -> CiftiConvertOutputs:
    """
    Dump cifti matrix into other formats.
    
    This command is used to convert a full CIFTI matrix to/from formats that can
    be used by programs that don't understand CIFTI. You must specify exactly
    one of -to-gifti-ext, -from-gifti-ext, -to-nifti, -from-nifti, -to-text, or
    -from-text.
    
    If you want to write an existing CIFTI file with a different CIFTI version,
    see -file-convert, and its -cifti-version-convert option.
    
    If you want part of the CIFTI file as a metric, label, or volume file, see
    -cifti-separate. If you want to create a CIFTI file from metric and/or
    volume files, see the -cifti-create-* commands.
    
    If you want to import a matrix that is restricted to an ROI, first create a
    template CIFTI file matching that ROI using a -cifti-create-* command. After
    importing to CIFTI, you can then expand the file into a standard
    brainordinates space with -cifti-create-dense-from-template. If you want to
    export only part of a CIFTI file, first create an roi-restricted CIFTI file
    with -cifti-restrict-dense-mapping.
    
    The -transpose option to -from-gifti-ext is needed if the replacement binary
    file is in column-major order.
    
    The -unit options accept these values:
    
    SECOND
    HERTZ
    METER
    RADIAN.
    
    Author: Washington University School of Medicin
    
    Args:
        to_gifti_ext: convert to GIFTI external binary.
        from_gifti_ext: convert a GIFTI made with this command back into a\
            CIFTI.
        to_nifti: convert to NIFTI1.
        from_nifti: convert a NIFTI (1 or 2) file made with this command back\
            into CIFTI.
        to_text: convert to a plain text file.
        from_text: convert from plain text to cifti.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `CiftiConvertOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(CIFTI_CONVERT_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-cifti-convert")
    if to_gifti_ext is not None:
        cargs.extend(to_gifti_ext.run(execution))
    if from_gifti_ext is not None:
        cargs.extend(from_gifti_ext.run(execution))
    if to_nifti is not None:
        cargs.extend(to_nifti.run(execution))
    if from_nifti is not None:
        cargs.extend(from_nifti.run(execution))
    if to_text is not None:
        cargs.extend(to_text.run(execution))
    if from_text is not None:
        cargs.extend(from_text.run(execution))
    ret = CiftiConvertOutputs(
        root=execution.output_file("."),
        from_gifti_ext=from_gifti_ext.outputs(execution) if from_gifti_ext else None,
        to_nifti=to_nifti.outputs(execution) if to_nifti else None,
        from_nifti=from_nifti.outputs(execution) if from_nifti else None,
        from_text=from_text.outputs(execution) if from_text else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "CIFTI_CONVERT_METADATA",
    "CiftiConvertFromGiftiExt",
    "CiftiConvertFromGiftiExtOutputs",
    "CiftiConvertFromNifti",
    "CiftiConvertFromNiftiOutputs",
    "CiftiConvertFromText",
    "CiftiConvertFromTextOutputs",
    "CiftiConvertOutputs",
    "CiftiConvertReplaceBinary",
    "CiftiConvertResetTimepoints",
    "CiftiConvertResetTimepoints_",
    "CiftiConvertResetTimepoints_2",
    "CiftiConvertToGiftiExt",
    "CiftiConvertToNifti",
    "CiftiConvertToNiftiOutputs",
    "CiftiConvertToText",
    "cifti_convert",
]
