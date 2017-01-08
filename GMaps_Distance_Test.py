##### https://github.com/googlemaps/google-maps-services-python
# https://developers.google.com/places/

import googlemaps
from datetime import datetime

gmaps = googlemaps.Client(key='AIzaSyAdFmqaYcof2P1b7UqaCFahdWJ03wismcY')

distance_result = gmaps.distance_matrix(origins='улица Каховка, 31-1',
                                        destinations='Улица Наметкина, 13Б',
                    mode=None, language='ru', avoid=None, units=None,
                    departure_time=None, arrival_time=None, transit_mode=None,
transit_routing_preference=None, traffic_model=None)

print(distance_result['rows'][0]['elements'][0]['distance'])