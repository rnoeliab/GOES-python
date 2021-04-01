#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 13:13:08 2021

@author: noelia
"""
# GNC-A Blog GOES-16 Python Tutorial: Part II
 
# Required libraries
import matplotlib.pyplot as plt # Import the Matplotlib package
from netCDF4 import Dataset # Import the NetCDF Python interface
from mpl_toolkits.basemap import Basemap # Import the Basemap toolkit
import numpy as np # Import the Numpy package
 
# Path to the GOES-R simulated image file
path = '/home/noelia/input/OR_ABI-L2-CMIPF-M6C07_G16_s20192311230197_e20192311239516_c20192311239586.nc'
output = '/home/noelia/output/'
# Open the file using the NetCDF4 library
nc = Dataset(path)
 
# Extract the Brightness Temperature values from the NetCDF
data = nc.variables['CMI'][:] 
 
# Create the basemap reference for the Satellite Projection
bmap = Basemap(projection='geos', lon_0=-89.5, lat_0=0.0, satellite_height=35786023.0, ellps='GRS80')
 
# Plot GOES-16 Channel using 170 and 378 as the temperature thresholds
bmap.imshow(data, origin='upper', vmin=170, vmax=410, cmap='Greys')
 
# Draw the coastlines, countries, parallels and meridians
bmap.drawcoastlines(linewidth=0.3, linestyle='solid', color='black')
bmap.drawcountries(linewidth=0.3, linestyle='solid', color='black')
bmap.drawparallels(np.arange(-90.0, 90.0, 10.0), linewidth=0.1, color='white')
bmap.drawmeridians(np.arange(0.0, 360.0, 10.0), linewidth=0.1, color='white')
 
# Insert the legend
bmap.colorbar(location='bottom', label='Brightness Temperature [K]')
 
# Export result
DPI = 300
plt.savefig(output + 'GOES-16_Ch13br.png', dpi=DPI, bbox_inches='tight', pad_inches=0)
 
# Show the plot
plt.show()
