"""
Pydantic schema for Connectome Workbench command definitions.
"""

from pydantic import BaseModel, Field

# Constants for Workbench types
TYPE_STRING = "String"
TYPE_FILE_SURFACE = "Surface File"
TYPE_FILE_BORDER = "Border File"
TYPE_FILE_METRIC = "Metric File"
TYPE_FILE_ANNOTATION = "Annotation File"
TYPE_FILE_CIFTI = "Cifti File"
TYPE_FILE_VOLUME = "Volume File"
TYPE_FILE_LABEL = "Label File"
TYPE_FILE_FOCI = "Foci File"
TYPE_FLOATING_POINT = "Floating Point"
TYPE_INTEGER = "Integer"
TYPE_BOOLEAN = "Boolean"
TYPE_ANY_FILE = {
    TYPE_FILE_SURFACE,
    TYPE_FILE_BORDER,
    TYPE_FILE_METRIC,
    TYPE_FILE_ANNOTATION,
    TYPE_FILE_CIFTI,
    TYPE_FILE_VOLUME,
    TYPE_FILE_LABEL,
    TYPE_FILE_FOCI,
}


class Parameter(BaseModel):
    """Represents a parameter for a command or option."""

    key: int
    short_name: str
    description: str
    type: str


class Output(BaseModel):
    """Represents an output file or result from a command or option."""

    key: int
    short_name: str
    description: str
    type: str


class CommandComponent(BaseModel):
    """Base class for command components that can have parameters, outputs, and options."""

    params: list[Parameter] = Field(default_factory=list)
    outputs: list[Output] = Field(default_factory=list)
    options: list["Option"] = Field(default_factory=list)
    repeatable_options: list["Option"] = Field(default_factory=list)


class Option(CommandComponent):
    """Represents a command-line option with its own parameters, outputs, and sub-options."""

    key: int
    option_switch: str
    description: str


class WorkbenchCommand(CommandComponent):
    """Main schema for a Connectome Workbench command definition."""

    command: str
    short_description: str
    help_text: str
    version_info: list[str]


# Update forward references for recursive Option model
CommandComponent.model_rebuild()
Option.model_rebuild()
WorkbenchCommand.model_rebuild()
