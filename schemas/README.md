# NiWrap Metadata Schema Documentation

This directory contains JSON schemas that define and validate the NiWrap repository structure. These schemas enable IDE autocompletion, real-time validation, and ensure consistency across the project.

## Quick Start

### Repository Structure

```
src/
├── projects.json             # Root - lists all projects
└── {project}/
    ├── project.json          # Project configuration
    └── {package}/
        ├── package.json      # Package metadata
        └── {version}/
            ├── version.json  # Version configuration
            └── {app}/
                ├── app.json      # Application metadata
                └── boutiques.json  # Tool descriptor
```

## Schema Reference

### Common Conventions

All metadata files follow these patterns:

**Identifiers**
- Use kebab-case: `my-tool`, `fsl-fast`
- The `name` field must match its directory name
- Example: `src/niwrap/fsl/package.json` has `"name": "fsl"`

**Documentation Block**
```json
"docs": {
  "title": "Human-Readable Title",
  "description": "Detailed description with context",
  "authors": ["Author Name", "Organization"],
  "literature": ["Citation 1", "Citation 2"],
  "urls": ["https://official-site.com", "https://docs.example.com"]
}
```

---

## File Specifications

### `projects.json` - Root Index

Lists all available projects in the repository.

**Location:** `src/projects.json`

**Required Fields:**
- `projects` - Array of project identifiers

**Example:**
```json
{
  "projects": ["niwrap"]
}
```

**Multi-project example:**
```json
{
  "projects": ["niwrap", "bioimaging", "proteomics"]
}
```

---

### `project.json` - Project Configuration

Defines the overall project metadata and available packages.

**Location:** `src/{project}/project.json`

**Required Fields:**
- `name` - Project identifier (must match directory name)
- `version` - Semantic version (e.g., `"1.0.0"`)
- `license` - SPDX license identifier (e.g., `"MIT"`)
- `packages` - Array of available package names

**Optional Fields:**
- `docs` - Project documentation block

**Example:**
```json
{
  "name": "niwrap",
  "version": "1.0.0",
  "license": "MIT",
  "packages": ["afni", "fsl", "mrtrix3"],
  "docs": {
    "title": "NiWrap",
    "description": "Python and container wrappers for neuroimaging tools",
    "authors": ["CMI DAIR"],
    "urls": ["https://github.com/styx-api/niwrap"]
  }
}
```

---

### `package.json` - Package Metadata

Describes a neuroimaging software package and its available versions.

**Location:** `src/{project}/{package}/package.json`

**Required Fields:**
- `name` - Package identifier (must match directory name)
- `versions` - Array of version strings available for this package

**Optional Fields:**
- `default` - Recommended version identifier
- `docs` - Package documentation block

**Example:**
```json
{
  "name": "fsl",
  "versions": ["6.0.7", "6.0.8", "6.0.9"],
  "default": "6.0.7",
  "docs": {
    "title": "FSL",
    "description": "FMRIB Software Library for brain imaging analysis",
    "authors": ["FMRIB Analysis Group, University of Oxford"],
    "urls": ["https://fsl.fmrib.ox.ac.uk/"]
  }
}
```

---

### `version.json` - Version Configuration

Specifies configuration and available apps for a specific package version.

**Location:** `src/{project}/{package}/{version}/version.json`

**Required Fields:**
- `name` - Version identifier (must match directory name)

**Optional Fields:**
- `container` - Container image reference (e.g., `"fsl/fsl:6.0.7"`)
- `apps` - Array of wrapped application names
- `executables` - Executable validation configuration for CI
  - `required` - Executables that must exist in the container (validated by CI)
  - `ignored` - Executables explicitly excluded from wrapping
- `release_date` - Release date in ISO 8601 format (`"YYYY-MM-DD"`)
- `deprecated` - Boolean flag indicating deprecated versions
- `docs` - Version-specific documentation

**Example:**
```json
{
  "name": "6.0.7",
  "container": "fsl/fsl:6.0.7",
  "release_date": "2023-12-15",
  "apps": ["bet", "flirt", "fast"],
  "executables": {
    "required": ["bet", "flirt", "fast", "fslmaths"],
    "ignored": ["old-deprecated-tool"]
  }
}
```

**Notes:**
- For tools with subcommands (e.g., `wb_command -add-to-spec-file`), only list the base executable (`wb_command`) in `executables.required`
- The `executables.required` list is used by CI to verify container contents

---

### `app.json` - Application Metadata

Describes an individual tool or command within a package version.

**Location:** `src/{project}/{package}/{version}/{app}/app.json`

**Required Fields:**
- `name` - Application identifier (must match directory name)

