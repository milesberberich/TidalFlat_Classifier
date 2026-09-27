# TidalFlat_Classifier

## Purpose

**Enables you to detect tidal flat with just two functions!**

A easy package that enables you to implement the approach of [Murray et al. 2018](https://www.nature.com/articles/s41586-018-0805-8) using the _Google-Earth-Engine API_ in Python!
A pretrained Classifier will be used &rarr; no need to collect training data or train a model.

## Contents

The package itself consists of two functions:
- **download_classifier.py:** Downloads a trained Random Forest into your system.
- **run_classifier.py:** After specific the _area of interest (aoi)_ and the start and end year_ of the analysis, it performs the classification.
- **example_script.py**: Shows a example workflow.

