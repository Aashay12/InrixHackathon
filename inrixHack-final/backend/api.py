import requests
import json
from utils import polyline_to_coordinates


def getParkingLocations(lat, lon):
    AUTH_URL = "https://api.iq.inrix.com/auth/v1/appToken"
    BLOCKS_API = "https://api.iq.inrix.com/blocks/v3?"

    # Authentication
    appId, hashToken = "lh4c9o50cj", "bGg0YzlvNTBjanxuc0RMZ2hLU2hCYUFTNWIxdllHMWMxbGl3cVA4N0RsNzR0TWtFUE9K"
    response = requests.get(AUTH_URL, params={"appId": appId, "hashToken": hashToken}, headers={
        'Accept': 'application/json'})

    token = json.loads(response.text)
    token = token['result']['token']

    parkingLots = requests.get(BLOCKS_API, params={"point": "{}|{}".format(
        lat, lon), "radius": 50}, headers={"Authorization": "Bearer {}".format(token)})

    parkingLots = json.loads(parkingLots.text)
    coordinates = []
    # print(parkingLots)
    parkingLots = parkingLots['result']
    final = []
    unique = set()
    for i in range(len(parkingLots)):
        obj = parkingLots[i]
        segments = obj["segments"]
        count = 0
        # print(obj)
        if obj['probability']:

            probab = obj["probability"]/100
        else:
            probab = 0

        open_spaces = 0
        overnight = 1
        for s in segments:
            unique.add(s['polyline'])
            points = polyline_to_coordinates(s["polyline"])
            # print(s)
            open_spaces = max(open_spaces, s['spacesTotal'])

            coordinates.append(points)

        count += 1

        temp = [probab, open_spaces, overnight]
        print(count, 'counttt')
        final.append(temp)

    print(coordinates, len(coordinates))
    return coordinates, final


getParkingLocations(37.757386, -122.490667)