**Optional Fields:**
- `exe` - Executable name (use when different from `name`, e.g., for subcommands)
- `args` - Fixed arguments prepended before descriptor arguments (for subcommands)
- `source` - Descriptor source configuration
  - `type` - Descriptor format: `"boutiques"` or `"cwl"`
  - `path` - Relative path to descriptor file (e.g., `"boutiques.json"`)
- `docs` - Application documentation block

**Example (Simple Command):**
```json
{
  "name": "bet",
  "source": {
    "type": "boutiques",
    "path": "boutiques.json"
  },
  "docs": {
    "description": "Brain Extraction Tool - removes non-brain tissue from images"
  }
}
```

**Example (Subcommand):**
```json
{
  "name": "add-to-spec-file",
  "exe": "wb_command",
  "args": ["-add-to-spec-file"],
  "source": {
    "type": "boutiques",
    "path": "boutiques.json"
  },
  "docs": {
    "description": "Add data files to a Connectome Workbench spec file"
  }
}
```

**Example (Placeholder):**
```json
{
  "name": "future-tool",
  "docs": {
    "description": "Tool not yet wrapped - descriptor coming soon"
  }
}
```

**Notes:**
- Omit the `source` field for tools that don't yet have descriptors
- For subcommands, `exe` specifies the actual binary, while `args` provides fixed arguments

---

## IDE Integration

### Visual Studio Code

The repository includes `.vscode/settings.json` with schema associations. This provides:

- **Autocompletion** - Field name and value suggestions
- **Validation** - Real-time error highlighting
- **Documentation** - Hover tooltips showing field descriptions
- **Snippets** - Quick templates for common patterns

### Other Editors

Most modern editors support JSON Schema:

| Editor | Support |
|--------|---------|
| **IntelliJ/PyCharm** | Automatic detection from `$schema` field |
| **Sublime Text** | Via `LSP-json` plugin |
| **Vim/Neovim** | Via `coc-json` or LSP client |
| **Emacs** | Via `lsp-mode` with JSON language server |

---

## Validation

### Command Line

```bash
# Validate all metadata files
# TODO: Add validation script

# Validate specific project
# TODO: Add project-specific validation

# Validate specific package
# TODO: Add package-specific validation

# Verbose output with detailed errors
# TODO: Add verbose mode
```

### CI Integration

CI pipelines should validate:
1. All JSON files conform to their schemas
2. Referenced files exist (apps in versions, versions in packages, packages in projects, projects in root)
3. Required executables exist in containers
4. No duplicate names within scopes

**TODO:** Add CI validation configuration

---

## Design Principles

### Self-Documenting Structure

The directory hierarchy mirrors the conceptual model:
- `projects` contains `project`
- `project` contains `packages`
- `package` contains `versions`
- `version` contains `apps`

File names match their identifiers, making the structure intuitive to navigate.

### Consistency

All schemas follow uniform patterns:
- Every file has a `name` field matching its directory
- Documentation uses the standard `docs` block format
- Identifiers use kebab-case throughout
- Optional fields are truly optional - required fields are minimal

### Extensibility

The schema design allows for future expansion:
- Multiple projects in one repository
- Additional descriptor formats via `source.type`
- New documentation fields in `docs` blocks
- Package-specific extensions without breaking validation

---

## Schema Files

| Schema | Purpose | Validates |
|--------|---------|-----------|
| `projects.schema.json` | Root projects index | `src/projects.json` |
| `project.schema.json` | Project configuration | `src/{project}/project.json` |
| `package.schema.json` | Package metadata | `src/{project}/{package}/package.json` |
| `version.schema.json` | Version configuration | `src/{project}/{package}/{version}/version.json` |
| `app.schema.json` | Application metadata | `src/{project}/{package}/{version}/{app}/app.json` |
| `schemas.json` | Schema index | Pattern matching rules |

Schemas are hosted statically and referenced via URL for IDE integration.

---

## Example Path Hierarchy

```
src/projects.json                          → Lists: ["niwrap"]
src/niwrap/project.json                    → Lists: ["afni", "fsl"]
src/niwrap/fsl/package.json                → Lists: ["6.0.7", "6.0.8"]
src/niwrap/fsl/6.0.7/version.json          → Lists: ["bet", "flirt"]
src/niwrap/fsl/6.0.7/bet/app.json          → Describes: bet tool
src/niwrap/fsl/6.0.7/bet/boutiques.json    → Descriptor: bet parameters
```

---

## Contributing

When adding or modifying metadata:

1. **Use your IDE** - Let schema validation catch errors early
2. **Follow conventions** - Match existing patterns for consistency
3. **Document thoroughly** - Use `docs` blocks to explain purpose and usage
4. **Validate before committing** - Run validation scripts (when available)
5. **Keep it minimal** - Only add fields when necessary

For questions or issues with the schema design, open an issue in the repository.