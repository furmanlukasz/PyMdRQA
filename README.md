# PyMdRQA

PyMdRQA is a Python implementation of Multidimensional Recurrence Quantification Analysis (MdRQA), a technique used for analyzing the behavior of multivariate time series data. This implementation is designed to work efficiently with large datasets, such as those typically found in neuroscience (e.g., fMRI time series data).

## Installation

Before you can use PyMdRQA, you need to ensure that you have Python installed on your system. The code is tested with Python 3.8 and above.

You will also need to install the following Python packages:

- numpy
- scipy
- pyrqa

You can install these packages using pip:

```
pip install numpy scipy pyrqa
```

Next clone the repository and install the package using pip:

```
git clone https://github.com/furmanlukasz/PyMdRQA.git
cd PyMdRQA
pip install .
```

## Usage

To use PyMdRQA, you can import the function `mdrqa` from the module and pass your time series data to it as a NumPy array. Here's a simple example:

```python
import numpy as np
from pymdrqa import mdrqa

# Example time series data
data = np.random.rand(100, 3)  # 100 data points in each of the 3 time series

# Run MdRQA
results, recurrence_matrix = mdrqa(data, emb=2, delay=1, norm='euc', radius=0.1)

# Print the results
print(results)
```

The `mdrqa` function returns a dictionary containing various RQA measures and a binary matrix representing the recurrence plot.

## Parameters

The `mdrqa` function accepts the following parameters:

- `data`: A NumPy array where each column is a time series.
- `emb`: The embedding dimension (default is 1).
- `delay`: The delay for embedding (default is 1).
- `norm`: The normalization method. Options are 'euc' for Euclidean, 'min', 'max', or 'non' (default is 'non').
- `radius`: The radius for fixed neighbourhood (default is 1).

## Citation

If you use PyMdRQA in your research, please cite the following papers:

- Rawald, T., Sips, M., Marwan, N. (2017): PyRQA – Conducting Recurrence Quantification Analysis on Very Long Time Series Efficiently, Computers & Geosciences, 104, 101–108. DOI:10.1016/j.cageo.2016.11.016

- Wallot, S. & Leonardi, G. Analyzing Multivariate Dynamics Using Cross-Recurrence Quantification Analysis (CRQA), Diagonal-Cross-Recurrence Profiles (DCRP), and Multidimensional Recurrence Quantification Analysis (MdRQA) – A Tutorial in R. Front. Psychol. 9, 2232 (2018).

Additionally, the original Matlab and R implementation can be found at:
https://github.com/Wallot/MdRQA

## License

This project is licensed under the GNU General Public License v2.0 - see the LICENSE file for details.

The GNU General Public License (GPL-2.0) is a free, copyleft license for software and other kinds of works, providing the freedom to use, study, redistribute, and modify the work. This project's adoption of the GPL-2.0 requires that any modifications to it or derivative works based on it are also distributed under the same license.

For more information on the GPL-2.0 license, visit [GNU General Public License v2.0](https://www.gnu.org/licenses/old-licenses/gpl-2.0.en.html).
