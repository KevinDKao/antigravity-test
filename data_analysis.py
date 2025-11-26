import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('globalAirQuality.csv')

# Create figure with 4 subplots
fig, axs = plt.subplots(2, 2, figsize=(15, 10))
fig.suptitle('Air Quality Data Analysis', fontsize=16)

# Graph 1: Average AQI by City
avg_aqi = df.groupby('city')['aqi'].mean().sort_values(ascending=False).head(10)
axs[0, 0].bar(avg_aqi.index, avg_aqi.values, color='skyblue')
axs[0, 0].set_title('Top 10 Cities by Average AQI')
axs[0, 0].set_xlabel('City')
axs[0, 0].set_ylabel('Average AQI')
axs[0, 0].tick_params(axis='x', rotation=45)

# Graph 2: PM2.5 vs PM10
axs[0, 1].scatter(df['pm25'], df['pm10'], alpha=0.5, color='green')
axs[0, 1].set_title('PM2.5 vs PM10')
axs[0, 1].set_xlabel('PM2.5')
axs[0, 1].set_ylabel('PM10')

# Graph 3: Temperature vs AQI
axs[1, 0].scatter(df['temperature'], df['aqi'], alpha=0.5, color='orange')
axs[1, 0].set_title('Temperature vs AQI')
axs[1, 0].set_xlabel('Temperature')
axs[1, 0].set_ylabel('AQI')

import geopandas as gpd
from shapely.geometry import Point
import geodatasets

# ... (previous code remains the same)

# Graph 4: Global Air Quality Map
world = gpd.read_file(geodatasets.get_path('naturalearth.land'))
geometry = [Point(xy) for xy in zip(df['longitude'], df['latitude'])]
gdf = gpd.GeoDataFrame(df, geometry=geometry)

world.plot(ax=axs[1, 1], color='lightgrey', edgecolor='white')
gdf.plot(ax=axs[1, 1], column='aqi', cmap='OrRd', markersize=20, legend=True, legend_kwds={'label': "AQI"})
axs[1, 1].set_title('Global Air Quality Map')
axs[1, 1].set_xlabel('Longitude')
axs[1, 1].set_ylabel('Latitude')

plt.tight_layout()
plt.savefig('air_quality_analysis.png')
print("Analysis complete. Image saved as air_quality_analysis.png")
