<img src="migratory_bird" align="right" width="250" alt="Tidal Flats Classifier Logo or Demo">

# TidalFlats_Classifier

<h2 style="overflow: hidden;">Purpose</h2>

**Enables you to detect tidal flats with just two functions!**

A user-friendly package that enables you to implement the approach of [Murray et al. 2018](https://www.nature.com/articles/s41586-018-0805-8) using the _Google Earth Engine API_ in Python!\
A pretrained classifier is included &rarr; no need to collect training data or train a model.

**Meant to support the conservation of migratory birds that rely on tidal flats as resting places.**

<h2 style="overflow: hidden;">Contents</h2>

The package itself consists of two functions:
- **download_classifier.py:** Downloads a trained Random Forest into your system.
- **run_classifier.py:** After specifying the _area of interest (aoi)_ and the _start and end year_ of the analysis, it performs the classification.
- **example_script.py**: Shows a simple example workflow.

<h2 style="overflow: hidden;">Requirements</h2>

- Google Earth Engine account
- Google Cloud project ID (for GEE authentication)
- Python >= 3.13

<br clear="right"/>

## Installation & Setup

The package can be installed via the terminal using:

```bash
pip install git+[https://github.com/milesberberich/TidalFlat_Classifier.git](https://github.com/milesberberich/TidalFlat_Classifier.git)