#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 13:13:08 2021

@author: Noelia and Joel Rojas
"""

# GEONETClass: Manipulating GOES-16 Data With Python: Part I

# Required libraries
import matplotlib.pyplot as plt
from netCDF4 import Dataset
 
# Path to the GOES-R simulated image file
path = '/home/acuna/vlab/simulado/OR_ABI-L2-CMIPF-M4C13_G16_s20161811455312_e20161811500135_c20161811500199.nc'
 
# Open the file using the NetCDF4 library
nc = Dataset(path)
 
# Extract the Brightness Temperature values from the NetCDF
data = nc.variables['CMI'][:]
 
# Show data
plt.imshow(data, cmap='Greys')


