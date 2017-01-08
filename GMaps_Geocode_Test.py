##### https://github.com/googlemaps/google-maps-services-python
# https://developers.google.com/places/

import googlemaps
from datetime import datetime

gmaps = googlemaps.Client(key='AIzaSyAdFmqaYcof2P1b7UqaCFahdWJ03wismcY')

# Geocoding an address
geocode_result = gmaps.geocode(address='Ленинский проспект, дом 1',
                               language='ru')
for item in geocode_result[0]['address_components']:
    print(item)
# print(geocode_result[0]['address_components'][0])
# print(geocode_result[0]['address_components'][1])
print('Широта места', geocode_result[0]['geometry']['location']['lat'])
print('Долгота места', geocode_result[0]['geometry']['location']['lng'])
