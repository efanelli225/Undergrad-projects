# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 12:39:07 2026

@author: evafa
"""
import matplotlib.pyplot as plt
import numpy as np

# parameters
n = 1.81e-5                                 # kg/(m*s)
p = 1.225                                   # kg/m^3
c_d = 0.47                                  # sphere
m = 0.145                                   # kg
r = 3.7e-2                                  # m 
g = 9.8                                    # m/s^2

# drag coefficients
c1 = 6*np.pi*n*r
c2 = 1/2*np.pi*p*c_d*r**2

def F(t ,v):
    return g - (lin*c1/m*v + quad*c2/m*v**2)

def RK(a, b, N, v0):
    h = (b-a)/N
    T = np.zeros(N+1)                       # time array
    V = np.zeros(N+1)                       # velocity array
    T[0] = a                                # initial time
    V[0] = v0                               # initial velocity
    for i in range(0, N):                   # apply R-K method
        t = T[i]
        v = V[i]
        k1 = h * F(t, v)
        k2 = h * F(t + h/2, v+(k1/2))
        k3 = h * F(t + h/2, v+(k2/2))
        k4 = h * F(t + h, v+k3)
        V[i+1] = V[i] + (k1 + 2*k2 + 2*k3 + k4) / 6
        T[i+1] = T[i] + h
    return T, V
    
    
# define domain
a = 0                                       # time start 
b = 20                                      # time end
N = 100                                     # number of steps
v0 = 0                                      # initial velocity

# determine if lin or quad term dominates
if 1/(c2/c1*r*2) > 1:
    lin, quad = 1, 0
else: 
    lin, quad = 0, 1

# solve
T, V = RK(a, b, N, v0)

# plot
fig1 = plt.figure()
plt.plot(T, V)
plt.xlabel("Time (s)")
plt.ylabel("Velocity (m/s)")
plt.title("Vertical velocity of a ball")
plt.grid(True)
plt.legend()
plt.show()



