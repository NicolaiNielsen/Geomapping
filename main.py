# %%
import pandas as pd
import matplotlib.pyplot as plt
import descartes
import geopandas as gpd
from shapely.geometry import Polygon, Point

sea_map = gpd.read_file('C:/Users/Nicol/Downloads/mygeodata/Limfjorden-polygon.shp')
sea_map.plot()
sea_map.to_crs(epsg=4326).plot()
df = pd.read_csv('C:/Users/Nicol/Downloads/mygeodata/secret-RawData.v3.csv',  encoding = "ISO-8859-1", sep=';', error_bad_lines=False, engine='python')


df["latitude"]=df["latitude"].astype(str)
df["longitude"]=df["longitude"].astype(str)
df['latitude'] = df['latitude'].str.replace('56', '56.', 1)
df['longitude'] = df['longitude'].str.replace('8', '8.', 1)
df["latitude"]=df["latitude"].astype(float)
df["longitude"]=df["longitude"].astype(float)
df.dtypes

crs = {'init':'EPSG:4326'}
geometry = [Point(xy) for xy in zip(df['longitude'], df['latitude'])]
geo_df = gpd.GeoDataFrame(df, crs = crs, geometry = geometry)
print(geo_df.head())

fig, ax = plt.subplots(figsize = (10,10))
sea_map.to_crs(epsg=4326).plot(ax=ax, color='lightgrey')
geo_df.head().plot(ax=ax)
ax.set_title('Mapped')



# %%
