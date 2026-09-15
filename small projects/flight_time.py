# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 14:53:09 2026

@author: evafa

calculates flight time for a projectile given initial conditions
"""

import numpy as np

# initial conditions 1
dt = 0.0001
x0 = 0
y0 = 5.279
v0 = 0
theta0 = -90
m = 0.00251
k = 0.000289

# initial conditions 2
vx = v0 * np.cos(theta0 * np.pi / 180)
vy = v0 * np.sin(theta0 * np.pi / 180)
x = x0
y = y0
t = 0.0

# table header (uncomment if you want a REALLY big table)
# print(f"{'t':>6} {'x':>10} {'y':>10} {'vx':>10} {'vy':>10} {'ax':>10} {'ay':>10} {'v':>10}")
# print("-" * 80)

while True:
    # compute speed
    v = np.sqrt(vx**2 + vy**2)

    # acceleration
    ax = -k/m * v * vx
    ay = -(9.8 + k/m * v * vy)

    # print current state (uncomment if you want a REALLY big table)
    # print(f"{t:6.2f} {x:10.4f} {y:10.4f} {vx:10.4f} {vy:10.4f} {ax:10.4f} {ay:10.4f} {v:10.4f}")

    # update velocity
    vx_new = vx + ax * dt
    vy_new = vy + ay * dt

    # update position
    x = x + vx * dt
    y = y + vy * dt

    # commit velocity update
    vx, vy = vx_new, vy_new

    # stop when projectile hits ground
    if y < 0 and t > 0:
        break

    t += dt


print("total time:",round(t,4))