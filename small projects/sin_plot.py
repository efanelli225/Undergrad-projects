# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 19:23:54 2026

@author: evafa
"""

import numpy as np
import matplotlib.pyplot as plt

# create the arrays
x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)

# save to a text file
data = np.column_stack((x, y))
np.savetxt("sine_data.txt", data, delimiter=",")
print("Saved sine_data.txt")

# load the saved file
loaded_data = np.loadtxt("sine_data.txt", delimiter=",")

# plot
x_loaded = loaded_data[:, 0]
y_loaded = loaded_data[:, 1]

plt.plot(x_loaded, y_loaded, label="y=sin(x)")

plt.xlabel("x")
plt.ylabel("y")
plt.title("Sine Function")
plt.grid()
plt.legend()

plt.show()
