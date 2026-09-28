# ------ 1. Login to GEE -------

import ee
ee.Authenticate()
ee.Initialize(project="example_project")

# ------ 2. Install

from tidalflat_classifier.download_classifier import *
from tidalflat_classifier.run_classifier import *

classifier = download_classifier()

result = run_classifier(path_to_aoi="/home/your_amazing_area_of_interest.geojson", start_year="2016", end_year="2019", classifier=classifier) # Change your AOI!

url = result.getDownloadURL({'scale': 30,'fileFormat': 'GeoTIFF'})
print(url)