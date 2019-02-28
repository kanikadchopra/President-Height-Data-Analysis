# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 10:49:19 2019

@author: 321758898
"""

# US President Heights Data
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn; seaborn.set() #set plot style

data = pd.read_csv('president_heights.csv')
heights = np.array(data['height(cm)'])

# Summary Statistics
print("Mean height:       ", heights.mean())
print("Standard deviation:      ", heights.std())
print("Minimum height:     ", heights.min())
print("Maximum height:     ", heights.max())

# Quantiles
print("25th percentile:    ", np.percentile(heights,25))
print("Median:     ", np.percentile(heights, 50))
print("75th percentile:     ", np.percentile(heights, 50))

# Creating a histogram with the data
plt.hist(heights)
plt.title('Heights Distribution of US Presidents')
plt.xlabel('height (cm)')
plt.ylabel('number');
