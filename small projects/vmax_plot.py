# -*- coding: utf-8 -*-
"""
Created on Sun Feb 15 11:50:11 2026

@author: evafa
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize

#discretize domain
N = 1000
x = np.linspace(0, 25, N)  

#define the functions
f = lambda x: (x / 6)**(3 / 2)
g = lambda x: (x / 9) * (2 * x / 3)**(1 / 2)
h = lambda x: (x / 6) * (2 * x / 3)**(1/2)

 
plt.figure(1)
plt.plot(x, f(x), 'red', linewidth=3, label='Vmax,a(A)')
plt.plot(x, g(x), 'green', linewidth=3, label='Vmax,b(A)')
plt.plot(x, h(x), 'blue', linewidth=3, label='Vmax,c(A)')
plt.title('Homework 2, Plot 1', fontsize=20)
plt.xlabel('Surface Area', fontsize=15)
plt.ylabel('Volume', fontsize=15)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.grid(True, which='both')
plt.xlim([np.min(x), np.max(x)])
plt.ylim([np.min(f(x)), np.max(f(x))])
plt.legend()

# Save the file 
plt.savefig('P1_HW2_Figure1.eps', format='eps')

#show the plot
plt.show()