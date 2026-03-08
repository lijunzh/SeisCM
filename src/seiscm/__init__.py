"""Seismic Colormap Generator."""

__all__ = ["__version__", "bwr", "frequency", "phase", "seismic"]

from ._version import __version__
from .seiscm import bwr, frequency, phase, seismic
