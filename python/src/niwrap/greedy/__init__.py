"""
Greedy

Greedy is a tool for fast medical image registration. It was developed by Paul
Yushkevich at the Penn Image Computing and Science Lab at the University of
Pennsylvania. The motivation for developing greedy was to have a really fast
CPU-based deformable image registration tool that could be used in applications
where many images have to be registered in parallel - like multi-atlas image
segmentation.

Greedy borrows many concepts (and some implementation strategies) from the
Symmetric Normalization (SyN) in ANTS. But greedy is non-symmetric, which makes
it faster (in applications like multi-atlas segmentation, symmetric property is
not required). Greedy also uses highly optimized code for image metric
computation that adds extra speed.

URL: https://sites.google.com/view/greedyreg/about
"""
# This file was auto generated by Styx.
# Do not edit this file directly.

from .greedy import *
