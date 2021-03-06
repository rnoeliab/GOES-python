# GOES-python
This repository is to process GOES images with python

Before starting to use this repository, you must have Anaconda3 and python 3.6 or higher installed. If in case you do not have it installed, click on the following link: [Installing Anaconda](https://github.com/rnoeliab/Installing_anaconda)

## Products Available
![Alt text](https://github.com/rnoeliab/GOES-python/blob/main/products_available.png)

## Download GOES data 
* [GOES-16/17 on Amazon Download Page](https://home.chpc.utah.edu/~u0553130/Brian_Blaylock/cgi-bin/goes16_download.cgi)
* [GOES-R Series Dataset](https://www.ncdc.noaa.gov/airs-web/search)
* [gcp-public-data-goes-16](https://console.cloud.google.com/storage/browser/gcp-public-data-goes-16?pageState=(%22StorageObjectListTable%22:(%22f%22:%22%255B%255D%22))&prefix=&forceOnObjectsSortingFiltering=false)

## GEONETClass: Manipulating GOES-16 Data With Python – Part I

*  To learn how to manipulate GOES data with python we are going to re-do the examples on this web page: [goes part I](https://geonetcast.wordpress.com/2017/04/27/geonetclass-manipulating-goes-16-data-with-python-part-i/)
* In this class we are only going to teach you to read an image goes [read_data.py](https://github.com/rnoeliab/GOES-python/blob/main/SST/1.read_data.py) in a very simple way and using the library "from netCDF4 import Dataset".
```
 conda install -c anaconda netcdf4 
```

## GEONETClass: Manipulating GOES-16 Data With Python – Part II

* Here we are going to manipulate the basemap library a bit, learn to represent a variable spatially. 
* Add a type of projection, contour of countries, states, meridians, parallels, add the colorbar, the levels of the palette and finally save the image [read_save.py](https://github.com/rnoeliab/GOES-python/blob/main/SST/2.read_save.py). 

```
  conda install -c anaconda basemap 
```
## GEONETClass: Manipulating GOES-16 Data With Python – Part III

Today, we’ll learn two things (read [3.extract_header.py](https://github.com/rnoeliab/GOES-python/blob/main/SST/3.extract_header.py)):

1-) How to extract the GOES-16 Band Number, the Start and the End of the Scan times based on the file name.

2-) How to read the GOES-16 NetCDF file header in order to retrieve information about the image.

## GEONETClass: Manipulating GOES-16 Data With Python – Part IV

Here, we can modify the basemap from the previous exercise ([3.extract_header.py](https://github.com/rnoeliab/GOES-python/blob/main/SST/3.extract_header.py)) to generate different maps:
* Add a type of background on the map and a transparency "alpha=0.5" (50%).
```python
# Add a Blue Marble background
bmap.bluemarble()
# Plot GOES-16 channel with transparency
bmap.imshow(data, origin='upper', vmin=170, vmax=378, cmap='Greys', alpha=0.5)
```
* Modifying the map background 
```python
# Add an ocean mask
bmap.shadedrelief() 
bmap.etopo()
```
* Add an ocean mask
```python
# Add an ocean mask
bmap.drawlsmask(ocean_color='aqua',lakes=True)
```
## GEONETClass: Manipulating GOES-16 Data With Python – Part V

In this chapter we are going to implement a vector "shapefile (shp)" in the basemap to visualize the divisions of the states of a specific country. [Brazilian_States_Shape](https://www.dropbox.com/s/8o5gfpl3jj2efib/Brazilian_States_Shape.zip?raw=1).
* Download the "shp" indicated above and check the directory path.
* Before running the [5.add_shp_cmap.py](https://github.com/rnoeliab/GOES-python/blob/main/SST/5.add_shp_cmap.py) script we will first run the [cpt_convert.py](https://github.com/rnoeliab/GOES-python/blob/main/SST/cpt_convert.py) script (Figure: [5.add_shp_cmap.png](https://github.com/rnoeliab/GOES-python/blob/main/Figures/5.add_shp_cmap.png)). 
* The [cpt_convert.py](https://github.com/rnoeliab/GOES-python/blob/main/SST/cpt_convert.py) script must be in the same directory as the [4.add_shp.py](https://github.com/rnoeliab/GOES-python/blob/main/SST/4.add_shp.py) script: 
```
python cpt_convert.py
```
* Then, from [3.extract_header.py] script, we are going to add several lines: 
```python
#add libraries
from cpt_convert import loadCPT # Import the CPT convert function
from matplotlib.colors import LinearSegmentedColormap # Linear interpolation for color maps
```
* After the line "bmap = Basemap(projection='geos', lon_0=-75.5, lat_0=0.0, satellite_height=35786023.0, ellps='GRS80')"
```python
# Converts the CPT file to be used in Python
cpt = loadCPT('/home/noelia/Documents/goes/tutorial/G16_SSTF/IR4AVHRR6.cpt')
# Makes a linear interpolation with the CPT file
cpt_convert = LinearSegmentedColormap('cpt', cpt)

# Plot the GOES-16 channel with the converted CPT colors
trend = bmap.imshow(data, origin='upper', vmin=170, vmax=378, cmap=cpt_convert)
```
* After the line "bmap.drawmeridians(np.arange(0.0, 360.0, 10.0), linewidth=0.3, color='white')": 
```python
bmap.readshapefile('/home/noelia/input/Brazilian_States_Shape/BRA_adm1','BRA_adm1',linewidth=0.3,color='black')
```
* There are other color palettes to show: [5.1.add_shp_cmap_temp.py](https://github.com/rnoeliab/GOES-python/blob/main/SST/5.1.add_shp_cmap_temp.py) and [5.2.add_shp_cmap_vapor.py](https://github.com/rnoeliab/GOES-python/blob/main/SST/5.2.add_shp_cmap_vapor.py)

## GEONETClass: Manipulating GOES-16 Data With Python – Part VI

* Here, we will learn how to reproject and image to the rectangular projection. Also we are going to choose the region that we want to visualize.
* We need some files: [cpt_convert.py](https://github.com/rnoeliab/GOES-python/blob/main/SST/cpt_convert.py), [IR4AVHRR6.cpt](https://github.com/rnoeliab/GOES-python/blob/main/SST/IR4AVHRR6.cpt), [remap.py](https://github.com/rnoeliab/GOES-python/blob/main/SST/remap.py) and [6.rectangular_projection.py](https://github.com/rnoeliab/GOES-python/blob/main/SST/6.rectangular_projection.py).
* First, we need to run `cpt_covert.py`, then `remap.py` and finally `6.rectangular_projection.py`.
* In the last script, we can change the `extent` by other latitudes and longitudes. This depends on the area of our interest.

![Alt text](https://github.com/rnoeliab/GOES-python/blob/main/Figures/6.rectangular_projection.png)











