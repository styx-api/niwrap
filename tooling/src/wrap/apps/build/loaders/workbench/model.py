"""Pydantic schema for Connectome Workbench command definitions."""

from pydantic import BaseModel, Field

# Constants for Workbench types
TYPE_STRING = "String"
TYPE_FLOATING_POINT = "Floating Point"
TYPE_INTEGER = "Integer"
TYPE_BOOLEAN = "Boolean"

TYPE_FILE_SURFACE = "Surface File"
TYPE_FILE_BORDER = "Border File"
TYPE_FILE_METRIC = "Metric File"
TYPE_FILE_ANNOTATION = "Annotation File"
TYPE_FILE_CIFTI = "Cifti File"
TYPE_FILE_VOLUME = "Volume File"
TYPE_FILE_LABEL = "Label File"
TYPE_FILE_FOCI = "Foci File"

TYPE_ANY_FILE = frozenset(
    {
        TYPE_FILE_SURFACE,
        TYPE_FILE_BORDER,
        TYPE_FILE_METRIC,
        TYPE_FILE_ANNOTATION,
        TYPE_FILE_CIFTI,
        TYPE_FILE_VOLUME,
        TYPE_FILE_LABEL,
        TYPE_FILE_FOCI,
    }
)


class Parameter(BaseModel):
    """Represents a parameter for a command or option."""

    key: int
    short_name: str
    description: str
    type: str


class Output(BaseModel):
    """Represents an output file from a command or option."""

    key: int
    short_name: str
    description: str
    type: str


class Option(BaseModel):
    """Represents a command-line option with its own parameters, outputs, and sub-options."""

    key: int
    option_switch: str
    description: str
    params: list[Parameter] = Field(default_factory=list)
    outputs: list[Output] = Field(default_factory=list)
    options: list["Option"] = Field(default_factory=list)
    repeatable_options: list["Option"] = Field(default_factory=list)


class WorkbenchCommand(BaseModel):
    """Main schema for a Connectome Workbench command definition."""

    command: str
    short_description: str
    help_text: str
    version_info: list[str]
    params: list[Parameter] = Field(default_factory=list)
    outputs: list[Output] = Field(default_factory=list)
    options: list[Option] = Field(default_factory=list)
    repeatable_options: list[Option] = Field(default_factory=list)


Option.model_rebuild()
