import requests
import ee

def download_classifier() -> ee.Classifier:
    ''''This function downloads the classifier from Github for further usage. It needs no input. It outputs the ee.Classifier used in run_classifier().'''

    def __init__(self):
        self._cl
    geojson = requests.get("https://raw.githubusercontent.com/milesberberich/TidalFlat_Classifier/master/RandomForest.json").json()
    trees = geojson["features"][0]["properties"]["trees"]
    classifier = ee.Classifier.decisionTreeEnsemble(trees)

    return classifier