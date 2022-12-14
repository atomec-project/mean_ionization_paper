# Improved calculations of mean ionization states with an average-atom model: supplementary information

This repository contains the supplementary information for the [paper](https://arxiv.org/abs/2203.05863) "Improved calculations of mean ionization states with an average-atom model" (to be published in *Phys. Rev. Research*).

The main file is the `supp_info.ipynb` file. This is a Jupyter notebook which contains computational details about the methods presented in the paper, and all the code required to reproduce the results of this paper.

The notebook can be converted to a formatted `.tex` file using `python raw_to_paper.py`.

## Installation

The packages needed to run the notebook are listed in `requirements.txt`, and can be installed (for example) with `pip install -r requirements.txt`. The notebook has been tested with Python 3.8.

## Data: direct download

Please note: the following steps are only required for the second part of the notebook, which contains the code required to reproduce the results of the paper. If you only want to learn the implementation details and see some examples, i.e. run the first part of the notebook, you can skip the following steps. They require either a large amount of computational resources, or the download of a large (~60 GB) dataset.

There are a large number of SCF calculations in the notebook. It is not feasible to run these on a personal computer, an HPC system is required. Therefore the notebook is by default set up not to run these calculations, though the code is provided for those who want to. 

Instead, the SCF results can be downloaded from this [link](https://rodare.hzdr.de/record/1999), and should be unpacked into the root directory of the repository. On a unix system you can run the following commands in your terminal:

```sh
$ wget https://rodare.hzdr.de/record/1999/files/SCF_results.tar
$ tar -xvf SCF_results.tar
```

This will create a `results/` directory, which contains a separate `README.md` file detailing the structure of this directory.

## References

If you use this notebook in your research, please cite the associated paper [1] and the atoMEC code [2].

1. T.J. Callow, E. Kraisler, and A. Cangi. "Improved calculations of mean ionization states with an average-atom model", arXiv pre-print (2022).
2. T. J. Callow, D. Kotik, E. Kraisler, and A. Cangi, "atoMEC: An open-source average-atom Python code", _Proceedings of the 21st Python in Science Conference_, edited by Meghann Agarwal, Chris Calloway, Dillon Niederhut, and David Shupe (2022), pp. 37-45.
