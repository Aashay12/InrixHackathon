import pandas
import polyline
import pandas as pd
import random
random.seed(10)


def polyline_to_coordinates(p):
    return list(polyline.decode(p, 5)[0])


def process_data():
    df = pd.read_csv('./dataWithRanks.csv')
    num_cameras = df.numberOfCameras
    num_crime = df.Crime
    random_cameras = random.choices(num_cameras, k=200)
    random_crime = random.choices(num_crime, k=200)
    # print(random_crime, random_cameras)
    return random_cameras, random_crime


def governmentData():
    df = pd.read_csv('.dataWithRanks.csv')
    lat, lon = df.Latitude, df.Longitude
    ranks = df.ranks

    return [lat, lon, ranks]


process_data()
