

MAPS_API_KEY = "YOUR_API_KEY"

## load libraries
import requests
import json
import pandas as pd
import zipfile

location_types = ["pharmacies", "hospitals"]
cities = ["hatay", "adana", "diyarbakir", "gaziantep", "iskenderun", "mersin", "sanliurfa", "osmaniye", "malatya","adiyaman"]

for city in cities:
    for location_type in location_types:
        url = 'https://maps.googleapis.com/maps/api/place/textsearch/json?query=' + location_type + '+in+' + city + '&key=' + MAPS_API_KEY
        print(url)
        response = requests.get(url)
        data = json.loads(response.text)
        df = pd.DataFrame(data['results'])
        df.head()
        # save to csv
        df.to_csv(location_type + '_in_' + city + '.csv', index=False)
# zip the files
with zipfile.ZipFile('locations.zip', 'w') as myzip:
    for city in cities:
        for location_type in location_types:
            myzip.write(location_type + '_in_' + city + '.csv')