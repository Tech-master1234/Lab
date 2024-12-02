import matplotlib.pyplot as plt
import geopandas as gpd
import pandas as pd

# Load India map shape file
fp = "C:/Users/manoj/OneDrive/Documents/DEV LAB/india_boundary.shp"
map_df = gpd.read_file(fp)

# Create a DataFrame with landslide data (you need to have this data)
data = {'State': ['Jammu and Kashmir', 'Himachal Pradesh', 'Uttarakhand', 'Sikkim', 'Arunachal Pradesh'],
        'Landslides': [175, 150, 125, 100, 75]}

df = pd.DataFrame(data)

# Merge the DataFrames
merged = map_df.set_index('st_nm').join(df.set_index('State'))

# Plot the map
fig, ax = plt.subplots(1, figsize=(10, 6))
merged.plot(column='Landslides', cmap='YlOrRd', linewidth=0.8, ax=ax, edgecolor='0.8', legend=True)
ax.axis('off')
ax.set_title('Number of Landslides in India State-wise')

plt.show()
