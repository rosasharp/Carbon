import json
import requests
import urllib.parse


API_KEY = "OHxATlRctIBu8dHAiRIggj3pzhPGGKhj"


def route(API_KEY, add1, add2, vehicle, lp100k, type):
   '''Finds the route between locations using coordinates'''

   coordinates = f"{add1[0]},{add1[1]}:{add2[0]},{add2[1]}"


   ROUTE_URL = (
      #Calculates route with coordinates
       "https://api.tomtom.com/routing/1/calculateRoute/" +
       str(coordinates) +
       "/json?" +
       "&key=" + str(API_KEY) +
       "&vehicleEngineType=" + str(vehicle) +
       "&constantSpeedConsumptionInLitersPerHundredkm=65," + str(lp100k) +
       "&routeType=" + str(type) +
       "&traffic=true"
   )


   response = requests.get(f"{ROUTE_URL}")
   return response.json()


def geocode(API_KEY, address):
   '''Identifies location using coordinates'''

   API_URL = f"https://api.tomtom.com/search/2/geocode/{urllib.parse.quote_plus(address)}.json?key={API_KEY}"

   response = requests.get(f"{API_URL}")

   latlong = [
      #Uses latitude and longitude to find location
       response.json()["results"][0]["position"]["lat"],
       response.json()["results"][0]["position"]["lon"],
   ]
   
   return latlong
