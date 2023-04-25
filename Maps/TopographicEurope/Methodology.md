# Process
## Getting the Data
- Download DTM from https://sonny.4lima.de.

I chose Europe DTM 3'', it is precise enough for a large scale map. The data comes as tiles in the .hgt format, in their respective CRS.

## Processing
1. Reproject the .hgt files into EPSG:3035 Geotiffs using the script `reproject_tiles`. We need to reproject them into a metric CRS in order to use the hillshade tool later, and it is faster to reproject the tiles than a big merged file.
2. Import the reprojected tiles into QGIS and merge them into a large Geotiff.
3. Replace nodata values with 0, to avoid having ugly straight line boundaries around the edges of the tiles. This works since we have nodata on the sea.
4. Compute a hillshade from the merged DTM. Here we chose multidirectional lighting, and keep the rest as default.
5. Style the DEM to highlight the mid to low elevations, so that the map does not appear flat.
	1. Set the minimum value to 0
	2. Pick a gradient that is darker at high elevations, more saturated at mid elevations, and less saturated (but still colored) at low elevations.
    3. The color map is found in the folder.
8. Style the hillshade to highlight the relief in high-slope areas (mountain ranges).
	1. Set rendering to multiply.
	2. Increase brightness to remove low frequency slopes and reduce gamma to make high frequency details more visible.
