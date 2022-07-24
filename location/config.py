from django.contrib.gis.geos import Point
from geopy import Nominatim
from loguru import logger

place_names = ['municipality', 'subdistrict', 'district', 'town', 'city', 'subregion', 'region', 'county',
                           'state', 'country', ]


additional_place_names = ['country_code', 'iso_3166_2_lvl4', 'postal_code', 'road', 'house_number', ]


def geopy_response(latitude, longitude):
    geolocator = Nominatim(user_agent="travel-attaplace")

    coordinate = f"{latitude}, {longitude}"
    location = geolocator.reverse(coordinate, language='en')
    response = {}
    if location and location.raw:
        response['id'] = location.raw.get('place_id')
        address: dict = location.raw.get('address')
        if address:
            # add postcode key to address
            postcode = address.get('postcode')
            if postcode:
                address['postal_code'] = postcode
            # add name to address
            for pn in place_names:
                if pn in address:
                    address['name'] = address[pn]
                    break
                else:
                    address['name'] = None
            response = {**response, **address}
    return response


def service_to_location_data(validated_data):
    latitude = validated_data.get('latitude')
    longitude = validated_data.get('longitude')

    response = geopy_response(latitude, longitude)
    logger.warning(response)

    for pn in (place_names + additional_place_names):
        for key in response.keys():
            if pn == key:
                continue
            else:
                validated_data[pn] = None

    for key, value in response.items():
        if key in ('id', 'place_id'):
            continue
        if key == 'ISO3166-2-lvl4':
            validated_data['iso_3166_2_lvl4'] = response[key]
            continue
        if key == 'postcode':
            validated_data['postal_code'] = response[key]
            continue
        if key == 'name':
            validated_data['name'] = response['name']
        if key not in (place_names + additional_place_names):
            continue
        validated_data[key] = value

    point = None
    if latitude and longitude:
        point = Point(float(longitude), float(latitude), srid=4326)
    validated_data['point'] = point

    return validated_data
