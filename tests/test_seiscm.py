import pytest
from matplotlib.colors import LinearSegmentedColormap

from seiscm import bwr, seismic, phase, frequency


class TestBwr():
    def test_alpha_range(self):
        with pytest.raises(ValueError):
            bwr(-1)

    def test_output_type(self):
        assert isinstance(bwr(), LinearSegmentedColormap)


class TestSeismic():
    def test_output_type(self):
        assert isinstance(seismic(), LinearSegmentedColormap)


class TestPhase():
    def test_output_type(self):
        assert isinstance(phase(), LinearSegmentedColormap)


class TestFrequency():
    def test_output_type(self):
        assert isinstance(frequency(), LinearSegmentedColormap)
