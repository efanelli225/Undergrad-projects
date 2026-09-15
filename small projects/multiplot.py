# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 19:39:06 2026

@author: evafa
"""

import numpy as np
import matplotlib.pyplot as plt

# functions
x = np.linspace(2, 7, 400)
y1 = np.exp(x)
y2 = x**6

# 1x3 subplot layout
fig, axes = plt.subplots(1, 3, figsize=(15, 4))

# linear plot
axes[0].plot(x, y1, label="f(x)=exp(x)")
axes[0].plot(x, y2, label="g(x)=x^6")
axes[0].set_title("Linear Plot")
axes[0].set_xlabel("x")
axes[0].set_ylabel("f(x), g(x)")
axes[0].legend()
axes[0].grid(True)

# semilog y-axis plot
axes[1].semilogy(x, y1, label="f(x)=exp(x)")
axes[1].semilogy(x, y2, label="g(x)=x^6")
axes[1].set_title("Semilog Plot (log y-axis)")
axes[1].set_xlabel("x")
axes[1].set_ylabel("log(y)")
axes[1].legend()
axes[1].grid(True)

# log-log plot
axes[2].loglog(x, y1, label="f(x)=exp(x)")
axes[2].loglog(x, y2, label="g(x)=x^6")
axes[2].set_title("Log-Log Plot")
axes[2].set_xlabel("log(x)")
axes[2].set_ylabel("log(y)")
axes[2].legend()
axes[2].grid(True)

plt.tight_layout()
plt.show()
