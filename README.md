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

CRS Choosen: EPSG 4326 - Reason for my choice simply because the oilspill dataset point features all came out as compared to when I used N32 layer

### Quality Checks
- I checked for the layer Coordinate Reference System and found it is EPSG:4326 - WGS 84

- Audit measurement units was Verified for CRS degrees, like WGS 84 and linear units (meters, UTM) 

What was Clipped is the point data features of the spill coordinates. It was clipped to the the State boundaries shapefiles of the Area of Study (Sout South Region).


[Clipped Image of Area of Study](https://github.com/elgaxton/geodev-lab-project/blob/main/Clipped%20area%20of%20study.PNG)

[Just the Map](https://github.com/elgaxton/geodev-lab-project/blob/main/Area%20of%20Study%20Clipped.PNG)

[Geopackage of Study Area](<Week 3/oilspill_layer_cliped.gpkg>)
- 

