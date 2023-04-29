# Process
1. Download DTM from [Copernicus](https://ec.europa.eu/eurostat/web/gisco/geodata/reference-data/elevation/copernicus-dem/elevation). They come as Geotiff tiles in the WGS 84 CRS.
2. Create a virtual raster to merge them, and reproject it to ESPG:3035, which is better suited for Europe.
3. Convert the virtual raster into a normal raster and compute a hillshade from it
	1. Parameters: multidirectional lighting, 315 degrees hazimut, and 65 degrees elevation, compute edges, Z factor = 2.
4. Style the DEM with a color ramp that starts at green near sea level, then yellow, brown and white for the mountains.
5. Style the hillshade to highlight the relief in high-slope areas (mountain ranges).
	1. Set rendering to multiply.
	2. Increase brightness to remove low frequency slopes and reduce gamma to make high frequency details more visible.
6. Use a vector shape of the world borders and dissolve it, to get just the coast lines. Give it a thin line, just to make the coastlines a bit sharper.

# Feedback
I asked for feedback about the first version of my map on the [GIS subreddit](https://www.reddit.com/r/gis/comments/12yibzz/first_time_making_a_topographic_map_at_a_large/) and received some fantastic advice. Here is what I ended up applying to improve my work:

- u/AD613, u/MrVernon09, u/Daexmun
	- Maps that cover a large extent are of course called small scale, not large scale.
- u/manualLurking
	- Clipping the DEM to the national boundaries looks better than using the raw DEM tiles.
	- Use a color ramp such that the color at low elevations contrasts with the background color.
- u/DjangoBojangles
	- Try different hillshades. Use angles about 30 degrees south of 90 or 270 for sunrise or sunset directions. Sun angles between 35-50 are most common.
	- Search gis topographic gradients to get some more color scheme ideas.
- u/gghumus
	- Use different colors to have the land stand out from the sea a bit better.
- u/geo-special
	- Use blender to make it pop. I have not done that, but I would like to in the future. I read the tutorials you linked, and one of them mentioned the Copernicus datasets, which I decided to use for this map. 
- u/Brawnyllama
	- Use boundary lines for definition of low contrast, and perhaps a graticule layer.
- u/Brawnyllama
	- Be mindful about font sizes, and scalebar extents.
- u/Tomniverse, u/ManAboutCouch
	- It's best to use ESPG:3035 for Europe.
- u/kaik1914
	- Move the map title higher up.
- u/DragonBadgerBearMole
	- Try to include Eastern Europe
	- Look at the McNally and National Geographic color ramp, where green implies vegetation and thus lowlands, and yellows/browns are used at the higher elevations.
