

# make API requests here
# need to retrieve 

import json
import requests
from config import api_key



url = "http://www.ctabustracker.com/bustime/api/v2/"


routes = "getroutes?key="
vehicles = "getvehicles?key="

#http://ctabustracker.com/bustime/api/v2/getstops?key=89dj2he89d8j3j3ksjhdue93j&rt=20&dir=East%20Bound&format=json

# Build query URL
query_url = url + + api_key + "&q=" + city

weather_response = requests.get(query_url)
weather_json = weather_response.json()




