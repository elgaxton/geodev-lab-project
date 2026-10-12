# Oil spill Monitor Project

Geospatial analysis and interactive mapping of oil spill hotspots and potential environmental risk areas across 

**GeoDev Lab Africa, Cohort One.** Gaxton Okobah


## Datasets 

- oilspill data
- State Boundaries

## Timeline in view
2015 to 2025

## The Question

Which areas in Nigeria's South South region have the highest concentration of oil spill incidents, and where are the potential environmental risk hotspots?

## Why it Matters

Although oil spill incidents are recorded across the region, simply mapping individual spill locations does not clearly show where incidents are concentrated or which areas may require greater attention. With spatial analysis we can:

- Identify oil spill hotspot
- Examine their distribution across the states and LGAs
- determine whether areas with frequent incidents overlap with settlements and environmentally sensitive features.


## Features of Focus on the Datasets

Point locations of recorded oil spill incidents, including:

- Incident date
- Latitude and longitude
- State
- LGA
- Oil spill cause
- Estimated quantity spilled
- Estimated spill area
- Company/operator
- Type of facility
- Contaminant
- Spill-area habitat

## Required South South State boundaries

Polygon boundaries for:
- Akwa Ibom
- Bayelsa
- Cross River
- Delta
- Edo
- Rivers

## Week 2

### Upload of Dataset to solve the above problem statement

Click here to `git commit` download the data [oilspill dataset](https://github.com/elgaxton/geodev-lab-project/blob/main/oil_spill_master.csv)

### Features of the Dataset

|DATASET |FEATURE TYPE |FEATURE COUNT |FILE FORMAT| SOURCE
|---|---|---|---|---|
|Oilspill Data |Points |9,929 | CSV |[OilspillMonitor](oilspillmitor.ng)
|State Boundaries |Polygons| 37 | SHAPE FILE|[GRID 3](grid3.org)

## Week 3

CRS Choosen: EPSG:32632 - WGS 84 / UTM zone 32N - Reason for my choice is simply because the oil spill dataset point features all came out well after Reprojection

### Quality Checks
1. What is the coodinate reference system?
   Coordinate System: The coordinate system was EPSG:4326 - WGS 84 which I reprojected to EPSG:32632 - WGS 84 / UTM zone 32N

2. Are there empty or null values? Yes, there are some null values, which will have to be handled as we progress further in this learning journey
3. Are there duplicate values? No duplicate values
4. Does the geometry look valid? Yes. the Geometric system looks valid.
5. Does the coverage include your study area of is it halfway? Yes, the coverage includes my total area of study, South-South Region of Nigeria

What was clipped was the point data features of the spill coordinates. It was clipped to the the State boundaries shapefiles of the Area of Study (South-South Region).


![Just the Map](https://github.com/elgaxton/geodev-lab-project/blob/main/Area%20of%20Study%20Clipped.PNG)

[Geopackage of Study Area](https://github.com/elgaxton/geodev-lab-project/blob/main/SouthSouth_oilspill%20points.gpkg)
- 
## Week 4

Question: WHAT SETTLEMENTS ARE WITHIN 200 METERS OF OIL SPILL LOCATIONS IN SOUTH SOUTH STATES FROM 2015 TO 2025?

Spatial Analysis Carried out as follows:
1. Buffer
2. Intersection
3. Union
4. Joint Attributes

Findings: 61, 506 Settlements out of 1,091,710  settlements  fall within  200M of Oil Spill Locations in the South South States of Nigeria


![Map of Settlements within 200 Meters of Oil Spill Locations in South South States](https://github.com/elgaxton/geodev-lab-project/blob/main/South%20South%20Settlements%20within%20200M%20%20of%20Oil%20Spill%20Locations.png)

## Month 2: Preparation of Environment, Python Intro

## Week 5:

- I Set up Python, Vs Code and Terminal. I also ran a Python file, hello.py

[Python file](https://github.com/elgaxton/geodev-lab-project/blob/main/hello.py)

![Screenshot of Python Environment](https://github.com/elgaxton/geodev-lab-project/blob/main/Python.png)

## Week 6
I learnt the Following:
-Installation of Pandas, Geopandas modules
- Understanding pyproject.toml, uv.lock files
- Using terminal on Powershell and on VS code
- Read CSV files and viewing the Dataframes
- Reading GeoJson files and viewing the Geodataframes
- How to increase the font of the Terminal

![SCreenshot of Main.py](https://github.com/elgaxton/geodev-lab-project/blob/main/pyproject_screenshot.png)

[uv.lock](https://github.com/elgaxton/geodev-lab-project/blob/main/uv.lock)

[pyproject.toml](https://github.com/elgaxton/geodev-lab-project/blob/main/pyproject.toml)

