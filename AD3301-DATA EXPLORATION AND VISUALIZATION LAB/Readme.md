````markdown
# Data Exploration and Visualization Lab

This repository contains scripts and datasets for performing exploratory data analysis (EDA) and cartographic visualizations using **Python** and **R**.

---

## 📌 Prerequisites

Before running the code, make sure you have the following installed:

- **Python** (>= 3.8 recommended)  
- **R** (>= 4.0 recommended)  
- **Git** (optional, for cloning the repository)

---

## 🐍 Python Setup

### 1. Clone the repository
```bash
git clone https://github.com/Tech-master1234/Lab.git
````

### 2. Create a virtual environment (recommended)
# On Windows
```bash
python -m venv venv
venv\Scripts\activate      
```
# On Mac/Linux
```bash
python3 -m venv venv
venv\Scripts\activate      
```

### 3. Install required dependencies

All Python dependencies are listed in **`requirements.txt`**. To install:

```bash
pip install -r requirements.txt
```

---

## 📊 R Setup

Some analyses/visualizations may also use R.
You can install the required R packages by running in R:

```r
install.packages(c("tidyverse", "ggplot2", "sf"))
```

---

## 🚀 Running the Project

* To run the **Python visualizations**:

```bash
python your_script_name.py
```

* To run the **R scripts**:

```bash
Rscript your_r_script.R
```

---

## 📂 Project Structure

```
.
├── datasets/                # Contains datasets like Titanic, Global Landslides, Wine Quality
    └── in_shp/                  # Shapefiles for India boundary map
├── requirements.txt         # Python dependencies
├── python_scripts.py      # Example Python visualization script
├── r_script.R          # Example R visualization script
└── README.md
```

---
