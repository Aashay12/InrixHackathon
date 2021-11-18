import pandas as pd
import numpy as np
import requests
import json
import xml.etree.ElementTree as ET


def parseXML(xml):
    cameraIDs = []
    noOfCameras = 0
    tree = ET.ElementTree(ET.fromstring(xml))
    root = tree.getroot()
    # print(xml, root.tag)
    for i in root:
        if i.tag == 'Cameras':
            for j in i:
                if j.tag == 'Camera':
                    attrib = j.attrib
                    noOfCameras += 1

    return noOfCameras


appId, hashToken = "ekfy78zqa6", "ZWtmeTc4enFhNnxSb2pvSlFMYkxNNTBuVU9xQkRYcWZhY2QxWEFFTDgyUDRsa1pxdVdR"
url = "https://api.iq.inrix.com/auth/v1/appToken"

res = requests.get(url, params={"appId": appId, "hashToken": hashToken}, headers={
                   'Accept': 'application/json'})
token = json.loads(res.text)
token = token['result']['token']

getCameraIdsUrl = 'https://api.iq.inrix.com/trafficCamerasInRadius'
getCameraImage = 'https://api.iq.inrix.com/trafficCameraImage'
getTripsUrl = 'https://api.iq.inrix.com/v1/trips'


col_list = ["Latitude", "Longitude"]
columns = pd.read_csv('Crime.csv', usecols=col_list)


lat, long = 37.743431, -122.431100
radius = 1.5

# 37.742631 -122.431022

final = []

# for i, j in zip(lat, long):

ids = requests.get(getCameraIdsUrl, params={"Token": token, "center": "{}|{}".format(
    lat, long), "radius": radius})

print(ids.text)

cameraIds = parseXML(ids.text)
final.append(cameraIds)

print(final)
