import geopandas as gpd
import matplotlib.pyplot as plt

# Load GeoJSON
geojson_path = r"datasets/TAMIL NADU_DISTRICTS.geojson"
gdf = gpd.read_file(geojson_path)

# Plot
fig, ax = plt.subplots(figsize=(10, 8))
gdf.plot(column="region" if "region" in gdf.columns else None,
         cmap="Set3",
         edgecolor="black",
         legend=True,
         ax=ax)

# Add labels at centroid
for idx, row in gdf.iterrows():
    plt.annotate(text=row["dtname"],  # change "region" to the right column in your file (e.g., "DIST_NAME")
                 xy=(row.geometry.centroid.x, row.geometry.centroid.y),
                 horizontalalignment="center",
                 fontsize=6,
                 color="black",
                 weight="bold")

ax.set_title("Tamil Nadu Map with Region Labels", fontsize=14)
plt.show()


# Load shapefile
world = gpd.read_file(r"datasets/countries/ne_110m_admin_0_countries.shp")

# Plot without reprojection
fig, ax = plt.subplots(figsize=(14, 8))
world.plot(ax=ax, color="lightblue", edgecolor="black")

ax.set_title("World Map with Countries", fontsize=14)
plt.axis("equal")
plt.show()
