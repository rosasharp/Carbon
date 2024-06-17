import json
import requests
import urllib.parse


API_KEY = "OHxATlRctIBu8dHAiRIggj3pzhPGGKhj"


def route(API_KEY, add1, add2, vehicle, lp100k, type):
   coordinates = f"{add1[0]},{add1[1]}:{add2[0]},{add2[1]}"


   ROUTE_URL = (
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
   API_URL = f"https://api.tomtom.com/search/2/geocode/{urllib.parse.quote_plus(address)}.json?key={API_KEY}"


   response = requests.get(f"{API_URL}")


   latlong = [
       response.json()["results"][0]["position"]["lat"],
       response.json()["results"][0]["position"]["lon"],
   ]


   return latlong

# if __name__ == "__main__":


#     final = route(
#     API_KEY,
#     geocode(API_KEY, input("First address: ")),
#     geocode(API_KEY, input("Second address: ")),
#     "combustion",
#     "8.7438",
#     "eco",
#     )


#     with open("route.json", "w") as f:
#         json.dump(final, f)


#     kilometers = int(final["routes"][0]["summary"]["lengthInMeters"]) / 1000
#     minutes = int(final["routes"][0]["summary"]["travelTimeInSeconds"]) / 60
#     traffic = int(final["routes"][0]["summary"]["trafficDelayInSeconds"]) / 60


#     print(
#     f"Your destination is {kilometers} kilometers away and it will take {minutes} minutes to get there."
#     )


#     if traffic > 0:
#       print(f"There is a traffic delay of {traffic} minutes.")