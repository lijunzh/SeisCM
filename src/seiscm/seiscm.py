"""Seismic colormaps for geophysical data visualization."""

from __future__ import annotations

from typing import TypeAlias

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap

_Segments: TypeAlias = tuple[tuple[float, float, float], ...]
_CDict: TypeAlias = dict[str, _Segments]


def _make_cmap(name: str, cdict: _CDict) -> LinearSegmentedColormap:
    """Thin wrapper around ``LinearSegmentedColormap`` for DRY construction."""
    return LinearSegmentedColormap(name, cdict)


# ---------------------------------------------------------------------------
# Public colormaps
# ---------------------------------------------------------------------------


def bwr(alpha: float = 0) -> LinearSegmentedColormap:
    """Blue-White-Red colormap with configurable mid-point transparency.

    Parameters
    ----------
    alpha : float
        Transparency at the centre of the map, in ``[0, 1]``.
        ``0`` (default) gives a fully transparent midpoint suitable for
        overlaying seismic amplitudes on other imagery.

    Returns
    -------
    LinearSegmentedColormap
    """
    if not 0 <= alpha <= 1:
        raise ValueError("alpha must be between 0 and 1.")

    cdict: _CDict = {
        "red": (
            (0, 0, 0),
            (0.25, 0, 0),
            (0.5, 1, 1),
            (0.75, 0.8314, 0.8314),
            (1, 0.5, 0.5),
        ),
        "green": (
            (0, 0, 0),
            (0.25, 0.375, 0.375),
            (0.5, 1, 1),
            (0.75, 0.375, 0.375),
            (1, 0, 0),
        ),
        "blue": (
            (0, 0.5, 0.5),
            (0.25, 0.8314, 0.8314),
            (0.5, 1, 1),
            (0.75, 0, 0),
            (1, 0, 0),
        ),
        "alpha": (
            (0, 1, 1),
            (0.5, alpha, alpha),
            (1, 1, 1),
        ),
    }
    return _make_cmap("BlueWhiteRed", cdict)


def seismic() -> LinearSegmentedColormap:
    """Seismic colormap.

    Returns
    -------
    LinearSegmentedColormap
    """
    cdict: _CDict = {
        "red": (
            (0, 0.6314, 0.6314),
            (0.33, 0, 0),
            (0.4, 0.302, 0.302),
            (0.5, 0.8, 0.8),
            (0.6, 0.3804, 0.3804),
            (0.667, 0.749, 0.749),
            (1, 1, 1),
        ),
        "green": (
            (0, 1, 1),
            (0.33, 0, 0),
            (0.4, 0.302, 0.302),
            (0.5, 0.8, 0.8),
            (0.6, 0.2706, 0.2706),
            (0.667, 0, 0),
            (1, 1, 1),
        ),
        "blue": (
            (0, 1, 1),
            (0.33, 0.749, 0.749),
            (0.4, 0.302, 0.302),
            (0.5, 0.8, 0.8),
            (0.6, 0, 0),
            (0.667, 0, 0),
            (1, 0, 0),
        ),
    }
    return _make_cmap("Seismic", cdict)


def phase() -> LinearSegmentedColormap:
    """Phase colormap.

    Returns
    -------
    LinearSegmentedColormap
    """
    cdict: _CDict = {
        "red": (
            (0, 1, 1),
            (0.1, 1, 1),
            (0.2, 1, 1),
            (0.3, 1, 1),
            (0.4, 0.7765, 0.7765),
            (0.5, 0, 0),
            (0.6, 0, 0),
            (0.7, 0, 0),
            (0.8, 0, 0),
            (0.9, 0.6314, 0.6314),
            (1, 1, 1),
        ),
        "green": (
            (0, 0, 0),
            (0.1, 0, 0),
            (0.2, 0.4471, 0.4471),
            (0.3, 0.8941, 0.8941),
            (0.4, 1, 1),
            (0.5, 1, 1),
            (0.6, 1, 1),
            (0.7, 0.8941, 0.8941),
            (0.8, 0.4471, 0.4471),
            (0.9, 0, 0),
            (1, 0, 0),
        ),
        "blue": (
            (0, 1, 1),
            (0.1, 0.6314, 0.6314),
            (0.2, 0, 0),
            (0.3, 0, 0),
            (0.4, 0, 0),
            (0.5, 0, 0),
            (0.6, 0.7765, 0.7765),
            (0.7, 1, 1),
            (0.8, 1, 1),
            (0.9, 1, 1),
            (1, 1, 1),
        ),
    }
    return _make_cmap("Phase", cdict)


def frequency() -> LinearSegmentedColormap:
    """Frequency colormap.

    Returns
    -------
    LinearSegmentedColormap
    """
    cdict: _CDict = {
        "red": (
            (0, 0, 0),
            (0.1, 1, 1),
            (0.2, 1, 1),
            (0.3, 0.9412, 0.9412),
            (0.4, 0.5765, 0.5765),
            (0.5, 0, 0),
            (0.6, 0, 0),
            (0.7, 0, 0),
            (0.8, 0, 0),
            (0.9, 0.6667, 0.6667),
            (1, 1, 1),
        ),
        "green": (
            (0, 0, 0),
            (0.1, 0, 0),
            (0.2, 0.7451, 0.7451),
            (0.3, 1, 1),
            (0.4, 1, 1),
            (0.5, 1, 1),
            (0.6, 1, 1),
            (0.7, 0.8157, 0.8157),
            (0.8, 0.3333, 0.3333),
            (0.9, 0, 0),
            (1, 0, 0),
        ),
        "blue": (
            (0, 0, 0),
            (0.1, 0, 0),
            (0.2, 0, 0),
            (0.3, 0, 0),
            (0.4, 0, 0),
            (0.5, 0.4706, 0.4706),
            (0.6, 0.8824, 0.8824),
            (0.7, 1, 1),
            (0.8, 1, 1),
            (0.9, 1, 1),
            (1, 1, 1),
        ),
    }
    return _make_cmap("Frequency", cdict)


if __name__ == "__main__":
    gradient = np.linspace(0, 1, 256)
    gradient = np.vstack((gradient, gradient))

    fig, axes = plt.subplots(4, 1)
    cmaps = [
        ("bwr", bwr),
        ("seismic", seismic),
        ("phase", phase),
        ("frequency", frequency),
    ]
    for ax, (name, cmap_fn) in zip(axes, cmaps, strict=True):
        ax.imshow(gradient, interpolation="none", aspect="auto", cmap=cmap_fn())
        ax.set_axis_off()
        ax.set_title(name)

    plt.show()
