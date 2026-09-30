 <img src="migratory_bird" align="right" width="250" alt="Tidal Flats Classifier Logo or Demo">



# TidalFlats_Classifier

## Purpose


**Enables you to detect tidal flats with just two functions!**


An user-friendly package that enables you to implement the approach of [Murray et al. 2018](https://www.nature.com/articles/s41586-018-0805-8) using the _Google-Earth-Engine API_ in Python!\

A pretrained Classifier will be used &rarr; no need to collect training data / train a model.\


**Meant to support the conservation of migratory birds that rely on tidal flats as resting places.**


## Contents


The package itself consists of two functions:

- **download_classifier.py:** Downloads a trained Random Forest into your system.

- **run_classifier.py:** After specifying the _area of interest (aoi)_ and the _start and end year_ of the analysis, it performs the classification.

- **example_script.py**: Shows a simple example workflow.


## Requirements


- Google Earth Engine account

- Google Cloud project ID (for GEE authentication)

- Python >= 3.13


## Installation & Setup


The package can be installed using:\


```

!pip install git+https://github.com/milesberberich/TidalFlat_Classifier.git

from tidalflats_classifier import download_classifier, run_classifier

```


To use Google-Earth-Engine, run:

```

import ee

ee.Authenticate()

ee.Initialize(project="your_example_project") 

```


## Example


After installation and authentication of GEE, this is the only code required to run the model and download the results.


```

classifier = download_classifier()


result = run_classifier(path_to_aoi="/home/example_areaofinterest.shp", start_year="2016", end_year="2019", classifier=classifier)


url = result.getDownloadURL({'scale': 30,'fileFormat': 'GeoTIFF'})

print(url)

```

The classification can then be downloaded using the link given by the code.\

The `start_year` and `end_year` need to span a three-year interval.


## Output


Using the link provided by the script, you can download a .tiff file with the classification.\

The classification will be saved like:


0 = "Other" (mostly land and vegetated areas)\

1 = "Water"\

2 = "Tidal Flat"


The classification has a spatial resolution of 30m and a temporal resolution of three years. It uses EPSG:4326.


**Reminder:** Depending on the software used to visualize the result, the class "Other" (0) might be set as a NoData-Value. 

## Methodology


The classification uses an approach based on [Murray et al. 2018](https://www.nature.com/articles/s41586-018-0805-8).

The full workflow used to train the model is documented in https://github.com/GebTorte/WWFTidalFlats.


Most of the 56 parameters are indices and metrics derived from Landsat data. Furthermore auxiliary data like `NOAA/NGDC/ETOPO1'` and `JRC/GSW1_4/GlobalSurfaceWater` were used.

The RandomForest-Classifier was trained using the training data of [Murray et al. 2018](https://www.nature.com/articles/s41586-018-0805-8).

The model was trained using the [code originally used in the paper](https://github.com/nick-murray/global-tidalFlat).


### Accuracy 

Overall Accuracy = 95%\

Tidal Flat Precision = 88,40%\

Tidal Flat Recall = 96.97%\

Tidal Flat F1-Score = 92.48%\


The classifier is highly reliable and performs well. However, the model occasionally overpredicts tidal flats.


## Scope


The purpose of this package is to provide an easy-to-use tool for conservationist to:


- locate current tidal flat habitats

- quantify habitat loss over time

- identify hotspots for conservation


All of that can be done without training data, computational resources or extensive programming knowledge.\

It can be part of a larger GEE workflow or just used as a standalone tool. The main purpose of this package is to support the conservation of tidal flats, especially for migratory bird.


## Contributions and Context


The model was created as a joint effort by Rosemary Jones, Simon Sacher, Jule Pfeiffer, and Miles Berberich: https://github.com/GebTorte/WWFTidalFlats\

It was created as part of the class "EO in ecology" supervised by Dr. Wegmann for the WWF. 