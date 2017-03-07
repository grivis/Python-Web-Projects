##### https://github.com/googlemaps/google-maps-services-python
# https://developers.google.com/places/

import googlemaps
from datetime import datetime

gmaps = googlemaps.Client(key='AIzaSyAdFmqaYcof2P1b7UqaCFahdWJ03wismcY')

# Geocoding an address
#geocode_result = gmaps.geocode(address='улица Каховка, дом 31-1, Москва, Россия', language='ru')

#distance_result = gmaps.distance_matrix(origins='ул. Донская, д. 13, стр.1, Москва, Россия',
                                        # destinations='улица Каховка, дом 31-1, Москва, Россия', mode='transit',
                                        # language='ru', avoid=None, units=None, departure_time=datetime.now(),
                                        # arrival_time=None,
                                        # transit_mode=None, transit_routing_preference=None, traffic_model=None)

# Look up an address with reverse geocoding
# reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))

# Request directions via public transit
# now = datetime.now()
# directions_result = gmaps.directions('станция метро Новые Черемушки, Москва, Россия',"улица Каховка, дом 31, Москва, Россия",
#                                     mode="transit",
#                                    departure_time=now)

directions_result = gmaps.directions(origin='улица Каховка, дом 31-1, Москва, Россия', \
                 destination='улица Профсоюзная, дом 136, копус 4, Москва, Россия', mode='transit', \
               language='ru', avoid=None, units=None, departure_time=datetime.now(), arrival_time=None, \
               transit_mode=None,transit_routing_preference=None, traffic_model=None)


# nearby_results = gmaps.places_nearby(location={'lat': 55.65898198029149, 'lng': 37.56774198029149}, radius=2000,
#                                      keyword=None, language='ru',
#                                      min_price=None, max_price=None, name=None, open_now=False, rank_by=None,
#                                      type='subway_station', page_token=None)

#print(geocode_result)
# print(distance_result)
# print('+++')
# print(distance_result['rows'][0]['elements'][0]['distance']['value'])
# print('---')
# print(distance_result['rows'][0]['elements'][0]['duration']['value'])
# print(nearby_results)
# print('---')
# print(nearby_results['results'][0]['geometry']['location'])
# print(nearby_results['results'][0]['vicinity'])
# print(nearby_results['results'][0]['name'])
# print('---')

print (directions_result)

