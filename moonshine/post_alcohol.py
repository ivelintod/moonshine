import requests

# Could be other port...
URL = 'http://localhost:8000/api/{alcohol}/'

# Could be input or whatever....
beers = [
    {
        'name': 'Heineken',
        'beer_type': 'AL',
        'description': 'valid beer'
    },
    {
        'name': 'CrapBeer',
        'beer_type': 'bla',
        'description': 'invalid beer'
    }
]

whiskeys = [
    {
        'name': 'Evan Williams',
        'whiskey_type': 'BR',
        'description': 'valid whiskey'
    },
    {
        'name': 'CrapWhiskey',
        'whiskey_type': 'crap',
        'description': 'invalid whiskey'
    }
]

alcohol_types = {
    'beer': beers,
    'whiskey': whiskeys
}


for alcohol_type in alcohol_types:
    url = URL.format(alcohol=alcohol_type)
    for instance in alcohol_types[alcohol_type]:
        resp = requests.post(url,
                             json=instance,
                             headers={'Content-Type': 'application/json'})
        print(resp.json())
