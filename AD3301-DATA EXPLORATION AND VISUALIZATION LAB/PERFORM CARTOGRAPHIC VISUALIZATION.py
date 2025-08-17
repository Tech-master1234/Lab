import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

# --- Step 1: Load shapefile (India boundaries) ---
fp = r"datasets/in_shp/in.shp"
map_df = gpd.read_file(fp)

# --- Step 2: Print DataFrame (first rows) ---
print(map_df.head())

# --- Step 3: Plot plain India map (blue) ---
fig, ax = plt.subplots(1, figsize=(8, 10))
ax.axis("off")
ax.set_title("India Map (Base Outline)", fontsize=14, fontweight="bold")
map_df.plot(ax=ax, color="dodgerblue", edgecolor="white", linewidth=0.8)
plt.show()

# --- Step 4: Load landslide dataset ---
df = pd.read_csv("datasets/globallandslides.csv")
pd.set_option("display.max_columns", None)

# --- Step 5: Filter for India only ---
ls_df = df[df.country_name == "India"].copy()

# --- Step 6: Extract year (optional) ---
ls_df["Year"] = pd.to_datetime(
    ls_df["event_date"], 
    format="%Y-%m-%d",   # adjust if needed
    errors="coerce"
).dt.year

# --- Step 7: Keep only landslides category ---
ls_df = ls_df[ls_df.landslide_category == "landslide"]

# --- Step 8: Clean state names ---
replacements = {
    "Nāgāland": "Nagaland",
    "Meghālaya": "Meghalaya",
    "Tamil Nādu": "Tamil Nadu",
    "Karnātaka": "Karnataka",
    "Gujarāt": "Gujarat",
    "Arunāchal Pradesh": "Arunachal Pradesh"
}
ls_df["admin_division_name"] = ls_df["admin_division_name"].replace(replacements)

# --- Step 9: Count landslides per state ---
state_df = ls_df["admin_division_name"].value_counts().to_frame()
state_df.reset_index(inplace=True)
state_df.columns = ["State", "Count"]

# --- Step 10: Merge with shapefile ---
merged = map_df.set_index("name").join(state_df.set_index("State"))
merged["Count"] = merged["Count"].fillna(0)

# --- Step 11: Plot choropleth (landslides) ---
fig, ax = plt.subplots(1, figsize=(12, 10))
ax.axis("off")
ax.set_title("Number of Landslides in India (State-wise)", 
             fontdict={"fontsize": 16, "fontweight": "bold"})

merged.plot(column="Count",
            cmap="YlOrRd",
            linewidth=0.8,
            ax=ax,
            edgecolor="0.8",
            legend=True,
            legend_kwds={"label": "Number of Landslides"})

plt.show()
