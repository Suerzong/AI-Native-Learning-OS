import geopandas as gpd
import matplotlib
import matplotlib.pyplot as plt

gdf_provinces = gpd.read_file('CN-Sheng-A.shp')
gdf_provinces = gdf_provinces.to_crs('EPSG:4326')
gdf = gpd.read_file('china_topography_wgs84.geojson')
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
print(list(set(gdf['CNAME'])))
gdf = gdf[gdf['CNAME'].isin (["低海拔冲积平原","沙丘", "湖泊", "高海拔剥蚀平原"])]
ax=gdf.plot(column='CNAME', legend=True, figsize=(18, 18),
            legend_kwds={'fontsize': 5, 'loc': 'upper left' })
plt.title("地貌类型空间分布")
gdf_provinces.boundary.plot(ax=ax, color='k', linewidth=0.5)
plt.show()

