#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 13:13:08 2021

@author: noelia
"""

# GNC-A Blog Python Tutorial: Part V
 
# Required libraries
import matplotlib.pyplot as plt # Import the Matplotlib package
from netCDF4 import Dataset # Import the NetCDF Python interface
from mpl_toolkits.basemap import Basemap # Import the Basemap toolkit
import numpy as np # Import the Numpy package

from cpt_convert import loadCPT # Import the CPT convert function
from matplotlib.colors import LinearSegmentedColormap # Linear interpolation for color maps

 
# Path to the GOES-R simulated image file
diretory = '/home/noelia/input/'
path = 'OR_ABI-L2-CMIPF-M6C09_G16_s20192311230197_e20192311239511_c20192311240005.nc'
output = '/home/noelia/output/'

# Search for the GOES-R channel in the file name
Band = (path[path.find("M6C")+3:path.find("_G16")])
# Search for the Scan start in the file name
Start = (path[path.find("s")+1:path.find("_e")])
Start_Formatted = Start[0:4] + " Day " + Start[4:7] + " - " + Start [7:9] + ":" + Start [9:11] + ":" + Start [11:13] + "." + Start [13:14] + " UTC"
# Search for the Scan end in the file name
End = (path[path.find("e")+1:path.find("_c")])
End_Formatted = End[0:4] + " Day " + End[4:7] + " - " + End [7:9] + ":" + End [9:11] + ":" + End [11:13] + "." + End [13:14] + " UTC"
 
# Open the file using the NetCDF4 library
nc = Dataset(diretory + path)
 
# Extract the Brightness Temperature values from the NetCDF
data = nc.variables['CMI'][:]

fig = plt.figure(figsize=(15, 11))
ax = fig.add_subplot(111, frame_on=False)
for axis in ['top','bottom','left','right']:
    ax.spines[axis].set_linewidth(3.0)
# Create the basemap reference for the Satellite Projection
bmap = Basemap(projection='geos', lon_0=-75.5, lat_0=0.0, 
               satellite_height=35786023.0, ellps='GRS80')

# Converts the CPT file to be used in Python
cpt = loadCPT('/home/noelia/Documents/goes/tutorial/G16_SSTF/WVCOLOR35.cpt')

# Makes a linear interpolation with the CPT file
cpt_convert = LinearSegmentedColormap('cpt', cpt)

# Plot the GOES-16 channel with the converted CPT colors
trend = bmap.imshow(data, origin='upper', vmin=170, vmax=378, cmap=cpt_convert)
# Plot GOES-16 channel
#trend = bmap.imshow(data, origin='upper', vmin=170, vmax=378, cmap='Greys')

# Draw the coastlines, countries, parallels and meridians
bmap.drawcoastlines(linewidth=0.5, linestyle='solid', color='black')
bmap.drawcountries(linewidth=0.5, linestyle='solid', color='black')
bmap.drawparallels(np.arange(-90.0, 90.0, 10.0), linewidth=0.3, color='white')
bmap.drawmeridians(np.arange(0.0, 360.0, 10.0), linewidth=0.3, color='white')
bmap.readshapefile('/home/noelia/Documents/goes/tutorial/Brazilian_States_Shape/BRA_adm1','BRA_adm1',linewidth=0.3,color='black')

# Insert the legend at the bottom
cbar = bmap.colorbar(trend, location='right', pad="5%")
cbar.set_label('Brightness Temperature [K]', fontsize=19)

# Add a title to the plot
plt.title("GOES-16 ABI Simulated Band " + Band + '\n'+
          "Data: "+  Start_Formatted[0:12]+'\n' ,fontsize=23)
#plt.title("GOES-16 ABI Simulated Band " + Band + "\n Scan from " + Start_Formatted + " to " + End_Formatted)

# Read some variables from the NetCDF header in order to use it in the plot
geo_extent = nc.variables['geospatial_lat_lon_extent']
center = str(geo_extent.geospatial_lon_center)
west = str(geo_extent.geospatial_westbound_longitude)
east = str(geo_extent.geospatial_eastbound_longitude)
north = str(geo_extent.geospatial_northbound_latitude)
south = str(geo_extent.geospatial_southbound_latitude)

# Put the information retrieved from the header in the final image
bbox=dict(facecolor='white', edgecolor='black', boxstyle='round')
texts = ("Observation Start: " + Start_Formatted[-14::] +'\n'+ 
         "Observation End: " + End_Formatted[-14::] +'\n'+ 
         'Geospatial Extent \n' + west + '°W \n' + east + 
         '°E \n' + north + '°N \n' + south + '°S \n' + 
         'Center = ' + center + '°') 
plt.text(-300000,300000, texts, bbox=bbox,fontsize = 15)
 
# Export result
DPI = 300
#plt.savefig(output+'Channel_13_python.png', dpi=DPI, bbox_inches='tight', pad_inches=0)
 
# Show the plot
plt.show()
