# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

SCENE_FILE_MERGE_METADATA = Metadata(
    id="c5a86083ec4db99dc4360c618252324b7f95a8a1.boutiques",
    name="scene-file-merge",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)


@dataclasses.dataclass
class SceneFileMergeUpTo:
    """
    use an inclusive range of scenes.
    """
    last_column: str
    """the number or name of the last scene to include"""
    opt_reverse: bool = False
    """use the range in reverse order"""
    
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
        cargs.append("-up-to")
        cargs.append(self.last_column)
        if self.opt_reverse:
            cargs.append("-reverse")
        return cargs


@dataclasses.dataclass
class SceneFileMergeScene:
    """
    specify a scene to use.
    """
    scene: str
    """the scene number or name"""
    up_to: SceneFileMergeUpTo | None = None
    """use an inclusive range of scenes"""
    
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
        cargs.append("-scene")
        cargs.append(self.scene)
        if self.up_to is not None:
            cargs.extend(self.up_to.run(execution))
        return cargs


@dataclasses.dataclass
class SceneFileMergeSceneFile:
    """
    specify a scene file to use scenes from.
    """
    scene_file: str
    """the input scene file"""
    scene: list[SceneFileMergeScene] | None = None
    """specify a scene to use"""
    
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
        cargs.append("-scene-file")
        cargs.append(self.scene_file)
        if self.scene is not None:
            cargs.extend([a for c in [s.run(execution) for s in self.scene] for a in c])
        return cargs


class SceneFileMergeOutputs(typing.NamedTuple):
    """
    Output object returned when calling `scene_file_merge(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def scene_file_merge(
    scene_file_out: str,
    scene_file: list[SceneFileMergeSceneFile] | None = None,
    runner: Runner | None = None,
) -> SceneFileMergeOutputs:
    """
    Rearrange scenes into a new file.
    
    Takes one or more scene files and constructs a new scene file by
    concatenating specified scenes from them.
    
    Example: wb_command -scene-file-merge out.scene -scene-file first.scene
    -scene 1 -scene-file second.scene
    
    This example would take the first scene from first.scene, followed by all
    scenes from second.scene, and write these scenes to out.scene.
    
    Author: Washington University School of Medicin
    
    Args:
        scene_file_out: output - the output scene file.
        scene_file: specify a scene file to use scenes from.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SceneFileMergeOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SCENE_FILE_MERGE_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-scene-file-merge")
    cargs.append(scene_file_out)
    if scene_file is not None:
        cargs.extend([a for c in [s.run(execution) for s in scene_file] for a in c])
    ret = SceneFileMergeOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "SCENE_FILE_MERGE_METADATA",
    "SceneFileMergeOutputs",
    "SceneFileMergeScene",
    "SceneFileMergeSceneFile",
    "SceneFileMergeUpTo",
    "scene_file_merge",
]
