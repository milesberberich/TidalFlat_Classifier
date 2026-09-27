def classify_tidalflats(path_to_aoi: str, start_year: str, end_year: str):

    '''The funtion calls the pretrained RandomForest-Classifier and applies it in the defined area-of-interest from start_year to end_year.
    path_to_aoi: needs to point to a geojson or shapefile
    start_year: e.g. 2016
    end_year: e.g. 2019

    To run the function, you need to be logged into Google-Earth-Engine'''

# ---------- CALL PACKAGES ---------

import geopandas as gpd
import ee

# ---------- READ AOI ----------

aoi = gpd.read_file(path_to_aoi)

