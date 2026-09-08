# My Geodev – Lab Project

## Project Question

**Which areas in Nigeria's South South region have the highest concentration of oil spill incidents, and where are the potential environmental risk hotspots?**

## Why it matters

Nigeria's South South region contains the core of the country's Niger Delta oil-producing environment, with extensive oil and gas infrastructure, communities, rivers, wetlands, mangrove ecosystems and agricultural areas.

Oil spill incidents can have significant environmental and socioeconomic consequences, particularly when spills occur repeatedly or close to communities, waterways, agricultural land and other environmentally sensitive areas.

Although oil spill incidents are recorded across the region, simply mapping individual spill locations does not clearly show where incidents are concentrated or which areas may require greater attention.

Spatial analysis can be used to identify **oil spill hotspots**, examine their distribution across states and Local Government Areas (LGAs), and determine whether areas with frequent incidents overlap with settlements and environmentally sensitive features.

Identifying these potential hotspots can support environmental monitoring, spill-response planning, prioritisation of field investigations, and data-driven decision-making.

The project will therefore develop a spatial analysis workflow for identifying areas of concentrated oil spill activity across the South South region of Nigeria.

## The data I need

### Oil spill incidents

Point locations of recorded oil spill incidents, including:

* Incident date
* Latitude and longitude
* State
* LGA
* Oil spill cause
* Estimated quantity spilled
* Estimated spill area
* Company/operator
* Type of facility
* Contaminant
* Spill-area habitat
* Other available incident attributes

### South South State boundaries

Polygon boundaries for:

* Akwa Ibom
* Bayelsa
* Cross River
* Delta
* Edo
* Rivers

### LGA boundaries

Administrative boundaries for analysing oil spill incidents and hotspot patterns at Local Government Area level.

### Settlements and populated places

Locations of villages, towns and communities within the South South region.

These will be used to examine whether high oil-spill concentration areas occur close to populated communities.

### Rivers and water bodies

Locations of rivers, creeks, lakes, wetlands and other major water features.

These will help identify potential overlap between oil spill hotspots and environmentally sensitive water resources.

### Road network

A road network covering the study area.

This can be used to examine accessibility to identified hotspot areas and potentially support future spill-response planning.

### Land-use / land-cover data

Land-use and land-cover information showing features such as:

* Built-up areas
* Agricultural land
* Forest
* Wetlands
* Mangrove areas
* Water bodies

This will provide additional environmental context for interpreting oil spill hotspots.

## The data sources

### Oil spill incident data – NOSDRA Oil Spill Monitor

The primary oil-spill dataset will be obtained from the **Nigerian Oil Spill Monitor**, managed by the National Oil Spill Detection and Response Agency (NOSDRA).

NOSDRA states that the Oil Spill Monitor provides public access to oil-spill information collected through Joint Investigation Visits (JIVs), although the agency also notes that records can be incomplete and may change as new information becomes available.

