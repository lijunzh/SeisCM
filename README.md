# Seismic Colormaps (SeisCM)

[![PyPI version](https://img.shields.io/pypi/v/SeisCM)](https://pypi.org/project/SeisCM/)
![License](https://img.shields.io/pypi/l/SeisCM)
![Python versions](https://img.shields.io/pypi/pyversions/SeisCM)
[![CI/CD](https://github.com/lijunzh/seiscm/actions/workflows/cicd.yml/badge.svg)](https://github.com/lijunzh/seiscm/actions/workflows/cicd.yml)

## Introduction

Geophysicists can never agree on a standard colormap — so here's a package
with the most common ones, ready to import. SeisCM provides
[matplotlib](https://matplotlib.org/)-compatible colormaps designed
specifically for seismic and geophysical data visualization.

Pull requests for new colormaps are welcome!

## Available Colormaps

| Name | Description |
|------|-------------|
| `bwr` | Blue-White-Red with configurable mid-point transparency |
| `seismic` | Classic seismic amplitude display |
| `phase` | Phase attribute visualisation |
| `frequency` | Frequency attribute visualisation |

![Colormap Demo](/fig/colormaps.png?raw=true "Colormaps")

## Installation

### From PyPI

```bash
pip install seiscm
```

### From source (development)

```bash
git clone https://github.com/lijunzh/seiscm.git
cd seiscm
uv sync --all-extras --dev
```

## Quick Start

```python
from seiscm import bwr
import matplotlib.pyplot as plt
import numpy as np

data = np.random.default_rng(42).standard_normal((100, 100))
plt.imshow(data, cmap=bwr())
plt.colorbar()
plt.show()
```

## Dependencies

- [NumPy](https://numpy.org/)
- [Matplotlib](https://matplotlib.org/)

## Development

```bash
uv run ruff check src tests   # lint
uv run ruff format src tests  # format
uv run pytest                 # test
uv run pre-commit install     # set up git hooks
```

## Contact

For issues, please open a
[GitHub issue](https://github.com/lijunzh/seiscm/issues) or contact
*gatechzhu@gmail.com*.
