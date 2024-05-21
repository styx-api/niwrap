# This file was auto generated by styx
# Do not edit this file directly

import typing

from ..styxdefs import *


SCENE_FILE_UPDATE_METADATA = Metadata(
    id="c3ec4360e1dee70beb08f3b1d4f6a80013ea0057",
    name="scene-file-update",
    container_image_type="docker",
    container_image_tag="mcin/docker-fsl:latest",
)


class SceneFileUpdateOutputs(typing.NamedTuple):
    """
    Output object returned when calling `scene_file_update(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def scene_file_update(
    runner: Runner,
    input_scene_file: str,
    output_scene_file: str,
    scene_name_or_number: str,
    opt_fix_map_palette_settings: bool = False,
    opt_remove_missing_files: bool = False,
    opt_error: bool = False,
    opt_verbose: bool = False,
    opt_copy_map_one_palette_data_file_name_suffix: str | None = None,
    opt_data_file_add_name_of_data_file: str | None = None,
    opt_data_file_remove_name_of_data_file: str | None = None,
) -> SceneFileUpdateOutputs:
    """
    scene-file-update by Washington University School of Medicin.
    
    UPDATE SCENE FILE.
    
    This command will update a scene for specific changes in data files.
    
    "-fix-map-palette-settings" will find all data files that have had a change
    in the number of maps since the scene scene was created. If the file has its
    "Apply to All Maps" property enabled, the palette setting in the first map
    is copied to all maps in the file. Note: This modifies the palette settings
    for the file in the scene (data file is NOT modified).
    
    "-copy-map-one-palette" will copy the palette settings from the first map to
    all other maps in a data file. This option is typically used when the number
    of maps in a data file changes. It changes the palette settings in the scene
    that are applied to the data file when the scene is loaded (the data file is
    not modified). The name of the data file specified on the command line is
    matched to the end of file names in the scene. This allows matching multiple
    files if their names end with the same characters. It also allows including
    a relative path when there is more than one file with the same name but in
    different paths and only one of the files to be updated.
    
    "-remove-missing-files" Any files that fail to load when the scene is read
    will be removed from the scene. Thus, if one deletes files prior to running
    with this option, the deleted files are removed from the scene.
    
    "-error" If this option is provided and there is an error while performing
    any of the scene operations, the command will immediately cease processing
    and the output scene file will not be created. Otherwise any errors will be
    listed after the command finishes.
    .
    
    Args:
        runner: Command runner
        input_scene_file: the input scene file
        output_scene_file: the new scene file to create
        scene_name_or_number: name or number (starting at one) of the scene in
            the scene file
        opt_fix_map_palette_settings: Fix palette settings for files with change
            in number of maps
        opt_remove_missing_files: Remove missing files from SpecFile
        opt_error: Abort command if there is an error performing any of the
            operations on the scene file
        opt_verbose: Print names of files that have palettes updated
        opt_copy_map_one_palette_data_file_name_suffix: Copy palettes settings
            from first map to all maps in a data file: Name of palette mapped data
            file (cifti, metric, volume)
        opt_data_file_add_name_of_data_file: Add a data file to scene's loaded
            files: Name of data file. If a data file not in the current directory,
            it is best to use an absolute path (a relative path may work). Instead
            of a data file, this value may be the name of a text file (must end in
            ".txt") that contains the names of one or more data files, one per line.
            Example on UNIX to create a
            text file containing all CIFTI
            scalar files in the current
            directory with absolute paths:
            ls -d $PWD/*dscalar.nii >
            file.txt
        opt_data_file_remove_name_of_data_file: Remove a data file from scene's
            loaded files: Name of data file. If a data file not in the current
            directory, it is best to use an absolute path (a relative path may
            work). Instead of a data file, this value may be the name of a text file
            (must end in ".txt") that contains the names of one or more data files,
            one per line.
            Example on UNIX to create a
            text file containing all
            CIFTI scalar files in the
            current directory with
            absolute paths:
            ls -d $PWD/*dscalar.nii >
            file.txt
    Returns:
        NamedTuple of outputs (described in `SceneFileUpdateOutputs`).
    """
    execution = runner.start_execution(SCENE_FILE_UPDATE_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-scene-file-update")
    cargs.append(input_scene_file)
    cargs.append(output_scene_file)
    cargs.append(scene_name_or_number)
    if opt_fix_map_palette_settings:
        cargs.append("-fix-map-palette-settings")
    if opt_remove_missing_files:
        cargs.append("-remove-missing-files")
    if opt_error:
        cargs.append("-error")
    if opt_verbose:
        cargs.append("-verbose")
    if opt_copy_map_one_palette_data_file_name_suffix is not None:
        cargs.extend(["-copy-map-one-palette", opt_copy_map_one_palette_data_file_name_suffix])
    if opt_data_file_add_name_of_data_file is not None:
        cargs.extend(["-data-file-add", opt_data_file_add_name_of_data_file])
    if opt_data_file_remove_name_of_data_file is not None:
        cargs.extend(["-data-file-remove", opt_data_file_remove_name_of_data_file])
    ret = SceneFileUpdateOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret
