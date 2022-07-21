from geopy import Nominatim

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
