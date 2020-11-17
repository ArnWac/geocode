from urllib.parse import urlencode
import requests

api_key ='APY_KEY here'

class Error(Exception):
    pass

def gmaps(address, data_type = 'json'):
    endpoint = f'https://maps.googleapis.com/maps/api/geocode/{data_type}'
    params = {'address': address, 'key': api_key, 'language': 'de'}
    url_params = urlencode(params)
    url = f'{endpoint}?{url_params}'
    r = requests.get(url)
    if r.status_code not in range(200, 299):
        return {}
    try:
        results = r.json()['results'][0]['geometry']['location']
        if results is not None:
            return results.get('lat'), results.get('lng')
        raise Error("No results for '%s'" % address)
    except:
        pass