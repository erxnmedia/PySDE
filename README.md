#Introduction

**PyS<sup>3</sup>DE** is a solver of stochastic differential equations (SDE) implemented by Python, which both symbolic and numeric schemems are supported.
Numerical solvers include schemes for both with and without jumps.
<br>
<font color="red">PyS<sup>3</sup>DE</font> 
= <div color="red"> Py</div>thon Solver via Sympy + SciPy/NumPy for Stochastic Differential Equations!

##Requirements:

1. Sympy: http://sympy.org
2. Scipy and NumPy: http://www.scipy.org

##Optional:
scitools: http://code.google.com/p/scitools/

##Installation

Copy __init__.py and sde.py into the directory, $Python/site-packages/pysde/

##Note

Althought this module is tested for Python2.6~2.7, it can run for Python3.x by using 2to3 converting the source code. It is also
tested on the notebook() interface of both Sage-5.x and IPython-1.

##DEMO

1. python code: http://diffusion.cgu.edu.tw/ftp/sde (demo.py)
2. TeXmacs with Python plugin: http://diffusion.cgu.edu.tw/ftp/sde (sdedemo.py)
3. TeXmacs with Python plugin: SDE with jumps http://diffusion.cgu.edu.tw/ftp/sde (sdejump.py)
4. Sage notebook(): http://diffusion.cgu.edu.tw/ftp/sde DiffusionJumps.sws, DiffusionJumps-1.sws

##Developer:


chu-ching huang: cchuang2009@gmail.com
