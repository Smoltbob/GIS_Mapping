# Swedish postcodes
## Goal
When making maps I often end up needing to subdivide localities into smaller areas. Using zipcodes is one way.
Instead of grabing a few zipcode polygons when I need them, I thought it would be good to gather them all for once.

## Process
It was not easy to find a source of geo data for the Swedish zipcodes. There is a database one can buy but no free data. 
1. I ended up using web scrapping to collect 10610 geojson files, one for each zipcode area.
2. I then combined all of these into a geopackage database.

## Map
This is a simple map meant to experiment with the dataset. I displayed the zipcodes as integer values with the Turbo color gradient.
I then picked a few cities that I found interesting to display.
The font I used is [Tratex](https://en.wikipedia.org/wiki/Tratex).