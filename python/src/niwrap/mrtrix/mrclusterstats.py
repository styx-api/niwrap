# This file was auto generated by styx
# Do not edit this file directly

import dataclasses
import pathlib
import typing

from styxdefs import *


MRCLUSTERSTATS_METADATA = Metadata(
    id="755682ade8cd53164a332feba7e5eecfcd6d205b",
    name="mrclusterstats",
    container_image_type="docker",
    container_image_tag="mrtrix3/mrtrix3:3.0.4",
)


@dataclasses.dataclass
class MrclusterstatsColumn:
    """
    add a column to the design matrix corresponding to subject voxel-wise values (note that the contrast matrix must include an additional column for each use of this option); the text file provided via this option should contain a file name for each subject
    """
    path: InputPathType
    """add a column to the design matrix corresponding to subject voxel-wise
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
            self: The sub-command object.
            execution: The execution object.
        Returns:
            
        """
        cargs = []
        cargs.append("-column")
        cargs.extend(["", execution.input_file(self.path)])
        return cargs


@dataclasses.dataclass
class MrclusterstatsConfig:
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
            self: The sub-command object.
            execution: The execution object.
        Returns:
            
        """
        cargs = []
        cargs.append("-config")
        cargs.extend(["", self.key])
        cargs.extend(["", self.value])
        return cargs


class MrclusterstatsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mrclusterstats(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def mrclusterstats(
    input_: InputPathType,
    design: InputPathType,
    contrast: InputPathType,
    mask: InputPathType,
    output: str,
    notest: bool = False,
    errors: typing.Literal["spec"] | None = None,
    exchange_within: InputPathType | None = None,
    exchange_whole: InputPathType | None = None,
    strong: bool = False,
    nshuffles: int | None = None,
    permutations: InputPathType | None = None,
    nonstationarity: bool = False,
    skew_nonstationarity: float | int | None = None,
    nshuffles_nonstationarity: int | None = None,
    permutations_nonstationarity: InputPathType | None = None,
    tfce_dh: float | int | None = None,
    tfce_e: float | int | None = None,
    tfce_h: float | int | None = None,
    variance: InputPathType | None = None,
    ftests: InputPathType | None = None,
    fonly: bool = False,
    column: list[MrclusterstatsColumn] = None,
    threshold: float | int | None = None,
    connectivity: bool = False,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[MrclusterstatsConfig] = None,
    help_: bool = False,
    version: bool = False,
    runner: Runner = None,
) -> MrclusterstatsOutputs:
    """
    mrclusterstats by David Raffelt (david.raffelt@florey.edu.au).
    
    Voxel-based analysis using permutation testing and threshold-free cluster
    enhancement.
    
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
    
    * If not using the -threshold command-line option:
    Smith, S. M. & Nichols, T. E. Threshold-free cluster enhancement: Addressing
    problems of smoothing, threshold dependence and localisation in cluster
    inference. NeuroImage, 2009, 44, 83-98
    
    * If using the -nonstationary option:
    Salimi-Khorshidi, G. Smith, S.M. Nichols, T.E. Adjusting the effect of
    nonstationarity in cluster-based and TFCE inference. Neuroimage, 2011,
    54(3), 2006-19.
    
    More information:
    https://mrtrix.readthedocs.io/en/latest/reference/commands/mrclusterstats.html
    
    Args:
        input_: a text file containing the file names of the input images, one
            file per line
        design: the design matrix
        contrast: the contrast matrix
        mask: a mask used to define voxels included in the analysis.
        output: the filename prefix for all output.
        notest: don't perform statistical inference; only output population
            statistics (effect size, stdev etc)
        errors: specify nature of errors for shuffling; options are: ee,ise,both
            (default: ee)
        exchange_within: specify blocks of observations within each of which
            data may undergo restricted exchange
        exchange_whole: specify blocks of observations that may be exchanged
            with one another (for independent and symmetric errors, sign-flipping
            will occur block-wise)
        strong: use strong familywise error control across multiple hypotheses
        nshuffles: the number of shuffles (default: 5000)
        permutations: manually define the permutations (relabelling). The input
            should be a text file defining a m x n matrix, where each relabelling is
            defined as a column vector of size m, and the number of columns, n,
            defines the number of permutations. Can be generated with the
            palm_quickperms function in PALM
            (http://fsl.fmrib.ox.ac.uk/fsl/fslwiki/PALM). Overrides the -nshuffles
            option.
        nonstationarity: perform non-stationarity correction
        skew_nonstationarity: specify the skew parameter for empirical statistic
            calculation (default for this command is 1)
        nshuffles_nonstationarity: the number of shuffles to use when
            precomputing the empirical statistic image for non-stationarity
            correction (default: 5000)
        permutations_nonstationarity: manually define the permutations
            (relabelling) for computing the emprical statistics for non-stationarity
            correction. The input should be a text file defining a m x n matrix,
            where each relabelling is defined as a column vector of size m, and the
            number of columns, n, defines the number of permutations. Can be
            generated with the palm_quickperms function in PALM
            (http://fsl.fmrib.ox.ac.uk/fsl/fslwiki/PALM) Overrides the
            -nshuffles_nonstationarity option.
        tfce_dh: the height increment used in the tfce integration (default:
            0.1)
        tfce_e: tfce extent exponent (default: 0.5)
        tfce_h: tfce height exponent (default: 2)
        variance: define variance groups for the G-statistic; measurements for
            which the expected variance is equivalent should contain the same index
        ftests: perform F-tests; input text file should contain, for each
            F-test, a row containing ones and zeros, where ones indicate the rows of
            the contrast matrix to be included in the F-test.
        fonly: only assess F-tests; do not perform statistical inference on
            entries in the contrast matrix
        column: add a column to the design matrix corresponding to subject
            voxel-wise values (note that the contrast matrix must include an
            additional column for each use of this option); the text file provided
            via this option should contain a file name for each subject
        threshold: the cluster-forming threshold to use for a standard
            cluster-based analysis. This disables TFCE, which is the default
            otherwise.
        connectivity: use 26-voxel-neighbourhood connectivity (Default: 6)
        info: display information messages.
        quiet: do not display information messages or progress status;
            alternatively, this can be achieved by setting the MRTRIX_QUIET
            environment variable to a non-empty string.
        debug: display debugging messages.
        force: force overwrite of output files (caution: using the same file as
            input and output might cause unexpected behaviour).
        nthreads: use this number of threads in multi-threaded applications (set
            to 0 to disable multi-threading).
        config: temporarily set the value of an MRtrix config file entry.
        help_: display this information page and exit.
        version: display version information and exit.
        runner: Command runner
    Returns:
        NamedTuple of outputs (described in `MrclusterstatsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRCLUSTERSTATS_METADATA)
    cargs = []
    cargs.append("mrclusterstats")
    if notest:
        cargs.append("-notest")
    if errors is not None:
        cargs.extend(["-errors", errors])
    if exchange_within is not None:
        cargs.extend(["-exchange_within", execution.input_file(exchange_within)])
    if exchange_whole is not None:
        cargs.extend(["-exchange_whole", execution.input_file(exchange_whole)])
    if strong:
        cargs.append("-strong")
    if nshuffles is not None:
        cargs.extend(["-nshuffles", str(nshuffles)])
    if permutations is not None:
        cargs.extend(["-permutations", execution.input_file(permutations)])
    if nonstationarity:
        cargs.append("-nonstationarity")
    if skew_nonstationarity is not None:
        cargs.extend(["-skew_nonstationarity", str(skew_nonstationarity)])
    if nshuffles_nonstationarity is not None:
        cargs.extend(["-nshuffles_nonstationarity", str(nshuffles_nonstationarity)])
    if permutations_nonstationarity is not None:
        cargs.extend(["-permutations_nonstationarity", execution.input_file(permutations_nonstationarity)])
    if tfce_dh is not None:
        cargs.extend(["-tfce_dh", str(tfce_dh)])
    if tfce_e is not None:
        cargs.extend(["-tfce_e", str(tfce_e)])
    if tfce_h is not None:
        cargs.extend(["-tfce_h", str(tfce_h)])
    if variance is not None:
        cargs.extend(["-variance", execution.input_file(variance)])
    if ftests is not None:
        cargs.extend(["-ftests", execution.input_file(ftests)])
    if fonly:
        cargs.append("-fonly")
    if column is not None:
        cargs.extend([a for c in [s.run(execution) for s in column] for a in c])
    if threshold is not None:
        cargs.extend(["-threshold", str(threshold)])
    if connectivity:
        cargs.append("-connectivity")
    if info:
        cargs.append("-info")
    if quiet:
        cargs.append("-quiet")
    if debug:
        cargs.append("-debug")
    if force:
        cargs.append("-force")
    if nthreads is not None:
        cargs.extend(["-nthreads", str(nthreads)])
    if config is not None:
        cargs.extend([a for c in [s.run(execution) for s in config] for a in c])
    if help_:
        cargs.append("-help")
    if version:
        cargs.append("-version")
    cargs.extend(["", execution.input_file(input_)])
    cargs.extend(["", execution.input_file(design)])
    cargs.extend(["", execution.input_file(contrast)])
    cargs.extend(["", execution.input_file(mask)])
    cargs.extend(["", output])
    ret = MrclusterstatsOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MRCLUSTERSTATS_METADATA",
    "MrclusterstatsColumn",
    "MrclusterstatsConfig",
    "MrclusterstatsOutputs",
    "mrclusterstats",
]
