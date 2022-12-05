This directory contains the following types of file:

1. `MIS_*.csv`: Mean ionization state (MIS) results, sorted by material and method. The methods are `thresh` for threshold, `count` for counting, `ELF` for the electron localization function, and `kg` for Kubo-Greenwood.
2. `*.log`: Log files from atoMEC SCF calculations, sorted by material, boundary condition, and temperature or density.
3. `*_dens_*.pkl`: Pickle files containg the `staticKS.Density` object from atoMEC SCF calculations,  sorted by material, boundary condition, and temperature or density.
4. `*_orbs_*.pkl`: Pickle files containing the `staticKS.Orbitals` object from atoMEC SCF calculations, sorted by material, boundary condition, and temperature or density.
