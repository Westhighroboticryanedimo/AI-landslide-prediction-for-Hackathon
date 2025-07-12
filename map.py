import pandas
import geopandas as gpd
from matplotlib import pyplot as plt
import matplotlib.colors as mcolors
print("DONE! ")
data = pandas.read_csv(r'C:\Users\pries\ai_landslide_predictions.csv')
print("DONE! ")
shape_data = gpd.read_file(r'C:\Users\pries\OneDrive\Desktop\Games\PythonPrograms\Face\Flood Model\WA_Soils.zip')
print("DONE! ")
# Merge the results
revised_map_data = shape_data.merge(data[["OBJECTID", "SOIL_LANDSLIDE_HAZARD"]], on="OBJECTID", how="left")
print("DONE! ")
# Plot the data with the custom colormap
revised_map_data.plot(column='SOIL_LANDSLIDE_HAZARD', cmap=mcolors.ListedColormap(['burlywood', 'saddlebrown']), legend=True)
plt.show()