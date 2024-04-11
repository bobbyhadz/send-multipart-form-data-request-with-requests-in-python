# Python: Sending multipart/form-data request with requests

from pprint import pprint
import requests

url = 'https://httpbin.org/post'

response = requests.post(
    url,
    files={'id': 1, 'site': 'bobbyhadz.com'},
    timeout=30
)

print(response.status_code)
pprint(response.json()['headers'])