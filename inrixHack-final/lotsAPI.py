import json
import pandas as pd
import requests

# API Request URLs
AUTH_URL = "https://api.iq.inrix.com/auth/v1/appToken"
LOTS_API = "https://api.iq.inrix.com/blocks/v3?"


# Authentication
appId, hashToken = "lh4c9o50cj", "bGg0YzlvNTBjanxuc0RMZ2hLU2hCYUFTNWIxdllHMWMxbGl3cVA4N0RsNzR0TWtFUE9K"
response = requests.get(AUTH_URL, params={"appId": appId, "hashToken": hashToken}, headers={
    'Accept': 'application/json'})

print(response.text)
token = json.loads(response.text)
token = token['result']['token']

# Process data from Lots API

df = pd.read_csv('./data/CrimeData.csv')
with open('sample.json') as json_file:
    res = json.load(json_file)

res = res['result']

data = []

'''
probaility
rateCard
amenities
  Overnight Parking


minPrice,

'''
completeData = []
count = 1
df1 = df.loc[0:200, ['Latitude', 'Longitude']]
latitude, longitude = df1.Latitude, df1.Longitude
# print()
for i, j in zip(latitude, longitude):
    lat, lon = i, j

    req = requests.get(LOTS_API, params={"point": "{}|{}".format(
        lat, lon), "radius": 200}, headers={"Authorization": "Bearer {}".format(token)})

    # print(req.content)
    res = json.loads(req.text)
    if 'result' in res:
        res = res['result']
        # print()
        # break

        for d in res:
            # print(d.keys())
            # break
            segments = d['segments']
            probability = d['probability']
            minPrice = float('inf')
            data = {}
            feat = 0
            spacesTotal = 0

            for i in range(len(segments)):
                structuredRates = segments[i]['structuredRates']
                amenities = segments[i]['amenities']
                spacesTotal = max(spacesTotal, segments[i]['spacesTotal'])
                # rates

                for j in range(len(structuredRates)):
                    rate = structuredRates[j]
                    if rate['rate'] == -1:
                        continue

                    minPrice = min(minPrice, rate['rate'])

                for j in range(len(amenities)):
                    obj = amenities[j]
                    # print(obj['name'])
                    if 'overnight' in obj['name'].lower():
                        feat = 1
                        break

            data['probability'] = probability
            data['rate'] = minPrice
            data['overnight'] = feat
            data['openSpaces'] = spacesTotal
            print(count, i, j, data)
            count += 1
            completeData.append(data)

finalLotsData = pd.DataFrame(completeData)
finalLotsData.to_csv('lotsData.csv')


# for i in completeData:
#     print(i)

# for i in res:
#     obj = i
#     d = {}
#     for j in obj.keys():
#         # print(j)
#         if j == 'probability':
#             d['probability'] = obj[j]
#             # print(d)

#         if j == 'segments':

#             for s in obj[j]:
#                 p1 = 0
#                 for val in s.keys():

#                     if val == 'rateCards':
#                         for k in s[val]:
#                             if 'No Parking' in k:
#                                 continue
#                             elif 'Free' in k:
#                                 d['parkingCost'] = 0
#                                 f = 1
#                                 p1 += 1
#                             else:
#                                 if d['parkingCost']:
#                                     d['parkingCost'] = min(
#                                         d['parkingCost'], int(k[-2:]))
#                                 else:
#                                     d['parkingCost'] = int(k[-2:])
#                                 p1 += 1

#                     if p1 == 2:
#                         break

#                     if val == 'amenities':
#                         for k in s[val]:
#                             if 'Overnight' in k['name']:
#                                 d['overnightParking'] = 1
#                                 f += 1

#                         else:
#                             d['overnightParking'] = 1
#                             f += 1

#                     if f == 2:
#                         break

#     data.append(d)

# for i in data:
#     print(i)
