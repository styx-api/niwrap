# NiWrap <img src="logo.png" align="right" width="25%"/>

[![PyPI](https://img.shields.io/pypi/v/niwrap.svg)](https://pypi.org/project/niwrap/)
[![npm](https://img.shields.io/npm/v/niwrap.svg)](https://www.npmjs.com/package/niwrap)
[![CRAN status](https://img.shields.io/badge/CRAN-coming%20soon-orange)](https://cran.r-project.org/)
[![GitHub stars](https://img.shields.io/github/stars/styx-api/niwrap?style=social)](https://github.com/styx-api/niwrap/stargazers)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

## 🧠 Modern Neuroimaging Made Simple

NiWrap provides seamless, programmatic access to powerful neuroimaging command-line tools through clean, type-safe APIs in Python, TypeScript, and R (coming soon). Stop struggling with command-line parameters and focus on your neuroimaging workflows.

## ✨ Key Features

- **Type-Safe APIs**: Leverage full IDE autocompletion and type checking
- **Extensive Coverage**: Access tools from FSL, FreeSurfer, ANTs, MRTrix3, and more
- **Cross-Language Support**: Use the same tools in Python, TypeScript, or R
- **Consistent Interface**: Uniform API design across all neuroimaging packages
- **Container Integration**: Seamlessly run tools in Docker, Singularity, or other container environments
- **Structured Outputs**: All functions return organized output paths for simple pipeline creation

## 🧰 Supported Packages

<!-- START_PACKAGES_TABLE -->
<!-- Package table will be auto-generated here -->
<!-- END_PACKAGES_TABLE -->
<small>*API Coverage: The percentages shown represent the proportion of tool binaries with available NiWrap descriptors, not the completeness of each descriptor.*</small>

## 🚀 Getting Started

### Installation

<details>
<summary><b>Python</b></summary>

```bash
pip install niwrap
```
</details>

<details>
<summary><b>TypeScript/JavaScript</b></summary>

```bash
npm install niwrap
# or
yarn add niwrap
```
</details>

<details>
<summary><b>R (Coming Soon)</b></summary>

```bash
# Not yet available on CRAN
# Coming soon!
```
</details>

### Basic Usage Examples

<details open>
<summary><b>Python</b></summary>

```python
from niwrap import fsl, ants, mrtrix3

# Optional: Use Docker to run all tools (no local installation needed)
import niwrap
niwrap.use_docker()

# Run FSL's BET brain extraction
outputs = fsl.bet("input.nii.gz", "brain.nii.gz", f=0.5)
# outputs.output_file -> "brain.nii.gz"
# outputs.mask_file -> "brain_mask.nii.gz"

# Chain outputs into next step
reg_outputs = ants.antsRegistration(
    fixed="t1.nii.gz", 
    moving=outputs.output_file,  # Use the BET output
    output_prefix="reg_",
    transform_type="s"  # Rigid transformation
)
# reg_outputs.warped_image -> "reg_Warped.nii.gz"
# reg_outputs.inverse_warped_image -> "reg_InverseWarped.nii.gz"

# Calculate fiber orientation distributions with MRTrix3
fod_outputs = mrtrix3.dwi2fod(
    algorithm="csd",
    in_file="dwi.mif",
    wm_txt="wm_response.txt",
    wm_odf="wmfod.mif"
)
# fod_outputs.wm_odf -> "wmfod.mif"
```
</details>

<details>
<summary><b>TypeScript/JavaScript</b></summary>

```typescript
import { niwrap, fsl, ants, mrtrix3 } from 'niwrap';

// Optional: Use Docker to run all tools (no local installation needed)
niwrap.useDocker();

// Run FSL's BET brain extraction
const outputs = await fsl.bet({
    input: "input.nii.gz", 
    output: "brain.nii.gz",
    f: 0.5 
});
// outputs.outputFile -> "brain.nii.gz"
// outputs.maskFile -> "brain_mask.nii.gz"

// Chain outputs into next step
const regOutputs = await ants.antsRegistration({
    fixed: "t1.nii.gz", 
    moving: outputs.outputFile,  // Use the BET output
    outputPrefix: "reg_",
    transformType: "s"  // Rigid transformation
});
// regOutputs.warpedImage -> "reg_Warped.nii.gz"
// regOutputs.inverseWarpedImage -> "reg_InverseWarped.nii.gz"

// Calculate fiber orientation distributions with MRTrix3
const fodOutputs = await mrtrix3.dwi2fod({
    algorithm: "csd",
    in_file: "dwi.mif",
    wm_txt: "wm_response.txt",
    wm_odf: "wmfod.mif"
});
// fodOutputs.wmOdf -> "wmfod.mif"
```
</details>

<details>
<summary><b>R (Coming Soon)</b></summary>

```R
library(niwrap)

# Optional: Use Docker to run all tools (no local installation needed)
niwrap$use_docker()

# Run FSL's BET brain extraction
outputs <- fsl$bet("input.nii.gz", "brain.nii.gz", f=0.5)
# outputs$output_file -> "brain.nii.gz"
# outputs$mask_file -> "brain_mask.nii.gz"

# More functionality coming soon!
```
</details>

## 🔧 Container Orchestration

NiWrap handles container orchestration for you, making it easy to run tools without installing them locally:

<details>
<summary><b>Python</b></summary>

```python
import niwrap

# Use Docker containers
niwrap.use_docker()

# Use Singularity containers
niwrap.use_singularity()

# Custom container configuration
niwrap.use_docker()
```
</details>

<details>
<summary><b>TypeScript/JavaScript</b></summary>

```typescript
import { niwrap } from 'niwrap';

// Use Docker containers
niwrap.useDocker();

// Use Singularity containers
niwrap.useSingularity();

// Custom container configuration
niwrap.useDocker({
    bindMounts: ["/data:/data"],
    envs: {"CUDA_VISIBLE_DEVICES": "0"}
});
```
</details>

<details>
<summary><b>R (Coming Soon)</b></summary>

```R
library(niwrap)

# Use Docker containers
niwrap$use_docker()

# Use Singularity containers
niwrap$use_singularity()

# Custom container configuration
niwrap$use_docker(
    bind_mounts = c("/data:/data"),
    envs = list(CUDA_VISIBLE_DEVICES = "0")
)
```
</details>

## 🔍 How It Works

NiWrap is powered by the [Styx](https://github.com/styx-api/styx) compiler, which transforms structured descriptors (using the [Boutiques](https://boutiques.github.io/) standard) into type-safe language bindings. This repository contains the descriptors, while the compiled packages are available in separate repositories:

- [niwrap-python](https://github.com/styx-api/niwrap-python)
- [niwrap-js](https://github.com/styx-api/niwrap-js)
- [niwrap-r](https://github.com/styx-api/niwrap-r) (in development)

## 📚 Documentation

For complete documentation on using NiWrap, configuring Styx, and contributing to the project, please visit our [Styx Book](https://styx-api.github.io/styx-book/).

## 📋 Prerequisites

To use NiWrap without containers, you need to have the corresponding neuroimaging packages installed on your system. Using the container integration features (`use_docker()` or `use_singularity()`) eliminates this requirement.

## 🤝 Contributing

We welcome contributions! Whether you want to add support for new neuroimaging tools, improve existing descriptors, or fix bugs, please feel free to open an issue or submit a pull request.

See our [contribution guide](https://styx-api.github.io/styx-book/contributing.html) for more information.

## 📄 License

NiWrap is released under the MIT License. See the LICENSE file for details.

**Important Note:** NiWrap provides wrappers for third-party neuroimaging tools, each with its own license. Please consult the license terms of each individual tool before use in your projects. NiWrap does not modify or redistribute these tools; it simply provides interfaces to them.

## 📚 Citation

If you use NiWrap in your research, please consider citing:

```bibtex
% Placeholder - please cite our soon to be released preprint.
@software{niwrap,
  author = {The NiWrap Contributors},
  title = {NiWrap: Type-Safe Neuroimaging Tool Wrappers},
  url = {https://github.com/styx-api/niwrap},
  year = {2023}
}
```

## 🔗 Related Projects

- [Styx Compiler](https://github.com/styx-api/styx)
- [Styx Documentation](https://styx-api.github.io/styx-book/)
- [Boutiques](https://boutiques.github.io/)
