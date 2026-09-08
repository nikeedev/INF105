#!/usr/bin/python3
import requests, json

api = "https://api.met.no/weatherapi/locationforecast/2.0/compact?lat=60.3825550&lon=5.3334599&altitude=11"

x = requests.get(api, headers = {"User-Agent": "weather.py/1.0 by nikeedev"});
 
weather = json.loads(x.text)

# print(x.text)

print(f"\n{"."*30}\n")
print(f"Været på Høytek (\"Høyteknologisenteret\")\n")
print(f"Temperatur: {weather["properties"]["timeseries"][0]["data"]["instant"]["details"]["air_temperature"]} C grader")
print(f"Relativ fuktighet (RH): {weather["properties"]["timeseries"][0]["data"]["instant"]["details"]["relative_humidity"]}%")
print(f"Vindstyrke: {weather["properties"]["timeseries"][0]["data"]["instant"]["details"]["wind_speed"]} m/s\n")
print(f"\n{"."*30}\n")

