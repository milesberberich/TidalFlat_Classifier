# TidalFlats_Classifier

## Purpose

**Enables you to detect tidal flat with just two functions!**

An easy package that enables you to implement the approach of [Murray et al. 2018](https://www.nature.com/articles/s41586-018-0805-8) using the _Google-Earth-Engine API_ in Python!\
A pretrained Classifier will be used &rarr; no need to collect training data / train a model.

## Contents

The package itself consists of two functions:
- **download_classifier.py:** Downloads a trained Random Forest into your system.
- **run_classifier.py:** After specific the _area of interest (aoi)_ and the start and end year_ of the analysis, it performs the classification.
- **example_script.py**: Shows a simple example workflow.

## Requirements

- Google Earth Engine account
- Google Cloud project ID (for GEE authentification)
- Python >= 3.13

## Installation & Setup

The package can be installed using:\

```pip install git+https://github.com/milesberberich/TidalFlat_Classifier.git```

To be able to use the Google-Earth-Engine, run:
```
import ee
ee.Authenticate()
ee.Initialize(project="your_example_project") 
```

## Example

After installation and authentification of GEE, thats the only code required to run the model and download the results.

```
classifier = download_classifier()

result = run_classifier(path_to_aoi="/home/example_areaofinterest.shp", start_year="2016", end_year="2019", classifier=classifier)

url = result.getDownloadURL({'scale': 30,'fileFormat': 'GeoTIFF'})
print(url)
```
The classification can then be downloaded using the link given by the code.\
The `start_year` and `end_year` needs to be a three-year intervall.

## Output

Using the link you download a .tiff file with the classification.\
The classification will be saved like:

0 = "Other" (mostly land and vegetated areas)\
1 = "Water"\
2 = "Tidal Flat"

The classification has a spatial resolution of 3m and a temporal resolution of three years. 

**Reminder:** Depending on the software used to visualize the result, the class "Other" (0) might be set as a NoData-Value. 
## Methodology

The classification uses an approach based on [Murray et al. 2018](https://www.nature.com/articles/s41586-018-0805-8).\
Landsat-data is used to derive indices and statistics. 
Auxillary data like `NOAA/NGDC/ETOPO1'` and `JRC/GSW1_4/GlobalSurfaceWater` is used as well and  
The RandomForest-Classifier was trained using the training data of [Murray et al. 2018](https://www.nature.com/articles/s41586-018-0805-8).
Overall Accuracy is 93%. The model was trained using the [code originally used in the paper](https://github.com/nick-murray/global-tidalFlat).
