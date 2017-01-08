##### https://github.com/googlemaps/google-maps-services-python
# https://developers.google.com/places/

import googlemaps
from datetime import datetime

gmaps = googlemaps.Client(key='AIzaSyAdFmqaYcof2P1b7UqaCFahdWJ03wismcY')

# Geocoding an address
revgeocode_result = gmaps.reverse_geocode((55.6576, 37.5663), language='ru')

#print(revgeocode_result)
for level0 in revgeocode_result:
    #print('------>', level0['address_components'])
    for level1 in level0['address_components']:
         print('+++++++++++>', level1)
    print('#######')