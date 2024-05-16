# This file was auto generated by styx
# Do not edit this file directly

import typing

from ..styxdefs import *


VOLUME_LABEL_MODIFY_KEYS_METADATA = Metadata(
    id="546e3babf05e69949c2e689fe6c05e3566c17bde",
    name="volume-label-modify-keys",
    container_image_type="docker",
    container_image_tag="mcin/docker-fsl:latest",
)


class VolumeLabelModifyKeysOutputs(typing.NamedTuple):
    """
    Output object returned when calling `volume_label_modify_keys(...)`.
    """
    volume_out: OutputPathType
    """the output volume label file"""


def volume_label_modify_keys(
    runner: Runner,
    volume_in: InputPathType,
    remap_file: str,
    volume_out: InputPathType,
    opt_subvolume_subvolume: str | None = None,
) -> VolumeLabelModifyKeysOutputs:
    """
    CHANGE KEY VALUES IN A VOLUME LABEL FILE.
    
    <remap-file> should have lines of the form 'oldkey newkey', like so:
    
    3 5
    5 8
    8 2
    
    This would change the current label with key '3' to use the key '5' instead,
    5 would use 8, and 8 would use 2. Any collision in key values results in the
    label that was not specified in the remap file getting remapped to an
    otherwise unused key. Remapping more than one key to the same new key, or
    the same key to more than one new key, results in an error. This will not
    change the appearance of the file when displayed, as it will change the key
    values in the data at the same time.
    
    Args:
        runner: Command runner
        volume_in: the input volume label file
        remap_file: text file with old and new key values
        volume_out: the output volume label file
        opt_subvolume_subvolume: select a single subvolume: the subvolume number
            or name
    Returns:
        NamedTuple of outputs (described in `VolumeLabelModifyKeysOutputs`).
    """
    execution = runner.start_execution(VOLUME_LABEL_MODIFY_KEYS_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-volume-label-modify-keys")
    cargs.append(execution.input_file(volume_in))
    cargs.append(remap_file)
    cargs.append(execution.input_file(volume_out))
    if opt_subvolume_subvolume is not None:
        cargs.extend(["-subvolume", opt_subvolume_subvolume])
    ret = VolumeLabelModifyKeysOutputs(
        volume_out=execution.output_file(f"{volume_out}"),
    )
    execution.run(cargs)
    return ret
