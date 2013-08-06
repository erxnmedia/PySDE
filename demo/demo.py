# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 16:18:09 2010

@author: -
"""

from __future__ import division
import copy
from sympy import *
from scitools import *
from scitools.StringFunction import StringFunction
from scitools.numpytools import iseq
from scitools.std import *
from copy import copy
from numpy import *
import numpy as np
from time import time
from scitools.easyviz.matplotlib_ import * 

Exnum = 100
M=100
N=100

a=StringFunction('1.')
b=StringFunction('1.')
c=StringFunction('0.')
h=StringFunction('1/(1+x*x)')

nx=M+1
dx=4/float(M)


nt=N+1
dt=1./float(N)
sqrtdt = sqrt(dt)



xmesh = linspace(-2, 2, M+1)
tmesh = linspace(0, 1, N+1)
Ex=np.zeros([N+1,M+1])

"""
sample 1000
vectorization calculation: 0.000061035625
loop calculation: 0.00108408927917
"""
def ICset(Ex,h):
    Ex[0,:]=h(xmesh)
"""
def ICset2(Ex,h):
    for i in arange(0,M+1):
        Ex[0,i]=h(xmesh[i])
"""
#t0=time();
ICset(Ex,h)
#tt=time()-t0
#print tt 
e = np.ones(Exnum,float)
for j in range(0,nx):
    bts = np.zeros(Exnum,float)
    Xts = xmesh[j] *ones(Exnum,float)
    Is  = np.zeros(Exnum,float)
    
    for i in range(1,nt):
        # vectorization calculation
        Ex_u = np.zeros(Exnum,float) 
        db = random.randn(Exnum)*sqrtdt
        Xts += e*a('Xt') * dt + e*b('Xt') * db
        Xt=Xts
  
        Is += e*c(Xt)*dt
        Ex_u[:] += e*h(Xt[:])*exp(Is[:])

        Ex[i,j] = sum(Ex_u)/Exnum
        """
        # Calculation by loop
        Ex[i,j] = 0.0
        for k in range(0, Exnum):
            bt = bts[k]
            Xt = Xts[k]
            Is[k] += 0.#c(Xt)* dt
            Ex[i,j] += h(Xt) * exp(Is[k])
            db = random.randn()*sqrtdt
            bts[k] += db
            Xts[k] += a(Xt)* dt+ b(Xt) * db
        Ex[i,j] /= Exnum
        """
#tt2=time()-t2

"""
array calculation: 0.252888917923
scalar calculation: 20.8320679665
"""
counter = 0
time=counter*dt
for s in range(0,N):
    y = Ex[s,:]
    plot(xmesh,Ex[0,:],xmesh, y, axis=[xmesh[0], xmesh[-1],0.01,1.],
         xlabel='x', ylabel='fk', legend='time=%0.2f' % time,
         hardcopy='tmp_%04d.ps' % counter)
    counter += 1
    time = counter*dt
    #time.sleep(0.2)  # can insert a pause to control movie speed

# make movie file:
movie('tmp_*.ps' ,encoder='convert', fps=10, output_file='a.gif')
