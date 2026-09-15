# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 12:39:07 2026

@author: evafa
"""
import matplotlib.pyplot as plt
import math
import numpy as np

# parameters
n = 1.81e-5                                 # kg/(m*s)
p = 1.225                                   # kg/m^3
c_d = 0.47                                  # sphere
m = 0.145                                   # kg
r = 3.7e-2                                  # m 
g = -9.8                                    # m/s^2

c1 = 6*math.pi*n*r
c2 = 1/2*math.pi*p*c_d*r**2

# define domain
a = 0
b = 10
N = 10                                     # number of segments
h = (b-a)/N
T = np.arange(a, b, h)                      # domain


lin = 0
quad = 1

def F(t ,v):
    return g - lin*c1/m*v - quad*c2/m*v**2

def Y(t ,v):
    k1 = h * F(t, v)
    k2 = h * F(t + h/2, v+(k1/2))
    k3 = h * F(t + h/2, v+(k2/2))
    k4 = h * F(t + h, v+k3)
    vf = 1/6*(k1 + 2*k2 + 2*k3 + k4)
    print(k1, k2, k3, k4)
    return vf

v=0
V=[v]

print(1/(c2/c1*r*2))

if 1/(c2/c1*r*2) > 1:
    for i in range(0, N): 
        t = T[i]
        vi = V[i]
        lin, quad = 1, 0
        vf = Y(t, vi)
        V = np.append(V, vf)
else: 
    for i in range(0, N): 
        t = T[i]
        vi = V[i]
        lin, quad = 0, 1
        vf = Y(t, vi)
        V = np.append(V, vf)

fig1 = plt.figure()
plt.plot(T, V[0:N])
plt.show()



