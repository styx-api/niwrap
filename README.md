# NiWrap <img src="logo.png" align="right" width="25%"/>

🧠 Modern Python wrappers for neuroimaging tools

## 🚀 Features

- Extensive collection of neuroimaging command line tool metadata
- Generates idiomatic Python wrappers for popular neuroimaging tools
- Based on [Boutiques Descriptor Schema](https://github.com/boutiques/boutiques)
- Powered by [Styx compiler](https://github.com/styx-api/styx)

## 🧰 Supported Packages

<!-- START_PACKAGES_TABLE -->

| Package | Status | Version | API Coverage |
| --- | --- | --- | --- |
| [AFNI](https://afni.nimh.nih.gov/) | Experimental | [`24.2.06`](https://hub.docker.com/r/afni/afni_make_build) | 565/611 (92.5%) |
| [ANTs](https://github.com/ANTsX/ANTs) | Experimental | [`2.5.3`](https://hub.docker.com/r/antsx/ants) | 71/113 (62.8%) |
| [Connectome Workbench](https://github.com/Washington-University/workbench) | Experimental | [`1.5.0`](https://hub.docker.com/r/brainlife/connectome_workbench) | 202/202 (100% 🎉) |
| [Convert3D](http://www.itksnap.org/pmwiki/pmwiki.php?n=Convert3D.Convert3D) | Experimental | [`1.1.0`](https://hub.docker.com/r/pyushkevich/itksnap) | 2/2 (100% 🎉) |
| [FSL](https://fsl.fmrib.ox.ac.uk/fsl/fslwiki) | Experimental | [`6.0.5`](https://hub.docker.com/r/brainlife/fsl) | 239/310 (77.1%) |
| [FastSurfer](https://github.com/Deep-MI/FastSurfer) | Experimental | [`2.3.3`](https://hub.docker.com/r/deepmi/fastsurfer) | 1/1 (100% 🎉) |
| [FreeSurfer](https://github.com/freesurfer/freesurfer) | Experimental | [`7.4.1`](https://hub.docker.com/r/freesurfer/freesurfer) | 707/800 (88.4%) |
| [Greedy](https://sites.google.com/view/greedyreg/about) | Experimental | [`1.0.1`](https://hub.docker.com/r/pyushkevich/itksnap) | 1/1 (100% 🎉) |
| [MRTrix3](https://www.mrtrix.org/) | Well tested | [`3.0.4`](https://hub.docker.com/r/mrtrix3/mrtrix3) | 115/121 (95.0%) |
| [MRTrix3Tissue](https://3tissue.github.io/) | Well tested | [`5.2.8`](https://hub.docker.com/r/brainlife/3tissue) | 1/1 (100% 🎉) |
| [NiftyReg](http://cmictig.cs.ucl.ac.uk/wiki/index.php/NiftyReg) | Experimental | [`1.4.0`](https://hub.docker.com/r/vnmd/niftyreg_1.4.0) | 7/7 (100% 🎉) |
| [dcm2niix](https://github.com/rordenlab/dcm2niix) | Experimental | [`1.0.20240202`](https://hub.docker.com/r/vnmd/dcm2niix_v1.0.20240202) | 1/1 (100% 🎉) |

<!-- END_PACKAGES_TABLE -->

> 📊 **API Coverage Explained**
>
> - Represents the percentage of tool binaries with available NiWrap descriptors
> - Does not indicate descriptor completeness
> - 100% coverage isn't always necessary (e.g., some FSL/AFNI utilities have Python stdlib equivalents)
> - To improve coverage:
>   - Add missing descriptor in `descriptors/`
>   - Mark irrelevant binaries as `"status": "ignore"` in `packages/`

## 🗂 Repository Structure

```
niwrap/
├── descriptors/    # Boutiques descriptors
├── schemas/        # JSON schema for Boutiques descriptors
├── python/         # Generated niwrap Python package
├── extraction/     # Source metadata extraction
└── packages/       # Package-specific metadata
```

## 🐍 [Python Package](https://github.com/styx-api/niwrap/blob/main/python/README.md)

Install the `niwrap` Python package to use the generated wrappers:

```bash
pip install niwrap
```

See the [NiWrap Python package readme](https://github.com/styx-api/niwrap/blob/main/python/README.md) for more details.

## 🤝 Contributing

Contributions are welcome! See [CONTRIBUTING.md](./CONTRIBUTING.md) for ways to get started.

## 📄 License

The NiWrap project itself, including all metadata and generated Python wrappers, is licensed under the MIT License. See the LICENSE file for details.

> **⚠️ Important**: The neuroimaging tools wrapped by NiWrap each have their own licenses. Using NiWrap does not grant any rights to use these tools beyond what their respective licenses allow. Users are responsible for complying with the licenses of the underlying tools they use through NiWrap.

## 🙋‍♀️ Support

For support, please open an issue in the [GitHub issue tracker](https://github.com/styx-api/niwrap/issues).
