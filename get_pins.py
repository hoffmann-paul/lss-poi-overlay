import requests
import json

def get_API_list():
    global response
    global keywords_list

    file = open("keywords.json", "r")
    keywords_list = json.loads(file.read())

    def format_keyword_list():
        string = ""
        for i in keywords_list:
            string += f'nwr["{i['osm-key']}"="{i['osm-tag']}"](area.a); '
        return string

    city = input("Enter City for Search: ")

    data = format_keyword_list()

    query = f"""
    [out:json][timeout:25];
    area["name"="{city}"]["boundary"="administrative"]->.a;
    (
    {data}
    );
    out center;
    """

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

def get_coordinates():
    response_answer = []
    for el in response.json()["elements"]:
        lat_raw = el.get("lat") or el["center"]["lat"]
        lng_raw = el.get("lon") or el["center"]["lon"]
        label = "None"
        tags = el.get("tags", {})
        for i in keywords_list:
            target_key = i["osm-key"]  
            target_val = i["osm-tag"]   
            if tags.get(target_key) == target_val:
                label = i["label"]
                break
        response_answer.append({"lat": float(lat_raw), "lng": float(lng_raw), "label": label})
    return response_answer

def server_request():
    get_API_list()
    return get_coordinates()