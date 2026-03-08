"""Tests for seiscm colormaps."""

import matplotlib.pyplot as plt
import pytest
from matplotlib.colors import LinearSegmentedColormap

from seiscm import bwr, frequency, phase, seismic


@pytest.fixture(autouse=True)
def _close_figures():
    """Close all matplotlib figures after each test to prevent leaks."""
    yield
    plt.close("all")


class TestBwr:
    """Tests for the Blue-White-Red colormap."""

    def test_returns_colormap(self):
        assert isinstance(bwr(), LinearSegmentedColormap)

    def test_default_alpha_zero(self):
        cmap = bwr()
        # Middle of the map should be fully transparent (alpha=0)
        assert cmap(0.5)[3] == pytest.approx(0.0, abs=0.01)

    def test_custom_alpha(self):
        cmap = bwr(alpha=0.5)
        assert cmap(0.5)[3] == pytest.approx(0.5, abs=0.01)

    def test_rejects_alpha_below_zero(self):
        with pytest.raises(ValueError, match="between 0 and 1"):
            bwr(-0.1)

    def test_rejects_alpha_above_one(self):
        with pytest.raises(ValueError, match="between 0 and 1"):
            bwr(1.1)

    def test_edge_colours(self):
        cmap = bwr()
        r0, _g0, b0, _ = cmap(0.0)
        r1, _g1, b1, _ = cmap(1.0)
        # Left end should be blue-ish, right end red-ish
        assert b0 > r0
        assert r1 > b1


class TestSeismic:
    """Tests for the seismic colormap."""

    def test_returns_colormap(self):
        assert isinstance(seismic(), LinearSegmentedColormap)

    def test_name(self):
        assert seismic().name == "Seismic"


class TestPhase:
    """Tests for the phase colormap."""

    def test_returns_colormap(self):
        assert isinstance(phase(), LinearSegmentedColormap)

    def test_name(self):
        assert phase().name == "Phase"


class TestFrequency:
    """Tests for the frequency colormap."""

    def test_returns_colormap(self):
        assert isinstance(frequency(), LinearSegmentedColormap)

    def test_name(self):
        assert frequency().name == "Frequency"
