import requests
import ee

def download_classifier():

    def __init__(self):
        self._cl
    geojson = requests.get("https://raw.githubusercontent.com/milesberberich/TidalFlat_Classifier/master/RandomForest.geojson").json()
    trees = geojson["features"][0]["properties"]["trees"]
    classifier = ee.Classifier.decisionTreeEnsemble(trees)

    return classifier