#Introduction

**PyS<sup>3</sup>DE** is a solver of stochastic differential equations (SDE) implemented by Python, which both symbolic and numeric schemems are supported.
Numerical solvers include schemes for both with and without jumps.
<br>
**PyS<sup>3</sup>DE** = **Py**thon Solver via **S**ympy + **S**ciPy/NumPy for **S**tochastic **D**ifferential **E**quations!

##Requirements:

1. Sympy: http://sympy.org
2. Scipy and NumPy: http://www.scipy.org

##Optional:
1. <a href="http://code.google.com/p/scitools/">scitools</a><br>
2. <a href="http://matplotlib.org">matplotlib</a>

##Installation

Copy **\_\_init\_\_.py** and **sde.py** into the directory, $Python/site-packages/pysde/

##Note

* Althought this module is tested in Python2.6~2.7, it can also run in Python3.x by using 2to3 converting the source code. It is also
tested on the notebook() interface of both Sage-5.x and IPython-1.
* **PyS<sup>3</sup>DE** also avails the **plot** function, sdeplot, based on *scitools*; but it
only works in python-2.x but not python-3.x since scitools is a python-2.x library. Thanks for Matplotlib
which provides plot functions, capable of doing high-performance pictures.

##DEMO

1. python code: http://diffusion.cgu.edu.tw/ftp/sde (demo.py)
2. TeXmacs with Python plugin: http://diffusion.cgu.edu.tw/ftp/sde (sdedemo.py)
3. TeXmacs with Python plugin: SDE with jumps http://diffusion.cgu.edu.tw/ftp/sde (sdejump.py)
4. Sage notebook(): http://diffusion.cgu.edu.tw/ftp/sde DiffusionJumps.sws, DiffusionJumps-1.sws

##Developer:


chu-ching huang: cchuang2009@gmail.com