[Nigerian Oil Spill Monitor](https://www.nosdra.oilspillmonitor.ng)

### Administrative boundaries – HDX / OCHA

State and LGA boundaries can be obtained from the Humanitarian Data Exchange and other authoritative Nigerian administrative boundary datasets.

[Humanitarian Data Exchange](https://data.humdata.org)

### Settlements and roads – OpenStreetMap

OpenStreetMap can provide settlement locations, roads and other geographic features.

[OpenStreetMap](https://www.openstreetmap.org)

### Road network – Geofabrik

Regional OpenStreetMap extracts can be obtained from Geofabrik.

[Geofabrik Downloads](https://download.geofabrik.de)

### Population data – WorldPop

Population distribution data can be used to estimate the number of people living within or close to identified oil-spill hotspot areas.

[WorldPop](https://www.worldpop.org)

### Land-cover data – ESA WorldCover

Global land-cover datasets can provide additional information about the environmental characteristics of areas affected by oil-spill incidents.

## Methodology

I will first obtain and prepare oil-spill incident records covering the six South South states.

The incident coordinates will be cleaned and converted into a GIS point layer.

The study area will then be clipped to the South South region and analysed at both **state and LGA levels**.

### Step 1 – Data preparation

The oil-spill dataset will be cleaned by:

* Removing duplicate records where appropriate;
* Checking missing coordinates;
* Validating latitude and longitude values;
* Standardising state and LGA names;
* Converting incident dates into a consistent format;
* Checking missing or inconsistent spill quantities;
* Creating derived variables such as incident year and spill-size categories.

### Step 2 – Spatial distribution

The locations of oil spill incidents will be mapped across the South South region.

The analysis will examine:

* Number of incidents by state;
* Number of incidents by LGA;
* Spill quantity by state;
* Spill quantity by LGA;
* Incident trends over time; and
* Distribution of incidents by reported cause.

### Step 3 – Hotspot analysis

Spatial hotspot analysis will then be used to identify areas where oil spill incidents are unusually concentrated.

I will use **Kernel Density Estimation (KDE)** to generate a continuous surface showing areas with high concentrations of spill incidents.

Where appropriate, a statistical hotspot technique such as **Getis-Ord Gi*** can also be applied at an aggregated spatial level to identify statistically significant high- and low-value clusters.

The resulting hotspot map will classify areas such as:

* Low concentration
* Moderate concentration
* High concentration
* Very high concentration

### Step 4 – Environmental exposure analysis

The identified oil-spill hotspots will be overlaid with:

* Settlements;
* Rivers and water bodies;
* Wetlands;
* Agricultural areas;
* Mangrove/forest areas; and
* Population distribution.

This will help identify areas where high concentrations of recorded oil spills coincide with populated or environmentally sensitive locations.

### Step 5 – Priority-risk areas

The different spatial layers will be combined to identify **potential priority environmental-risk areas**.

For example, an area may receive higher priority where it has:

**High oil-spill concentration + high population exposure + proximity to water bodies/environmentally sensitive land.**

The project will present these areas as **potential risk-priority zones**, rather than claiming that the analysis proves actual environmental contamination.

## Tools I would use

**QGIS / ArcGIS Pro** – for spatial data preparation, hotspot analysis, overlay analysis, mapping and visualization.

**Python** – for data cleaning, exploratory analysis, automation and statistical/spatial analysis where appropriate.

**Pandas / GeoPandas** – for tabular and geospatial data processing.

**OpenStreetMap** – for settlements, roads and other geographic features.

**GitHub** – for version control, project documentation and sharing the project workflow.

## What I would build

I would build an **Interactive South South Oil Spill Risk and Hotspot Map/Dashboard**.

The dashboard would allow users to explore:

* Oil spill incident locations;
* Number of incidents by state;
* Number of incidents by LGA;
* Oil spill trends over time;
* Reported causes of spills;
* Estimated quantities spilled;
* Oil spill hotspot areas;
* Nearby settlements;
* Nearby rivers and water bodies;
* Population potentially exposed to hotspot areas; and
* Potential environmental-risk priority zones.

A user could select a state or LGA and see the distribution and concentration of recorded oil spill incidents within that area.

The dashboard would also allow users to filter incidents by **year, cause, company/operator, facility type and spill quantity**, where those fields are available.

## Proposed analytical output

The main output would be a **South South Oil Spill Hotspot and Environmental Risk Map**.

The final map would combine:

**Oil Spill Incidents → Hotspot Density → Settlements → Water Bodies → Population → Environmental Context → Priority Areas**

This would provide a simple spatial decision-support tool for identifying areas that may require closer environmental monitoring or further field investigation.

## Limitations

The NOSDRA Oil Spill Monitor is based on reported oil-spill information and Joint Investigation Visit records. NOSDRA notes that some information may be incomplete, including missing geolocation or quantity information, and that the published dataset can change as records are added or updated.

Therefore, the absence of recorded spills in an area should **not** necessarily be interpreted as proof that no oil spills have occurred there.

OpenStreetMap settlement, road and geographic-feature data may also be incomplete, particularly in remote areas.

The analysis will identify **potential spatial risk or priority areas**, not establish actual levels of environmental contamination.

KDE and other hotspot methods describe the spatial pattern of recorded incidents; they do not by themselves establish causation.

Population proximity also does not necessarily mean that residents have been exposed to pollution.

Finally, the project will depend on the quality and completeness of the available incident coordinates, dates, spill quantities and other attributes.

## Expected final product

The project will produce:

1. **Cleaned South South oil-spill geospatial dataset**
2. **Interactive oil-spill incident map**
3. **Oil-spill density/hotspot map**
4. **State and LGA oil-spill statistics**
5. **Temporal trend visualisations**
6. **Oil-spill hotspot and settlement overlay**
7. **Oil-spill hotspot and water-body overlay**
8. **Potential environmental-risk priority map**
9. **Interactive dashboard**
10. **Documented and reproducible GIS/Python workflow on GitHub**

The final product will demonstrate how geospatial data, spatial analysis and interactive mapping can be used to transform oil-spill records into useful information for environmental monitoring and decision-making.
