import requests
from pprint import pprint

response = requests.get('https://www.google.com')
pprint(response.status_code)
pprint(response.headers)