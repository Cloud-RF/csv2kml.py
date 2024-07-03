import geopandas as gpd
from math import sqrt
import sys
import fiona
import pandas as pd

fiona.supported_drivers['KML'] = 'rw'
fiona.supported_drivers['LIBKML'] = 'rw'

diameter = 20

df = pd.read_csv(sys.argv[1])
gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df["lon"], df["lat"]), crs='EPSG:4326')
print(gdf)
gdf = gdf.to_crs('EPSG:3857')
print(gdf)
gdf = gpd.GeoDataFrame(geometry=gdf.buffer(distance=diameter/sqrt(2), cap_style=3), crs='EPSG:3857')
gdf = gdf.to_crs('EPSG:4326')
print(gdf)
gdf.to_file(f"{sys.argv[1]}.kml", driver='KML')

