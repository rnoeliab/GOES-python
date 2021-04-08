#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 23:55:47 2021

@author: noelia
"""

#======================================================================================================
# GNC-A Blog Python Tutorial: Part VI
#===================================# Required libraries ==================================================================================
import matplotlib.pyplot as plt # Import the Matplotlib package
from mpl_toolkits.basemap import Basemap # Import the Basemap toolkit&amp;amp;amp;amp;amp;amp;amp;amp;amp;lt;/pre&amp;amp;amp;amp;amp;amp;amp;amp;amp;gt;
import numpy as np # Import the Numpy package
from remap import remap # Import the Remap function

from cpt_convert import loadCPT # Import the CPT convert function
from matplotlib.colors import LinearSegmentedColormap # Linear interpolation for color maps
#======================================================================================================
 
# Load the Data =======================================================================================
# Path to the GOES-16 image file
diretory = '/home/noelia/input/'
path = 'OR_ABI-L2-CMIPF-M6C13_G16_s20192311230197_e20192311239516_c20192311242306.nc'
output = '/home/noelia/output/'
 
# Search for the GOES-16 channel in the file name
Band = (path[path.find("M6C")+3:path.find("_G16")])
# Search for the Scan start in the file name
Start = (path[path.find("_s")+2:path.find("_e")])
Start_Formatted = Start[0:4] + " Day " + Start[4:7] + " - " + Start [7:9] + ":" + Start [9:11] + ":" + Start [11:13] + "." + Start [13:14] + " UTC"
# Search for the Scan end in the file name
End = (path[path.find("_e")+2:path.find("_c")])
End_Formatted = End[0:4] + " Day " + End[4:7] + " - " + End [7:9] + ":" + End [9:11] + ":" + End [11:13] + "." + End [13:14] + " UTC"


# Choose the visualization extent (min lon, min lat, max lon, max lat)
extent = [-90.0, -40.0, -20.0, 10.0]
 
# Choose the image resolution (the higher the number the faster the processing is)
resolution = 2.0
 
# Call the reprojection funcion
grid = remap(diretory+path, extent, resolution, 'HDF5')
 
# Read the data returned by the function
data = grid.ReadAsArray()
#======================================================================================================

fig = plt.figure(figsize=(15, 11))
ax = fig.add_subplot(111, frame_on=False)
for axis in ['top','bottom','left','right']:
    ax.spines[axis].set_linewidth(3.0)
# Create the basemap reference for the Satellite Projection
bmap = Basemap(llcrnrlon=extent[0], llcrnrlat=extent[1], urcrnrlon=extent[2], 
               urcrnrlat=extent[3], epsg=4326)

# Converts the CPT file to be used in Python
cpt = loadCPT('/home/noelia/Documents/goes/tutorial/G16_SSTF/IR4AVHRR6.cpt')

# Makes a linear interpolation with the CPT file
cpt_convert = LinearSegmentedColormap('cpt', cpt)

# Plot the GOES-16 channel with the converted CPT colors
trend = bmap.imshow(data, origin='upper', vmin=170, vmax=378, cmap=cpt_convert)
# Plot GOES-16 channel
#trend = bmap.imshow(data, origin='upper', vmin=170, vmax=378, cmap='Greys')

# Draw the coastlines, countries, parallels and meridians
bmap.drawcoastlines(linewidth=0.5, linestyle='solid', color='black')
bmap.drawcountries(linewidth=0.5, linestyle='solid', color='black')
bmap.drawparallels(np.arange(-90.0, 90.0, 10.0), linewidth=0.3, color='white', labels=[1, 0, 0, 0],fontsize=22)
bmap.drawmeridians(np.arange(0.0, 360.0, 10.0), linewidth=0.3, color='white', labels=[0, 0, 0, 1],fontsize=22)

bmap.readshapefile('/home/noelia/Documents/goes/tutorial/Brazilian_States_Shape/BRA_adm1','BRA_adm1',linewidth=0.3,color='black')

# Insert the legend at the bottom
cbar = bmap.colorbar(trend, location='right', pad="5%")
cbar.set_label('Brightness Temperature [K]', fontsize=19)

# Add a title to the plot
plt.title("GOES-16 ABI Simulated Band " + Band + '\n'+
          "Data: "+  Start_Formatted[0:12]+'\n'+
          "Scan from " + Start_Formatted + " to " + End_Formatted,fontsize=23)
#plt.title("GOES-16 ABI Simulated Band " + Band + "\n Scan from " + Start_Formatted + " to " + End_Formatted)

 
# Export result
DPI = 300
#plt.savefig(output+'Channel_13_python.png', dpi=DPI, bbox_inches='tight', pad_inches=0)
 
# Show the plot
plt.show()
