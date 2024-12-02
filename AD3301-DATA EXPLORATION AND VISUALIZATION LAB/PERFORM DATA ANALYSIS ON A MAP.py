import numpy as np
import pandas as pd
import shapefile as shp
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid", palette="pastel", color_codes=True)
plt.figure(figsize=(10, 6))

#Opening a Vector Map
shp_path = "C:/Users/manoj/OneDrive/Documents/DEV LAB/comuna.shp"
sf = shp.Reader(shp_path)

num_shapes = len(sf.shapes())
print("Number of shapes (features) in the shapefile:", num_shapes)


