Multi-Energy System Py (MES-Py)
========================

### Description

The Multi-Energy System Py (MES-Py) model main objective is to provide an open-source alternative to the problem of sizing and dispatch of energy in multi-energy systems in isolated places. It’s written in python(pyomo) and use excel and text files as input and output data handling and visualization. It is an expansion of the existing Micro-Grids Py library, developed by S.Balderrama and S.Quoilin.

Main features:

    Optimal sizing of: a) Lion-Ion batteries, diesel generators and PV panels; and b) hot water tanks, solar thermal collectors and LPG boilers in order to supply a single-node electricity demand and a multi-node thermal demand with the lowest cost possible.
    Optimal dispatch from different energy sources.
    Calculation of the net present cost of the system for the project lifetime.
    Determination of the LCOE for the optimal system.


### Main developers

Nicolò Stevanato <br/>
Politecnico di Milano, Milan <br/>
E-mail: nicolo.stevanato@polimi.it <br/>

Lorenzo Rinaldi <br/>
Politecnico di Milano, Milan <br/>
E-mail: lorenzo.rinaldi@polimi.it

Stefano Pistolese <br/>
Politecnico di Milano, Milan <br/>

Francesco Lombardi <br/>
Politecnico di Milano, Milan <br/>

Sergio Balderrana <br/>
University of Liege, Belgium - Universidad Mayor de San Simon, Bolivia <br/>

Sylvain Quoilin <br/>
University of Liege, Belgium. <br/>
 
### Required libraries

The python libraries needed to run Micro-Grids are the following:

    -Pyomo Optimization object library, interface to LP solver (e.g. CPLEX)
    -Pandas for input and result data handling
    -Matplotlib for plotting


### Licence
This is a free software licensed under the “European Union Public Licence" EUPL v1.1. It 
can be redistributed and/or modified under the terms of this license.

### Getting started

To start using the MES-Py library please Go to Documentation/_build/html and double click in the archive index.html. This will open a Documention in html format. Please read carefully the tutorial part of this documentation in order to understand how to setup and use MES-Py library.

