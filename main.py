import requests
from pprint import pprint

response = requests.get('https://www.google.com')
pprint(response.status_code)
pprint(response.headers)

pprint("a message from the collaborator in a new branch to test the pull request")