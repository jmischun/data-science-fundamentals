import os
import requests

payload = {
    'client_id': os.environ['FOURSQUARE_ID'],
    'client_secret': os.environ['FOURSQUARE_SECRET'],
    'v': '20160101'
}

query = {
    'near': 'Seattle, WA',
    'limit': 10,
    'time': 'any',
    'day': 'any',
    'offset': 3
}

res = requests.get('https://api.foursquare.com/v2/venues/explore', params={**payload, **query})
data = res.json()