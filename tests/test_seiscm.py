import pytest

from seiscm import bwr
from matplotlib.colors import LinearSegmentedColormap


class TestBwr():
    def test_alpha_range(self):
        with pytest.raises(ValueError):
            bwr(-1)

    def test_output_type(self):
        assert isinstance(bwr(), LinearSegmentedColormap)
