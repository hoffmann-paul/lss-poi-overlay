import requests

city = input("Enter City for Search: ")

query = f"""
[out:json][timeout:25];
area["name"="{city}"]["boundary"="administrative"]->.a;
(
  nwr["amenity"="school"](area.a);
);
out center;
"""

import requests

headers = {
    "User-Agent": "lss-poi-overlay/1.0 (paulhoffmann410@gmail.com)",
    "Accept": "application/json",
}

response = requests.post(
    "https://overpass-api.de/api/interpreter",
    data={"data": query},
    headers=headers,
    timeout=60,
)
response.raise_for_status()

for el in response.json()["elements"]:
    lat = el.get("lat") or el["center"]["lat"]
    lon = el.get("lon") or el["center"]["lon"]
    print(el.get("tags", {}).get("name"), lat, lon)

def get_coordinates():
    
    return [
        {"lat": 52.9667, "lng": 11.15, "label": "Lüchow"},
        {"lat": 52.5200, "lng": 13.4050, "label": "Berlin"},
    ]