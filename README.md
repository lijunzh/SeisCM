# Seismic ColorMap

[![Build Status](https://travis-ci.org/gatechzhu/SeisCM.svg?branch=master)](https://travis-ci.org/gatechzhu/SeisCM)

## Introduction
As geophysicists can never agree on a standard colormap to plot seismic datasets that make every one happy, I try to make a package that include most common colormaps so that I can call them simply by import a package. 
This package is designed to be minimal initially and try to include as manny cm as possible. 
Open a pull request for any new colormap that you want me to include and I will put it in the package as soon as possible.
 
## List of Available Colormaps
- Blue-White-Red 
- Seismic
- Phase
- Frequency
 
 
![Colormap Demo](/fig/colormaps.png?raw=true "Colormaps")
 

## Dependancy
- [NumPy](http://www.numpy.org/)
- [Matplotlib](http://matplotlib.org/)

## Usage
For a given $CM (replace $CM by the actual colormap that you want to use), you can use it as following:
```
from seiscm import $CM 
import matplotlib.pyplot as plt

plt.imshow(img, cmap=$CM())

```
 
## Installation

### From PyPI
```
pip install seiscm
```

### From source file
Download srouce file from [releases page](https://github.com/gatechzhu/SeisCM/releases). Under the root directory, type:

```
python setup.py install
```


## Contact

In counter of any trouble, contact *gatechzhu@gmail.com*
