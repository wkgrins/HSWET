# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 14:51:33 2021

@author: Willa Grinsfelder, Fabrice Ingabire
"""
# Import relevant modules
import pandas as pd
import numpy as np
#matplotlib
#pandas?
#math

# Import logged data from .csv file format as a Pandas dataframe
# obj = pd.read_excel("test.xlsx", index_col='Tim elapsed (ms)')


# Import Manually Logged Wind Tunnel Data and time stamps
# vals = pd.read_excel("test_speeds.xlsx")

# Calculate wind speed from motor RPMS
# Eq'n: Wind speed (m/s) = 0.0021*motor rpms + 0.3346

# Section obj into time intervals corresponding to time intervals logged in vals
# Remove any data collected outside of the desired time intervals
obj.iloc[vals.iloc[1,[1]]]

# Add a new column to the obj data with wind speed corresponding to correct time intervals from vals data

# Make a directory named after the test data

# Write the munged data to a file called munged.csv with commas as data delimiters

#### Anything past here is future additions
# Plot raw data and save the images to the directory
# Make sub-directory called "raw"

# Plot TSR with wind speed (three lines for different pitch combinations)

# Plot Power with wind speed (three lines for different pitch combinations)

# Plot generator voltage vs rpms

# Clean outliers from the data 

# Make plots of the cleaned data in the same directory

# Plot TSR with wind speed (three lines for different pitch combinations)

# Plot Power with wind speed (three lines for different pitch combinations)

# Plot generator voltage vs rpms

# Write cleaned data results to a .txt file in the directory

# Place original loaded data in the directory named after the test data

