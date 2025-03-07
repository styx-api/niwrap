from styxdefs import *  # Reexport styxdefs
from styxdocker import DockerRunner
from styxsingularity import SingularityRunner
from styxgraph import GraphRunner


def use_local(*args, **kwargs):
    """Set the LocalRunner as the global runner."""
    set_global_runner(LocalRunner(*args, **kwargs))


def use_dry(*args, **kwargs):
    """Set the DryRunner as the global runner."""
    set_global_runner(DryRunner(*args, **kwargs))


def use_docker(*args, **kwargs):
    """Set the DockerRunner as the global runner."""
    set_global_runner(DockerRunner(*args, **kwargs))


def use_singularity(*args, **kwargs):
    """Set the SingularityRunner as the global runner."""
    set_global_runner(SingularityRunner(*args, **kwargs))


def use_graph(*args, **kwargs):
    """Set the GraphRunner as the global runner."""
    set_global_runner(GraphRunner(*args, **kwargs))
