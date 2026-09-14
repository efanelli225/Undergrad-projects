# -*- coding: utf-8 -*-
"""
Title: Code Assignment 2
Author: Eva Fanelli
Date: 08/31/2026

"""
import math
import matplotlib.pyplot as plt


y = 20          # m 
x = 0           # m
v_0 = 10        # m/s
angle = -30     # degrees
dt = 0.001      # seconds
t = 0           # seconds
vx1 = v_0 * math.cos(math.radians(angle))
vy1 = v_0 * math.sin(math.radians(angle))

Y = [y]
X = [x]
T = [t]
Vy = [vy1]


while y > 0:
    vx2 = vx1
    vy2 = vy1 - 9.8 * dt
    dx = vx2 * dt
    dy = vy2 * dt - 1/2 * (9.8) * dt**2
    x += dx
    y += dy
    t += dt
    X.append(x)
    Y.append(y)
    Vy.append(vy2)
    T.append(t)
    vy1 = vy2

# plots
fig1 = plt.figure()
plt.plot(X, Y, linewidth=1)
plt.title('Position of da ball')
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.grid(True)

fig2 = plt.figure()
plt.plot(T, Vy, linewidth=1)
plt.title('How fast da ball be moving (in y-dir)')
plt.xlabel('time (s)')
plt.ylabel('velocity (m/s)')
plt.ylim(-21, 0)
plt.grid(True)

plt.show()












