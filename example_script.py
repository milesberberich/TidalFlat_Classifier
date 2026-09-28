# ------ 1. Login to GEE -------

import ee
ee.Authenticate()
ee.Initialize(project="lstcalculation")

# ------ 2. Install
from tidalflat_classifier.download_classifier import *
from tidalflat_classifier.run_classifier import *

classifier = download_classifier()

result = run_classifier(path_to_aoi="/home/milesberberich/Documents/uni/wwf/example_aoi2.shp", start_year="2016", end_year="2019", classifier=classifier) # Change your AOI!

url = result.getDownloadURL({'scale': 30,'fileFormat': 'GeoTIFF'})
print(url)