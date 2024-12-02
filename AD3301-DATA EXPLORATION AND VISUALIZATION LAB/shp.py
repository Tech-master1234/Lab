import geopandas as gpd
from shapely.geometry import Polygon

# Define the coordinates for the boundary of India
india_boundary_coords = [
    (68.1, 7.5), (97.4, 7.5), (97.4, 35.7), (68.1, 35.7), (68.1, 7.5)  # Add more points as needed
]

# Create a Polygon geometry representing the boundary of India
india_polygon = Polygon(india_boundary_coords)

# Create a GeoDataFrame with the India boundary geometry
gdf = gpd.GeoDataFrame(geometry=[india_polygon])

# Define the file path to save the shapefile
output_fp = 'india_boundary3.shp'

# Save the GeoDataFrame to a shapefile
gdf.to_file(output_fp)
