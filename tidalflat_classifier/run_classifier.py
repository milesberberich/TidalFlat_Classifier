
# ---------- CALL PACKAGES ---------

import geopandas as gpd
import ee
from shapely.geometry import mapping


def run_classifier(path_to_aoi: str, start_year: str, end_year: str, classifier: ee.Classifier) -> ee.Image:

    '''The funtion calls the pretrained RandomForest-Classifier and applies it in the defined area-of-interest from start_year to end_year.
    path_to_aoi: needs to point to a geojson or shapefile
    start_year: e.g. 2016
    end_year: e.g. 2019

    The year need to create a 3-year intervall.

    To run the function, you need to be logged into Google-Earth-Engine.
    The function outputs an ee.Image, which can be used for further processing or downloaded as shown in the example script.
    '''



# ---------- READ AOI ----------

    aoi = gpd.read_file(path_to_aoi)
    aoi = aoi.to_crs(epsg=4326)
    aoi = ee.Geometry(mapping(aoi.geometry.unary_union))
    print("Area of interest was converted to a ee.geometry")

# ---------- LOAD LANDSAT ----------

    def mask_and_scale(image):
        qa_mask = image.select('QA_PIXEL').bitwiseAnd(62).eq(0)
        optical = image.select('SR_B.').multiply(0.0000275).add(-0.2)
        return image.addBands(optical, None, True).updateMask(qa_mask)


    band_names = ['green', 'swir1', 'swir2', 'nir', 'red']
    bands_tm = ['SR_B2', 'SR_B5', 'SR_B7', 'SR_B4', 'SR_B3']  # L7
    bands_oli = ['SR_B3', 'SR_B6', 'SR_B7', 'SR_B5', 'SR_B4']  # L8, L9


    def load_collection(collection_id, band_map):
        return (ee.ImageCollection(collection_id)
                .filterBounds(aoi)
                .filterDate(start_year, end_year)
                .map(mask_and_scale)
                .select(band_map, band_names))


    l7 = load_collection('LANDSAT/LE07/C02/T1_L2', bands_tm)
    l8 = load_collection('LANDSAT/LC08/C02/T1_L2', bands_oli)
    l9 = load_collection('LANDSAT/LC09/C02/T1_L2', bands_oli)
    collection = l7.merge(l8).merge(l9)

    print("Landsat collection loaded")

# ---- Indices ----
    def ndwi(img):  return img.normalizedDifference(['green', 'nir']).rename('ndwi')
    def mndwi(img): return img.normalizedDifference(['green', 'swir1']).rename('mndwi')
    def ndvi(img):  return img.normalizedDifference(['nir', 'red']).rename('ndvi')
    def awei(img):
        return img.expression("4*(b('green')-b('swir1'))-(0.25*b('nir')+2.75*b('swir2'))").rename('awei')


# ---- Reducers ----
    full_stats = (ee.Reducer.min()
              .combine(ee.Reducer.max(), '', True)
              .combine(ee.Reducer.stdDev(), '', True)
              .combine(ee.Reducer.median(), '', True)
              .combine(ee.Reducer.percentile([10, 25, 50, 75, 90]), '', True)
              .combine(ee.Reducer.intervalMean(0, 10).setOutputs(['intMn0010']), '', True)
              .combine(ee.Reducer.intervalMean(10, 25).setOutputs(['intMn1025']), '', True)
              .combine(ee.Reducer.intervalMean(25, 50).setOutputs(['intMn2550']), '', True)
              .combine(ee.Reducer.intervalMean(50, 75).setOutputs(['intMn5075']), '', True)
              .combine(ee.Reducer.intervalMean(75, 90).setOutputs(['intMn7590']), '', True)
              .combine(ee.Reducer.intervalMean(90, 100).setOutputs(['intMn90100']), '', True)
              .combine(ee.Reducer.intervalMean(10, 90).setOutputs(['intMn1090']), '', True)
              .combine(ee.Reducer.intervalMean(25, 75).setOutputs(['intMn2575']), '', True))

    mean_10_90 = ee.Reducer.intervalMean(10, 90).setOutputs(['intMn1090'])

    predictors = (collection.map(awei).reduce(full_stats)
        .addBands(collection.map(ndwi).reduce(full_stats))
        .addBands(collection.map(mndwi).reduce(full_stats))
        .addBands(collection.map(ndvi).reduce(mean_10_90))
        .addBands(collection.select('nir').reduce(mean_10_90))
        .addBands(collection.select('swir1').reduce(mean_10_90))
        .addBands(ee.Image('NOAA/NGDC/ETOPO1').select(['bedrock'], ['etopo']).resample('bicubic'))
        .addBands(ee.Image('JRC/GSW1_4/GlobalSurfaceWater').select(['occurrence'], ['surfaceWater']).unmask())
        .clip(aoi))

    print("Predictors calculated.")
    print("Classification starts.")

# ---------- CLASSIFICATION ---------

    results = predictors.classify(classifier)
    print("Classification finished.")
    return(results)







