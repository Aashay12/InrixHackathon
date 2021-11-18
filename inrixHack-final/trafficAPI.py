from numpy import number
import pandas as pd
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


col_list = ["Latitude", "Longitude"]
columns = pd.read_csv('./data/CrimeData.csv', usecols=col_list)
# lat,long = columns['Latitude'],columns['Longitude']
df_1 = columns.loc[2000:4000, ['Latitude', 'Longitude']]
lat, long = df_1['Latitude'], df_1['Longitude']
radius = 1.5

appId, hashToken = "d6c9o7nv6j", "ZDZjOW83bnY2anxOTE1MNHl0STB1MWxBOG1YaHp1YkI4OVZNeHBzaHVrUjNoWGpLZGNz"
url = "https://api.iq.inrix.com/auth/v1/appToken"

getCameraIdsUrl = 'https://api.iq.inrix.com/trafficCamerasInRadius'


res = requests.get(url, params={"appId": appId, "hashToken": hashToken}, headers={
                   'Accept': 'application/json'})

token = json.loads(res.text)
token = token['result']['token']

numberOfCameras = []
for i, j in zip(lat, long):
    print(i, j)
    retry = 0
    # ids = requests.get(getCameraIdsUrl, params={"Token": token, "center": "{}|{}".format(i,j), "radius": radius})
    # print(ids.text)

    # retry_strategy = Retry(
    #     total=3,
    #     status_forcelist=[429, 500, 404,502, 503, 504],
    #     method_whitelist=["HEAD", "GET", "OPTIONS"]
    # )

    # adapter = HTTPAdapter(max_retries=retry_strategy)
    # http = requests.Session()
    # http.mount("https://", adapter)
    # http.mount("http://", adapter)

    ids = requests.get(getCameraIdsUrl, params={
                       "Token": token, "center": "{}|{}".format(i, j), "radius": radius})
    # print(ids.text)
    if ids.status_code == 200:
        cameraIds = parseXML(ids.text)
        numberOfCameras.append(cameraIds)
        print(len(numberOfCameras))
    else:
        numberOfCameras.append(-1)


df = pd.DataFrame({"numberOfCameras": numberOfCameras})
df.to_csv('numberOfCameras.csv')
