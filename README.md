# csv2kml.py
Turn CSV points into KML polygons for use with CloudRF's custom clutter feature.
Useful for windfarm planing etc.

## CSV points

CSV data should have a lat and lon header in EPSG 4326 projection.

	lat,lon
	51.1,-1.2

## Usage

	python3 csv2KML.py points.csv

Change the diameter of the polygon in the script. Default is 20m.
