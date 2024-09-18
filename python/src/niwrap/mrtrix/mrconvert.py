# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRCONVERT_METADATA = Metadata(
    id="852b1bbfb4bbbdaacefbe39fd16e3b09b7b9dd6c.boutiques",
    name="mrconvert",
    package="mrtrix",
    container_image_tag="mrtrix3/mrtrix3:3.0.4",
)


@dataclasses.dataclass
class MrconvertCoord:
    """
    retain data from the input image only at the coordinates specified in the
    selection along the specified axis. The selection argument expects a number
    sequence, which can also include the 'end' keyword.
    """
    axis: int
    """retain data from the input image only at the coordinates specified in the
    selection along the specified axis. The selection argument expects a number
    sequence, which can also include the 'end' keyword."""
    selection: list[int]
    """retain data from the input image only at the coordinates specified in the
    selection along the specified axis. The selection argument expects a number
    sequence, which can also include the 'end' keyword."""
    
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
        cargs.append("-coord")
        cargs.append(str(self.axis))
        cargs.extend(map(str, self.selection))
        return cargs


@dataclasses.dataclass
class MrconvertClearProperty:
    """
    remove the specified key from the image header altogether.
    """
    key: str
    """remove the specified key from the image header altogether."""
    
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
        cargs.append("-clear_property")
        cargs.append(self.key)
        return cargs


@dataclasses.dataclass
class MrconvertSetProperty:
    """
    set the value of the specified key in the image header.
    """
    key: str
    """set the value of the specified key in the image header."""
    value: str
    """set the value of the specified key in the image header."""
    
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
        cargs.append("-set_property")
        cargs.append(self.key)
        cargs.append(self.value)
        return cargs


@dataclasses.dataclass
class MrconvertAppendProperty:
    """
    append the given value to the specified key in the image header (this adds
    the value specified as a new line in the header value).
    """
    key: str
    """append the given value to the specified key in the image header (this
    adds the value specified as a new line in the header value)."""
    value: str
    """append the given value to the specified key in the image header (this
    adds the value specified as a new line in the header value)."""
    
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
        cargs.append("-append_property")
        cargs.append(self.key)
        cargs.append(self.value)
        return cargs


@dataclasses.dataclass
class MrconvertVariousString:
    obj: str
    """String object."""
    
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
        cargs.append(self.obj)
        return cargs


@dataclasses.dataclass
class MrconvertVariousFile:
    obj: InputPathType
    """File object."""
    
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
        cargs.append(execution.input_file(self.obj))
        return cargs


@dataclasses.dataclass
class MrconvertVariousString_:
    obj: str
    """String object."""
    
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
        cargs.append(self.obj)
        return cargs


@dataclasses.dataclass
class MrconvertVariousFile_:
    obj: InputPathType
    """File object."""
    
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
        cargs.append(execution.input_file(self.obj))
        return cargs


@dataclasses.dataclass
class MrconvertFslgrad:
    """
    Provide the diffusion-weighted gradient scheme used in the acquisition in
    FSL bvecs/bvals format files. If a diffusion gradient scheme is present in
    the input image header, the data provided with this option will be instead
    used.
    """
    bvecs: InputPathType
    """Provide the diffusion-weighted gradient scheme used in the acquisition in
    FSL bvecs/bvals format files. If a diffusion gradient scheme is present in
    the input image header, the data provided with this option will be instead
    used."""
    bvals: InputPathType
    """Provide the diffusion-weighted gradient scheme used in the acquisition in
    FSL bvecs/bvals format files. If a diffusion gradient scheme is present in
    the input image header, the data provided with this option will be instead
    used."""
    
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
        cargs.append("-fslgrad")
        cargs.append(execution.input_file(self.bvecs))
        cargs.append(execution.input_file(self.bvals))
        return cargs


