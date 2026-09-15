# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 19:22:44 2026

@author: evafa
"""

import numpy as np
import matplotlib.pyplot as plt

# Prompt user for filename
filename = input("Enter the data file name: ")

try:
    # Load the file
    data = np.loadtxt(filename, delimiter=",", skiprows=1)

    # print shape and first three data points
    print("Data shape:", data.shape)
    print("First three data points:")
    print(data[:3])
    
    # 
    x = data[:, 0]
    y = data[:, 1]

    # Plot the data
    plt.plot(x, y, 'r', marker="o", label="HIV Data")
    plt.xlabel("Year")
    plt.ylabel("Infected Population")
    plt.title("HIV Viral Load Over Time")
    plt.legend()

    # save
    plt.savefig("HIVplot.pdf")

    # Show the plot
    plt.show()

except FileNotFoundError:
    print("Error: The file was not found. Please try again.")
except Exception as e:
    print("An error occurred while loading the file:", e)
