# -*- coding: utf-8 -*-
"""
Created on Sun Feb 15 12:35:20 2026

@author: evafa
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize

# Discretize the domain with a vector, x
N = 1000
r = np.linspace(0, 15, N) 

#define the parameters
c = 1.5
cb = 1.0
ct = 2.5
V = 10.0
pi = np.pi

#define the function
def f(r):
    return c*2*pi*r + cb*(2*V/r -1/3*pi*r**2) + ct*2*pi*r**2

#define derivative
def fp(r):
    return c*2*pi + cb*((-2)*V/r**2 - 2*pi*r/3) + ct*4*pi*r

#critical point calculator
c_1 = optimize.root_scalar(fp, bracket=(.1, 15), method="brentq")

print('The radius that will minimize the cost given the parameters is',c_1.root,"inches.")