class MrconvertExportGradFslOutputs(typing.NamedTuple):
    """
    Output object returned when calling `MrconvertExportGradFsl | None(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    bvecs_path: OutputPathType
    """export the diffusion-weighted gradient table to files in FSL (bvecs /
    bvals) format"""
    bvals_path: OutputPathType
    """export the diffusion-weighted gradient table to files in FSL (bvecs /
    bvals) format"""


@dataclasses.dataclass
class MrconvertExportGradFsl:
    """
    export the diffusion-weighted gradient table to files in FSL (bvecs / bvals)
    format.
    """
    bvecs_path: str
    """export the diffusion-weighted gradient table to files in FSL (bvecs /
    bvals) format"""
    bvals_path: str
    """export the diffusion-weighted gradient table to files in FSL (bvecs /
    bvals) format"""
    
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
        cargs.append("-export_grad_fsl")
        cargs.append(self.bvecs_path)
        cargs.append(self.bvals_path)
        return cargs
    
    def outputs(
        self,
        execution: Execution,
    ) -> MrconvertExportGradFslOutputs:
        """
        Collect output file paths.
        
        Args:
            execution: The execution object.
        Returns:
            NamedTuple of outputs (described in `MrconvertExportGradFslOutputs`).
        """
        ret = MrconvertExportGradFslOutputs(
            root=execution.output_file("."),
            bvecs_path=execution.output_file(self.bvecs_path),
            bvals_path=execution.output_file(self.bvals_path),
        )
        return ret


@dataclasses.dataclass
class MrconvertImportPeEddy:
    """
    import phase-encoding information from an EDDY-style config / index file
    pair.
    """
    config: InputPathType
    """import phase-encoding information from an EDDY-style config / index file
    pair"""
    indices: InputPathType
    """import phase-encoding information from an EDDY-style config / index file
    pair"""
    
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
        cargs.append("-import_pe_eddy")
        cargs.append(execution.input_file(self.config))
        cargs.append(execution.input_file(self.indices))
        return cargs


class MrconvertExportPeEddyOutputs(typing.NamedTuple):
    """
    Output object returned when calling `MrconvertExportPeEddy | None(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    config: OutputPathType
    """export phase-encoding information to an EDDY-style config / index file
    pair"""
    indices: OutputPathType
    """export phase-encoding information to an EDDY-style config / index file
    pair"""


@dataclasses.dataclass
class MrconvertExportPeEddy:
    """
    export phase-encoding information to an EDDY-style config / index file pair.
    """
    config: str
    """export phase-encoding information to an EDDY-style config / index file
    pair"""
    indices: str
    """export phase-encoding information to an EDDY-style config / index file
    pair"""
    
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
        cargs.append("-export_pe_eddy")
        cargs.append(self.config)
        cargs.append(self.indices)
        return cargs
    
    def outputs(
        self,
        execution: Execution,
    ) -> MrconvertExportPeEddyOutputs:
        """
        Collect output file paths.
        
        Args:
            execution: The execution object.
        Returns:
            NamedTuple of outputs (described in `MrconvertExportPeEddyOutputs`).
        """
        ret = MrconvertExportPeEddyOutputs(
            root=execution.output_file("."),
            config=execution.output_file(self.config),
            indices=execution.output_file(self.indices),
        )
        return ret


@dataclasses.dataclass
class MrconvertConfig:
    """
    temporarily set the value of an MRtrix config file entry.
    """
    key: str
    """temporarily set the value of an MRtrix config file entry."""
    value: str
    """temporarily set the value of an MRtrix config file entry."""
    
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
        cargs.append("-config")
        cargs.append(self.key)
        cargs.append(self.value)
        return cargs


class MrconvertOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mrconvert(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output: OutputPathType
    """the output image."""
    json_export: OutputPathType | None
    """export data from an image header key-value pairs into a JSON file """
    export_grad_mrtrix: OutputPathType | None
    """export the diffusion-weighted gradient table to file in MRtrix format """
    export_pe_table: OutputPathType | None
    """export phase-encoding table to file """
    export_grad_fsl: MrconvertExportGradFslOutputs | None
    """Outputs from `MrconvertExportGradFsl`."""
    export_pe_eddy: MrconvertExportPeEddyOutputs | None
    """Outputs from `MrconvertExportPeEddy`."""


def mrconvert(
    input_: InputPathType,
    output: str,
    coord: list[MrconvertCoord] | None = None,
    vox: list[float] | None = None,
    axes: list[int] | None = None,
    scaling: list[float] | None = None,
    json_import: InputPathType | None = None,
    json_export: str | None = None,
    clear_property: list[MrconvertClearProperty] | None = None,
    set_property: list[MrconvertSetProperty] | None = None,
    append_property: list[MrconvertAppendProperty] | None = None,
    copy_properties: typing.Union[MrconvertVariousString, MrconvertVariousFile] | None = None,
    strides: typing.Union[MrconvertVariousString_, MrconvertVariousFile_] | None = None,
    datatype: str | None = None,
    grad: InputPathType | None = None,
    fslgrad: MrconvertFslgrad | None = None,
    bvalue_scaling: str | None = None,
    export_grad_mrtrix: str | None = None,
    export_grad_fsl: MrconvertExportGradFsl | None = None,
    import_pe_table: InputPathType | None = None,
    import_pe_eddy: MrconvertImportPeEddy | None = None,
    export_pe_table: str | None = None,
    export_pe_eddy: MrconvertExportPeEddy | None = None,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[MrconvertConfig] | None = None,
    help_: bool = False,
    version: bool = False,
    runner: Runner | None = None,
) -> MrconvertOutputs:
    """
    Perform conversion between different file types and optionally extract a subset
    of the input image.
    
    If used correctly, this program can be a very useful workhorse. In addition
    to converting images between different formats, it can be used to extract
    specific studies from a data set, extract a specific region of interest, or
    flip the images. Some of the possible operations are described in more
    detail below.
    
    Note that for both the -coord and -axes options, indexing starts from 0
    rather than 1. E.g. -coord 3 <#> selects volumes (the fourth dimension) from
    the series; -axes 0,1,2 includes only the three spatial axes in the output
    image.
    
    Additionally, for the second input to the -coord option and the -axes
    option, you can use any valid number sequence in the selection, as well as
    the 'end' keyword (see the main documentation for details); this can be
    particularly useful to select multiple coordinates.
    
    The -vox option is used to change the size of the voxels in the output image
    as reported in the image header; note however that this does not re-sample
    the image based on a new voxel size (that is done using the mrgrid command).
    
    By default, the intensity scaling parameters in the input image header are
    passed through to the output image header when writing to an integer image,
    and reset to 0,1 (i.e. no scaling) for floating-point and binary images.
    Note that the -scaling option will therefore have no effect for
    floating-point or binary output images.
    
    The -axes option specifies which axes from the input image will be used to
    form the output image. This allows the permutation, omission, or addition of
    axes into the output image. The axes should be supplied as a comma-separated
    list of axis indices. If an axis from the input image is to be omitted from
    the output image, it must either already have a size of 1, or a single
    coordinate along that axis must be selected by the user by using the -coord
    option. Examples are provided further below.
    
    The -bvalue_scaling option controls an aspect of the import of diffusion
    gradient tables. When the input diffusion-weighting direction vectors have
    norms that differ substantially from unity, the b-values will be scaled by
    the square of their corresponding vector norm (this is how multi-shell
    acquisitions are frequently achieved on scanner platforms). However in some
    rare instances, the b-values may be correct, despite the vectors not being
    of unit norm (or conversely, the b-values may need to be rescaled even
    though the vectors are close to unit norm). This option allows the user to
    control this operation and override MRrtix3's automatic detection.
    
    References:
    
    .
    
    Author: J-Donald Tournier (jdtournier@gmail.com) and Robert E. Smith
    (robert.smith@florey.edu.au)
    
    URL:
    https://mrtrix.readthedocs.io/en/latest/reference/commands/mrconvert.html
    
    Args:
        input_: the input image.
        output: the output image.
        coord: retain data from the input image only at the coordinates\
            specified in the selection along the specified axis. The selection\
            argument expects a number sequence, which can also include the 'end'\
            keyword.
        vox: change the voxel dimensions reported in the output image header.
        axes: specify the axes from the input image that will be used to form\
            the output image.
        scaling: specify the data scaling parameters used to rescale the\
            intensity values.
        json_import: import data from a JSON file into header key-value pairs.
        json_export: export data from an image header key-value pairs into a\
            JSON file.
        clear_property: remove the specified key from the image header\
            altogether.
        set_property: set the value of the specified key in the image header.
        append_property: append the given value to the specified key in the\
            image header (this adds the value specified as a new line in the header\
            value).
        copy_properties: clear all generic properties and replace with the\
            properties from the image / file specified.
        strides: specify the strides of the output data in memory; either as a\
            comma-separated list of (signed) integers, or as a template image from\
            which the strides shall be extracted and used. The actual strides\
            produced will depend on whether the output image format can support it.
        datatype: specify output image data type. Valid choices are: float32,\
            float32le, float32be, float64, float64le, float64be, int64, uint64,\
            int64le, uint64le, int64be, uint64be, int32, uint32, int32le, uint32le,\
            int32be, uint32be, int16, uint16, int16le, uint16le, int16be, uint16be,\
            cfloat32, cfloat32le, cfloat32be, cfloat64, cfloat64le, cfloat64be,\
            int8, uint8, bit.
        grad: Provide the diffusion-weighted gradient scheme used in the\
            acquisition in a text file. This should be supplied as a 4xN text file\
            with each line is in the format [ X Y Z b ], where [ X Y Z ] describe\
            the direction of the applied gradient, and b gives the b-value in units\
            of s/mm^2. If a diffusion gradient scheme is present in the input image\
            header, the data provided with this option will be instead used.
        fslgrad: Provide the diffusion-weighted gradient scheme used in the\
            acquisition in FSL bvecs/bvals format files. If a diffusion gradient\
            scheme is present in the input image header, the data provided with\
            this option will be instead used.
        bvalue_scaling: enable or disable scaling of diffusion b-values by the\
            square of the corresponding DW gradient norm (see Desciption). Valid\
            choices are yes/no, true/false, 0/1 (default: automatic).
        export_grad_mrtrix: export the diffusion-weighted gradient table to\
            file in MRtrix format.
        export_grad_fsl: export the diffusion-weighted gradient table to files\
            in FSL (bvecs / bvals) format.
        import_pe_table: import a phase-encoding table from file.
        import_pe_eddy: import phase-encoding information from an EDDY-style\
            config / index file pair.
        export_pe_table: export phase-encoding table to file.
        export_pe_eddy: export phase-encoding information to an EDDY-style\
            config / index file pair.
        info: display information messages.
        quiet: do not display information messages or progress status;\
            alternatively, this can be achieved by setting the MRTRIX_QUIET\
            environment variable to a non-empty string.
        debug: display debugging messages.
        force: force overwrite of output files (caution: using the same file as\
            input and output might cause unexpected behaviour).
        nthreads: use this number of threads in multi-threaded applications\
            (set to 0 to disable multi-threading).
        config: temporarily set the value of an MRtrix config file entry.
        help_: display this information page and exit.
        version: display version information and exit.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MrconvertOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRCONVERT_METADATA)
    cargs = []
    cargs.append("mrconvert")
    if coord is not None:
        cargs.extend([a for c in [s.run(execution) for s in coord] for a in c])
    if vox is not None:
        cargs.extend([
            "-vox",
            *map(str, vox)
        ])
    if axes is not None:
        cargs.extend([
            "-axes",
            *map(str, axes)
        ])
    if scaling is not None:
        cargs.extend([
            "-scaling",
            *map(str, scaling)
        ])
    if json_import is not None:
        cargs.extend([
            "-json_import",
            execution.input_file(json_import)
        ])
    if json_export is not None:
        cargs.extend([
            "-json_export",
            json_export
        ])
    if clear_property is not None:
        cargs.extend([a for c in [s.run(execution) for s in clear_property] for a in c])
    if set_property is not None:
        cargs.extend([a for c in [s.run(execution) for s in set_property] for a in c])
    if append_property is not None:
        cargs.extend([a for c in [s.run(execution) for s in append_property] for a in c])
    if copy_properties is not None:
        cargs.extend([
            "-copy_properties",
            *copy_properties.run(execution)
        ])
    if strides is not None:
        cargs.extend([
            "-strides",
            *strides.run(execution)
        ])
    if datatype is not None:
        cargs.extend([
            "-datatype",
            datatype
        ])
    if grad is not None:
        cargs.extend([
            "-grad",
            execution.input_file(grad)
        ])
    if fslgrad is not None:
        cargs.extend(fslgrad.run(execution))
    if bvalue_scaling is not None:
        cargs.extend([
            "-bvalue_scaling",
            bvalue_scaling
        ])
    if export_grad_mrtrix is not None:
        cargs.extend([
            "-export_grad_mrtrix",
            export_grad_mrtrix
        ])
    if export_grad_fsl is not None:
        cargs.extend(export_grad_fsl.run(execution))
    if import_pe_table is not None:
        cargs.extend([
            "-import_pe_table",
            execution.input_file(import_pe_table)
        ])
    if import_pe_eddy is not None:
        cargs.extend(import_pe_eddy.run(execution))
    if export_pe_table is not None:
        cargs.extend([
            "-export_pe_table",
            export_pe_table
        ])
    if export_pe_eddy is not None:
        cargs.extend(export_pe_eddy.run(execution))
    if info:
        cargs.append("-info")
    if quiet:
        cargs.append("-quiet")
    if debug:
        cargs.append("-debug")
    if force:
        cargs.append("-force")
    if nthreads is not None:
        cargs.extend([
            "-nthreads",
            str(nthreads)
        ])
    if config is not None:
        cargs.extend([a for c in [s.run(execution) for s in config] for a in c])
    if help_:
        cargs.append("-help")
    if version:
        cargs.append("-version")
    cargs.append(execution.input_file(input_))
    cargs.append(output)
    ret = MrconvertOutputs(
        root=execution.output_file("."),
        output=execution.output_file(output),
        json_export=execution.output_file(json_export) if (json_export is not None) else None,
        export_grad_mrtrix=execution.output_file(export_grad_mrtrix) if (export_grad_mrtrix is not None) else None,
        export_pe_table=execution.output_file(export_pe_table) if (export_pe_table is not None) else None,
        export_grad_fsl=export_grad_fsl.outputs(execution) if export_grad_fsl else None,
        export_pe_eddy=export_pe_eddy.outputs(execution) if export_pe_eddy else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MRCONVERT_METADATA",
    "MrconvertAppendProperty",
    "MrconvertClearProperty",
    "MrconvertConfig",
    "MrconvertCoord",
    "MrconvertExportGradFsl",
    "MrconvertExportGradFslOutputs",
    "MrconvertExportPeEddy",
    "MrconvertExportPeEddyOutputs",
    "MrconvertFslgrad",
    "MrconvertImportPeEddy",
    "MrconvertOutputs",
    "MrconvertSetProperty",
    "MrconvertVariousFile",
    "MrconvertVariousFile_",
    "MrconvertVariousString",
    "MrconvertVariousString_",
    "mrconvert",
]
