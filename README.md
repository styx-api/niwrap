# NiWrap <img src="logo.svg" align="right" width="25%"/>

[![PyPI](https://img.shields.io/pypi/v/niwrap.svg)](https://pypi.org/project/niwrap/)
[![npm](https://img.shields.io/npm/v/niwrap.svg)](https://www.npmjs.com/package/niwrap)
[![CRAN status](https://img.shields.io/badge/CRAN-coming%20soon-orange)](https://cran.r-project.org/)
[![GitHub stars](https://img.shields.io/github/stars/styx-api/niwrap?style=social)](https://github.com/styx-api/niwrap/stargazers)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Preprint](https://img.shields.io/badge/bioRxiv-preprint-green?logo=bookstack&logoColor=white)](https://doi.org/10.1101/2025.07.24.666435)
[![Discord](https://dcbadge.limes.pink/api/server/https://discord.gg/QMKUVCFWsR?style=flat)](https://discord.gg/QMKUVCFWsR)

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

| Package | Status | Version | API Coverage |
| --- | --- | --- | --- |
| [AFNI](https://afni.nimh.nih.gov/) | Experimental | [`24.2.06`](https://hub.docker.com/r/afni/afni_make_build) | <img src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTI1IiBoZWlnaHQ9IjI0IiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjxkZWZzPjxjbGlwUGF0aCBpZD0iciI+PHJlY3Qgd2lkdGg9IjEyNSIgaGVpZ2h0PSIyNCIgcng9IjgiLz48L2NsaXBQYXRoPjwvZGVmcz48ZyBjbGlwLXBhdGg9InVybCgjcikiPjxyZWN0IHdpZHRoPSIxMjUiIGhlaWdodD0iMjQiIGZpbGw9IiNmZmYiIGZpbGwtb3BhY2l0eT0iLjE1Ii8+PHJlY3Qgd2lkdGg9IjExNS41ODkxOTgwMzYwMDY1NiIgaGVpZ2h0PSIyNCIgZmlsbD0iIzNiODJmNiIvPjwvZz48dGV4dCB4PSI2Mi41IiB5PSIxNiIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZmlsbD0iI2ZmZiIgZm9udC1zaXplPSIxMiIgZm9udC13ZWlnaHQ9IjYwMCIgZm9udC1mYW1pbHk9InN5c3RlbS11aSxzYW5zLXNlcmlmIj41NjUvNjExPC90ZXh0Pjwvc3ZnPg==" alt="565/611"> |
| [ANTs](https://github.com/ANTsX/ANTs) | Experimental | [`2.5.3`](https://hub.docker.com/r/antsx/ants) | <img src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTI1IiBoZWlnaHQ9IjI0IiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjxkZWZzPjxjbGlwUGF0aCBpZD0iciI+PHJlY3Qgd2lkdGg9IjEyNSIgaGVpZ2h0PSIyNCIgcng9IjgiLz48L2NsaXBQYXRoPjwvZGVmcz48ZyBjbGlwLXBhdGg9InVybCgjcikiPjxyZWN0IHdpZHRoPSIxMjUiIGhlaWdodD0iMjQiIGZpbGw9IiNmZmYiIGZpbGwtb3BhY2l0eT0iLjE1Ii8+PHJlY3Qgd2lkdGg9Ijc4LjUzOTgyMzAwODg0OTU1IiBoZWlnaHQ9IjI0IiBmaWxsPSIjM2I4MmY2Ii8+PC9nPjx0ZXh0IHg9IjYyLjUiIHk9IjE2IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmaWxsPSIjZmZmIiBmb250LXNpemU9IjEyIiBmb250LXdlaWdodD0iNjAwIiBmb250LWZhbWlseT0ic3lzdGVtLXVpLHNhbnMtc2VyaWYiPjcxLzExMzwvdGV4dD48L3N2Zz4=" alt="71/113"> |
| [Connectome Workbench](https://github.com/Washington-University/workbench) | Experimental | [`1.5.0`](https://hub.docker.com/r/brainlife/connectome_workbench) | <img src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTI1IiBoZWlnaHQ9IjI0IiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjxkZWZzPjxjbGlwUGF0aCBpZD0iciI+PHJlY3Qgd2lkdGg9IjEyNSIgaGVpZ2h0PSIyNCIgcng9IjgiLz48L2NsaXBQYXRoPjwvZGVmcz48ZyBjbGlwLXBhdGg9InVybCgjcikiPjxyZWN0IHdpZHRoPSIxMjUiIGhlaWdodD0iMjQiIGZpbGw9IiNmZmYiIGZpbGwtb3BhY2l0eT0iLjE1Ii8+PHJlY3Qgd2lkdGg9IjEyNS4wIiBoZWlnaHQ9IjI0IiBmaWxsPSIjMjJjNTVlIi8+PC9nPjx0ZXh0IHg9IjYyLjUiIHk9IjE2IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmaWxsPSIjZmZmIiBmb250LXNpemU9IjEyIiBmb250LXdlaWdodD0iNjAwIiBmb250LWZhbWlseT0ic3lzdGVtLXVpLHNhbnMtc2VyaWYiPjIwMi8yMDI8L3RleHQ+PC9zdmc+" alt="202/202"> |
| [Convert3D](http://www.itksnap.org/pmwiki/pmwiki.php?n=Convert3D.Convert3D) | Experimental | [`1.1.0`](https://hub.docker.com/r/pyushkevich/itksnap) | <img src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTI1IiBoZWlnaHQ9IjI0IiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjxkZWZzPjxjbGlwUGF0aCBpZD0iciI+PHJlY3Qgd2lkdGg9IjEyNSIgaGVpZ2h0PSIyNCIgcng9IjgiLz48L2NsaXBQYXRoPjwvZGVmcz48ZyBjbGlwLXBhdGg9InVybCgjcikiPjxyZWN0IHdpZHRoPSIxMjUiIGhlaWdodD0iMjQiIGZpbGw9IiNmZmYiIGZpbGwtb3BhY2l0eT0iLjE1Ii8+PHJlY3Qgd2lkdGg9IjEyNS4wIiBoZWlnaHQ9IjI0IiBmaWxsPSIjMjJjNTVlIi8+PC9nPjx0ZXh0IHg9IjYyLjUiIHk9IjE2IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmaWxsPSIjZmZmIiBmb250LXNpemU9IjEyIiBmb250LXdlaWdodD0iNjAwIiBmb250LWZhbWlseT0ic3lzdGVtLXVpLHNhbnMtc2VyaWYiPjQvNDwvdGV4dD48L3N2Zz4=" alt="4/4"> |
| [FSL](https://fsl.fmrib.ox.ac.uk/fsl/fslwiki) | Experimental | [`6.0.4`](https://hub.docker.com/r/brainlife/fsl) | <img src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTI1IiBoZWlnaHQ9IjI0IiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjxkZWZzPjxjbGlwUGF0aCBpZD0iciI+PHJlY3Qgd2lkdGg9IjEyNSIgaGVpZ2h0PSIyNCIgcng9IjgiLz48L2NsaXBQYXRoPjwvZGVmcz48ZyBjbGlwLXBhdGg9InVybCgjcikiPjxyZWN0IHdpZHRoPSIxMjUiIGhlaWdodD0iMjQiIGZpbGw9IiNmZmYiIGZpbGwtb3BhY2l0eT0iLjE1Ii8+PHJlY3Qgd2lkdGg9Ijk3Ljg0MzQ1MDQ3OTIzMzIzIiBoZWlnaHQ9IjI0IiBmaWxsPSIjM2I4MmY2Ii8+PC9nPjx0ZXh0IHg9IjYyLjUiIHk9IjE2IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmaWxsPSIjZmZmIiBmb250LXNpemU9IjEyIiBmb250LXdlaWdodD0iNjAwIiBmb250LWZhbWlseT0ic3lzdGVtLXVpLHNhbnMtc2VyaWYiPjI0NS8zMTM8L3RleHQ+PC9zdmc+" alt="245/313"> |
| [FastSurfer](https://github.com/Deep-MI/FastSurfer) | Experimental | [`2.3.3`](https://hub.docker.com/r/deepmi/fastsurfer) | <img src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTI1IiBoZWlnaHQ9IjI0IiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjxkZWZzPjxjbGlwUGF0aCBpZD0iciI+PHJlY3Qgd2lkdGg9IjEyNSIgaGVpZ2h0PSIyNCIgcng9IjgiLz48L2NsaXBQYXRoPjwvZGVmcz48ZyBjbGlwLXBhdGg9InVybCgjcikiPjxyZWN0IHdpZHRoPSIxMjUiIGhlaWdodD0iMjQiIGZpbGw9IiNmZmYiIGZpbGwtb3BhY2l0eT0iLjE1Ii8+PHJlY3Qgd2lkdGg9IjEyNS4wIiBoZWlnaHQ9IjI0IiBmaWxsPSIjMjJjNTVlIi8+PC9nPjx0ZXh0IHg9IjYyLjUiIHk9IjE2IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmaWxsPSIjZmZmIiBmb250LXNpemU9IjEyIiBmb250LXdlaWdodD0iNjAwIiBmb250LWZhbWlseT0ic3lzdGVtLXVpLHNhbnMtc2VyaWYiPjEvMTwvdGV4dD48L3N2Zz4=" alt="1/1"> |
| [FreeSurfer](https://github.com/freesurfer/freesurfer) | Experimental | [`7.4.1`](https://hub.docker.com/r/freesurfer/freesurfer) | <img src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTI1IiBoZWlnaHQ9IjI0IiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjxkZWZzPjxjbGlwUGF0aCBpZD0iciI+PHJlY3Qgd2lkdGg9IjEyNSIgaGVpZ2h0PSIyNCIgcng9IjgiLz48L2NsaXBQYXRoPjwvZGVmcz48ZyBjbGlwLXBhdGg9InVybCgjcikiPjxyZWN0IHdpZHRoPSIxMjUiIGhlaWdodD0iMjQiIGZpbGw9IiNmZmYiIGZpbGwtb3BhY2l0eT0iLjE1Ii8+PHJlY3Qgd2lkdGg9IjExMC4yNjYxNTk2OTU4MTc0OSIgaGVpZ2h0PSIyNCIgZmlsbD0iIzNiODJmNiIvPjwvZz48dGV4dCB4PSI2Mi41IiB5PSIxNiIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZmlsbD0iI2ZmZiIgZm9udC1zaXplPSIxMiIgZm9udC13ZWlnaHQ9IjYwMCIgZm9udC1mYW1pbHk9InN5c3RlbS11aSxzYW5zLXNlcmlmIj42OTYvNzg5PC90ZXh0Pjwvc3ZnPg==" alt="696/789"> |
| [Greedy](https://sites.google.com/view/greedyreg/about) | Experimental | [`1.0.1`](https://hub.docker.com/r/pyushkevich/itksnap) | <img src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTI1IiBoZWlnaHQ9IjI0IiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjxkZWZzPjxjbGlwUGF0aCBpZD0iciI+PHJlY3Qgd2lkdGg9IjEyNSIgaGVpZ2h0PSIyNCIgcng9IjgiLz48L2NsaXBQYXRoPjwvZGVmcz48ZyBjbGlwLXBhdGg9InVybCgjcikiPjxyZWN0IHdpZHRoPSIxMjUiIGhlaWdodD0iMjQiIGZpbGw9IiNmZmYiIGZpbGwtb3BhY2l0eT0iLjE1Ii8+PHJlY3Qgd2lkdGg9IjEyNS4wIiBoZWlnaHQ9IjI0IiBmaWxsPSIjMjJjNTVlIi8+PC9nPjx0ZXh0IHg9IjYyLjUiIHk9IjE2IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmaWxsPSIjZmZmIiBmb250LXNpemU9IjEyIiBmb250LXdlaWdodD0iNjAwIiBmb250LWZhbWlseT0ic3lzdGVtLXVpLHNhbnMtc2VyaWYiPjEvMTwvdGV4dD48L3N2Zz4=" alt="1/1"> |
| [MRTrix3](https://www.mrtrix.org/) | Well tested | [`3.0.4`](https://hub.docker.com/r/mrtrix3/mrtrix3) | <img src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTI1IiBoZWlnaHQ9IjI0IiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjxkZWZzPjxjbGlwUGF0aCBpZD0iciI+PHJlY3Qgd2lkdGg9IjEyNSIgaGVpZ2h0PSIyNCIgcng9IjgiLz48L2NsaXBQYXRoPjwvZGVmcz48ZyBjbGlwLXBhdGg9InVybCgjcikiPjxyZWN0IHdpZHRoPSIxMjUiIGhlaWdodD0iMjQiIGZpbGw9IiNmZmYiIGZpbGwtb3BhY2l0eT0iLjE1Ii8+PHJlY3Qgd2lkdGg9IjExOC44MDE2NTI4OTI1NjE5OSIgaGVpZ2h0PSIyNCIgZmlsbD0iIzNiODJmNiIvPjwvZz48dGV4dCB4PSI2Mi41IiB5PSIxNiIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZmlsbD0iI2ZmZiIgZm9udC1zaXplPSIxMiIgZm9udC13ZWlnaHQ9IjYwMCIgZm9udC1mYW1pbHk9InN5c3RlbS11aSxzYW5zLXNlcmlmIj4xMTUvMTIxPC90ZXh0Pjwvc3ZnPg==" alt="115/121"> |
| [MRTrix3Tissue](https://3tissue.github.io/) | Well tested | [`5.2.8`](https://hub.docker.com/r/brainlife/3tissue) | <img src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTI1IiBoZWlnaHQ9IjI0IiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjxkZWZzPjxjbGlwUGF0aCBpZD0iciI+PHJlY3Qgd2lkdGg9IjEyNSIgaGVpZ2h0PSIyNCIgcng9IjgiLz48L2NsaXBQYXRoPjwvZGVmcz48ZyBjbGlwLXBhdGg9InVybCgjcikiPjxyZWN0IHdpZHRoPSIxMjUiIGhlaWdodD0iMjQiIGZpbGw9IiNmZmYiIGZpbGwtb3BhY2l0eT0iLjE1Ii8+PHJlY3Qgd2lkdGg9IjEyNS4wIiBoZWlnaHQ9IjI0IiBmaWxsPSIjMjJjNTVlIi8+PC9nPjx0ZXh0IHg9IjYyLjUiIHk9IjE2IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmaWxsPSIjZmZmIiBmb250LXNpemU9IjEyIiBmb250LXdlaWdodD0iNjAwIiBmb250LWZhbWlseT0ic3lzdGVtLXVpLHNhbnMtc2VyaWYiPjEvMTwvdGV4dD48L3N2Zz4=" alt="1/1"> |
| [NiftyReg](http://cmictig.cs.ucl.ac.uk/wiki/index.php/NiftyReg) | Experimental | [`1.4.0`](https://hub.docker.com/r/vnmd/niftyreg_1.4.0) | <img src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTI1IiBoZWlnaHQ9IjI0IiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjxkZWZzPjxjbGlwUGF0aCBpZD0iciI+PHJlY3Qgd2lkdGg9IjEyNSIgaGVpZ2h0PSIyNCIgcng9IjgiLz48L2NsaXBQYXRoPjwvZGVmcz48ZyBjbGlwLXBhdGg9InVybCgjcikiPjxyZWN0IHdpZHRoPSIxMjUiIGhlaWdodD0iMjQiIGZpbGw9IiNmZmYiIGZpbGwtb3BhY2l0eT0iLjE1Ii8+PHJlY3Qgd2lkdGg9IjEyNS4wIiBoZWlnaHQ9IjI0IiBmaWxsPSIjMjJjNTVlIi8+PC9nPjx0ZXh0IHg9IjYyLjUiIHk9IjE2IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmaWxsPSIjZmZmIiBmb250LXNpemU9IjEyIiBmb250LXdlaWdodD0iNjAwIiBmb250LWZhbWlseT0ic3lzdGVtLXVpLHNhbnMtc2VyaWYiPjcvNzwvdGV4dD48L3N2Zz4=" alt="7/7"> |
| [dcm2niix](https://github.com/rordenlab/dcm2niix) | Experimental | [`1.0.20240202`](https://hub.docker.com/r/vnmd/dcm2niix_v1.0.20240202) | <img src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTI1IiBoZWlnaHQ9IjI0IiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjxkZWZzPjxjbGlwUGF0aCBpZD0iciI+PHJlY3Qgd2lkdGg9IjEyNSIgaGVpZ2h0PSIyNCIgcng9IjgiLz48L2NsaXBQYXRoPjwvZGVmcz48ZyBjbGlwLXBhdGg9InVybCgjcikiPjxyZWN0IHdpZHRoPSIxMjUiIGhlaWdodD0iMjQiIGZpbGw9IiNmZmYiIGZpbGwtb3BhY2l0eT0iLjE1Ii8+PHJlY3Qgd2lkdGg9IjEyNS4wIiBoZWlnaHQ9IjI0IiBmaWxsPSIjMjJjNTVlIi8+PC9nPjx0ZXh0IHg9IjYyLjUiIHk9IjE2IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmaWxsPSIjZmZmIiBmb250LXNpemU9IjEyIiBmb250LXdlaWdodD0iNjAwIiBmb250LWZhbWlseT0ic3lzdGVtLXVpLHNhbnMtc2VyaWYiPjEvMTwvdGV4dD48L3N2Zz4=" alt="1/1"> |
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
from niwrap import fsl, ants, mrtrix

# Optional: Use Docker to run all tools (no local installation needed)
import niwrap
niwrap.use_docker()

# Run FSL's BET brain extraction
outputs = fsl.bet(
    infile="input.nii.gz", 
    maskfile="brain.nii.gz", 
    fractional_intensity=0.5,
    binary_mask=True,
)
# outputs.outfile -> "brain.nii.gz"
# outputs.binary_mask -> "brain_mask.nii.gz"

# Calculate fiber orientation distributions with MRTrix3
fod_outputs = mrtrix.dwi2fod(
    algorithm="csd",
    dwi="dwi.mif",
    response_odf=[
        mrtrix.dwi2fod_response_odf_params(
            response="wm_response.txt",
            odf="wmfod.mif",
        ),
    ]
)
# fod_outputs.response_odf[0].odf -> "wmfod.mif"
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
outputs <- fsl$bet("input.nii.gz", "brain.nii.gz", fractional_intensity=0.5)
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

For complete documentation on using NiWrap, configuring Styx, and contributing to the project, please visit our [Styx Book](https://styx-api.github.io/styxbook/).

## 📋 Prerequisites

To use NiWrap without containers, you need to have the corresponding neuroimaging packages installed on your system. Using the container integration features (`use_docker()` or `use_singularity()`) eliminates this requirement.

## 🤝 Contributing

We welcome contributions! Whether you want to add support for new neuroimaging tools, improve existing descriptors, or fix bugs, please feel free to open an issue or submit a pull request.

See our [contribution guide](https://styx-api.github.io/styxbook/contributing.html) for more information.

## 📄 License

NiWrap is released under the MIT License. See the LICENSE file for details.

**Important Note:** NiWrap provides wrappers for third-party neuroimaging tools, each with its own license. Please consult the license terms of each individual tool before use in your projects. NiWrap does not modify or redistribute these tools; it simply provides interfaces to them.

## 📚 Citation

If you use NiWrap in your research, please consider citing:

```bibtex
@article {rupprecht2025styx,
	author = {Rupprecht, Florian JM and Kai, Jason and Shrestha, Biraj and Giavasis, Steven and Xu, Ting and Glatard, Tristan and Milham, Michael P and Kiar, Gregory},
	title = {Styx: A multi-language API Generator for Command-Line Tools},
	elocation-id = {2025.07.24.666435},
	year = {2025},
	doi = {10.1101/2025.07.24.666435},
	publisher = {Cold Spring Harbor Laboratory},
	URL = {https://www.biorxiv.org/content/early/2025/07/30/2025.07.24.666435},
	eprint = {https://www.biorxiv.org/content/early/2025/07/30/2025.07.24.666435.full.pdf},
	journal = {bioRxiv}
}
```

## 🔗 Related Projects

- [Styx Compiler](https://github.com/styx-api/styx)
- [Styx Documentation](https://styx-api.github.io/styxbook/)
- [Boutiques](https://boutiques.github.io/)
