# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

FIXELCFESTATS_METADATA = Metadata(
    id="ee3bb73a1251abf2131550881e972d6232152783.boutiques",
    name="fixelcfestats",
    package="mrtrix",
    container_image_tag="mrtrix3/mrtrix3:3.0.4",
)


@dataclasses.dataclass
class FixelcfestatsColumn:
    """
    add a column to the design matrix corresponding to subject fixel-wise values
    (note that the contrast matrix must include an additional column for each
    use of this option); the text file provided via this option should contain a
    file name for each subject.
    """
    path: InputPathType
    """add a column to the design matrix corresponding to subject fixel-wise
    values (note that the contrast matrix must include an additional column for
    each use of this option); the text file provided via this option should
    contain a file name for each subject"""
    
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
        cargs.append("-column")
        cargs.append(execution.input_file(self.path))
        return cargs


@dataclasses.dataclass
class FixelcfestatsConfig:
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


@dataclasses.dataclass
class FixelcfestatsVariousString:
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
class FixelcfestatsVariousFile:
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


class FixelcfestatsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fixelcfestats(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def fixelcfestats(
    in_fixel_directory: InputPathType,
    subjects: InputPathType,
    design: InputPathType,
    contrast: InputPathType,
    connectivity: typing.Union[FixelcfestatsVariousString, FixelcfestatsVariousFile],
    out_fixel_directory: str,
    mask: InputPathType | None = None,
    notest: bool = False,
    errors: str | None = None,
    exchange_within: InputPathType | None = None,
    exchange_whole: InputPathType | None = None,
    strong: bool = False,
    nshuffles: int | None = None,
    permutations: InputPathType | None = None,
    nonstationarity: bool = False,
    skew_nonstationarity: float | None = None,
    nshuffles_nonstationarity: int | None = None,
    permutations_nonstationarity: InputPathType | None = None,
    cfe_dh: float | None = None,
    cfe_e: float | None = None,
    cfe_h: float | None = None,
    cfe_c: float | None = None,
    cfe_legacy: bool = False,
    variance: InputPathType | None = None,
    ftests: InputPathType | None = None,
    fonly: bool = False,
    column: list[FixelcfestatsColumn] | None = None,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[FixelcfestatsConfig] | None = None,
    help_: bool = False,
    version: bool = False,
    runner: Runner | None = None,
) -> FixelcfestatsOutputs:
    """
    Fixel-based analysis using connectivity-based fixel enhancement and
    non-parametric permutation testing.
    
    Unlike previous versions of this command, where a whole-brain tractogram
    file would be provided as input in order to generate the fixel-fixel
    connectivity matrix and smooth fixel data, this version expects to be
    provided with the directory path to a pre-calculated fixel-fixel
    connectivity matrix (likely generated using the MRtrix3 command
    fixelconnectivity), and for the input fixel data to have already been
    smoothed (likely using the MRtrix3 command fixelfilter).
    
    Note that if the -mask option is used, the output fixel directory will still
    contain the same set of fixels as that present in the input fixel template,
    in order to retain fixel correspondence. However a consequence of this is
    that all fixels in the template will be initialy visible when the output
    fixel directory is loaded in mrview. Those fixels outside the processing
    mask will immediately disappear from view as soon as any data-file-based
    fixel colouring or thresholding is applied.
    
    In some software packages, a column of ones is automatically added to the
    GLM design matrix; the purpose of this column is to estimate the "global
    intercept", which is the predicted value of the observed variable if all
    explanatory variables were to be zero. However there are rare situations
    where including such a column would not be appropriate for a particular
    experimental design. Hence, in MRtrix3 statistical inference commands, it is
    up to the user to determine whether or not this column of ones should be
    included in their design matrix, and add it explicitly if necessary. The
    contrast matrix must also reflect the presence of this additional column.
    
    References:
    
    Raffelt, D.; Smith, RE.; Ridgway, GR.; Tournier, JD.; Vaughan, DN.; Rose,
    S.; Henderson, R.; Connelly, A. Connectivity-based fixel enhancement:
    Whole-brain statistical analysis of diffusion MRI measures in the presence
    of crossing fibres.Neuroimage, 2015, 15(117):40-55
    
    * If not using the -cfe_legacy option:
    Smith, RE.; Dimond, D; Vaughan, D.; Parker, D.; Dhollander, T.; Jackson, G.;
    Connelly, A. Intrinsic non-stationarity correction for Fixel-Based Analysis.
    In Proc OHBM 2019 M789
    
    * If using the -nonstationary option:
    Salimi-Khorshidi, G. Smith, S.M. Nichols, T.E. Adjusting the effect of
    nonstationarity in cluster-based and TFCE inference. NeuroImage, 2011,
    54(3), 2006-19.
    
    Author: David Raffelt (david.raffelt@florey.edu.au) and Robert E. Smith
    (robert.smith@florey.edu.au)
    
    URL:
    https://mrtrix.readthedocs.io/en/latest/reference/commands/fixelcfestats.html
    
    Args:
        in_fixel_directory: the fixel directory containing the data files for\
            each subject (after obtaining fixel correspondence.
        subjects: a text file listing the subject identifiers (one per line).\
            This should correspond with the filenames in the fixel directory\
            (including the file extension), and be listed in the same order as the\
            rows of the design matrix.
        design: the design matrix.
        contrast: the contrast matrix, specified as rows of weights.
        connectivity: the fixel-fixel connectivity matrix.
        out_fixel_directory: the output directory where results will be saved.\
            Will be created if it does not exist.
        mask: provide a fixel data file containing a mask of those fixels to be\
            used during processing.
        notest: don't perform statistical inference; only output population\
            statistics (effect size, stdev etc).
        errors: specify nature of errors for shuffling; options are:\
            ee,ise,both (default: ee).
        exchange_within: specify blocks of observations within each of which\
            data may undergo restricted exchange.
        exchange_whole: specify blocks of observations that may be exchanged\
            with one another (for independent and symmetric errors, sign-flipping\
            will occur block-wise).
        strong: use strong familywise error control across multiple hypotheses.
        nshuffles: the number of shuffles (default: 5000).
        permutations: manually define the permutations (relabelling). The input\
            should be a text file defining a m x n matrix, where each relabelling\
            is defined as a column vector of size m, and the number of columns, n,\
            defines the number of permutations. Can be generated with the\
            palm_quickperms function in PALM\
            (http://fsl.fmrib.ox.ac.uk/fsl/fslwiki/PALM). Overrides the -nshuffles\
            option.
        nonstationarity: perform non-stationarity correction.
        skew_nonstationarity: specify the skew parameter for empirical\
            statistic calculation (default for this command is 1).
        nshuffles_nonstationarity: the number of shuffles to use when\
            precomputing the empirical statistic image for non-stationarity\
            correction (default: 5000).
        permutations_nonstationarity: manually define the permutations\
            (relabelling) for computing the emprical statistics for\
            non-stationarity correction. The input should be a text file defining a\
            m x n matrix, where each relabelling is defined as a column vector of\
            size m, and the number of columns, n, defines the number of\
            permutations. Can be generated with the palm_quickperms function in\
            PALM (http://fsl.fmrib.ox.ac.uk/fsl/fslwiki/PALM) Overrides the\
            -nshuffles_nonstationarity option.
        cfe_dh: the height increment used in the cfe integration (default: 0.1).
        cfe_e: cfe extent exponent (default: 2).
        cfe_h: cfe height exponent (default: 3).
        cfe_c: cfe connectivity exponent (default: 0.5).
        cfe_legacy: use the legacy (non-normalised) form of the cfe equation.
        variance: define variance groups for the G-statistic; measurements for\
            which the expected variance is equivalent should contain the same index.
        ftests: perform F-tests; input text file should contain, for each\
            F-test, a row containing ones and zeros, where ones indicate the rows\
            of the contrast matrix to be included in the F-test.
        fonly: only assess F-tests; do not perform statistical inference on\
            entries in the contrast matrix.
        column: add a column to the design matrix corresponding to subject\
            fixel-wise values (note that the contrast matrix must include an\
            additional column for each use of this option); the text file provided\
            via this option should contain a file name for each subject.
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
        NamedTuple of outputs (described in `FixelcfestatsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FIXELCFESTATS_METADATA)
    cargs = []
    cargs.append("fixelcfestats")
    if mask is not None:
        cargs.extend([
            "-mask",
            execution.input_file(mask)
        ])
    if notest:
        cargs.append("-notest")
    if errors is not None:
        cargs.extend([
            "-errors",
            errors
        ])
    if exchange_within is not None:
        cargs.extend([
            "-exchange_within",
            execution.input_file(exchange_within)
        ])
    if exchange_whole is not None:
        cargs.extend([
            "-exchange_whole",
            execution.input_file(exchange_whole)
        ])
    if strong:
        cargs.append("-strong")
    if nshuffles is not None:
        cargs.extend([
            "-nshuffles",
            str(nshuffles)
        ])
    if permutations is not None:
        cargs.extend([
            "-permutations",
            execution.input_file(permutations)
        ])
    if nonstationarity:
        cargs.append("-nonstationarity")
    if skew_nonstationarity is not None:
        cargs.extend([
            "-skew_nonstationarity",
            str(skew_nonstationarity)
        ])
    if nshuffles_nonstationarity is not None:
        cargs.extend([
            "-nshuffles_nonstationarity",
            str(nshuffles_nonstationarity)
        ])
    if permutations_nonstationarity is not None:
        cargs.extend([
            "-permutations_nonstationarity",
            execution.input_file(permutations_nonstationarity)
        ])
    if cfe_dh is not None:
        cargs.extend([
            "-cfe_dh",
            str(cfe_dh)
        ])
    if cfe_e is not None:
        cargs.extend([
            "-cfe_e",
            str(cfe_e)
        ])
    if cfe_h is not None:
        cargs.extend([
            "-cfe_h",
            str(cfe_h)
        ])
    if cfe_c is not None:
        cargs.extend([
            "-cfe_c",
            str(cfe_c)
        ])
    if cfe_legacy:
        cargs.append("-cfe_legacy")
    if variance is not None:
        cargs.extend([
            "-variance",
            execution.input_file(variance)
        ])
    if ftests is not None:
        cargs.extend([
            "-ftests",
            execution.input_file(ftests)
        ])
    if fonly:
        cargs.append("-fonly")
    if column is not None:
        cargs.extend([a for c in [s.run(execution) for s in column] for a in c])
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
    cargs.append(execution.input_file(in_fixel_directory))
    cargs.append(execution.input_file(subjects))
    cargs.append(execution.input_file(design))
    cargs.append(execution.input_file(contrast))
    cargs.extend(connectivity.run(execution))
    cargs.append(out_fixel_directory)
    ret = FixelcfestatsOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "FIXELCFESTATS_METADATA",
    "FixelcfestatsColumn",
    "FixelcfestatsConfig",
    "FixelcfestatsOutputs",
    "FixelcfestatsVariousFile",
    "FixelcfestatsVariousString",
    "fixelcfestats",
]
