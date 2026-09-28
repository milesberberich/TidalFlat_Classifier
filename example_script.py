
# ------ 1. Login to GEE -------
import ee
ee.Authenticate()
ee.Initialize(project="example_project")

# ------ 2. Install tidalflat_classifier ------
from tidalflat_classifier.download_classifier import *
from tidalflat_classifier.run_classifier import *

# ------ 3. Download Tidal Flat Classifier -------
classifier = download_classifier()

# ------- 4. Run Classifier ----------
result = run_classifier(path_to_aoi="/home/your_amazing_area_of_interest.geojson", # define your aoi
                        start_year="2016", end_year="2019", classifier=classifier) # define your needed time, always use three-year-intervalls

# ------ 5. Download results ----------
url = result.getDownloadURL({'scale': 30,'fileFormat': 'GeoTIFF'})
print(url) # just copy URL to browser and download results (in EPSG:4326)