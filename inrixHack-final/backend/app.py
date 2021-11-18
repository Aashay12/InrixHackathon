from flask import Flask, render_template, request, redirect, session
from flask_cors import CORS
import json
import os
from api import getParkingLocations
from utils import process_data
from model_predict import model_predict
from utils import governmentData

app = Flask(__name__)
app.secret_key = 'any'
CORS(app)


@app.route('/govern')
def route():
    lat, lon, ranks = governmentData()
    print(lat)
    return render_template('index3.html', lat=list(lat), lon=list(lon), ranks=list(ranks))


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        post_lat = request.form['lat']
        post_long = request.form['long']
        locations, final = getParkingLocations(
            37.77074774, -122.42485259999998)
        crime, num_cameras = process_data()
        # crime = [5000 for i in range(len(final))]
        # num_cameras = [0 for i in range(len(final))]
        for i in range(len(final)):

            final[i].append(crime[i])
            final[i].append(num_cameras[i])

        r = list(model_predict(final[:2], './finalized_model.sav'))

        print(final, "final")
        ranks = []
        for i in range(len(final)):
            final[i].extend(locations[i])

        r1 = list(model_predict(
            final[2:], './finalized_model_with_LatLong.sav'))
        finalRanks = r.extend(r1)
        print(finalRanks)
        print(r, 'rankkkk')
        print(r1, 'rankkkk')

        return render_template('index2.html', lat=post_lat, lng=post_long, locations=locations, ranks=[1, 1, 1, 2, 1, 1])


if __name__ == "__main__":
    app.run(debug=True)
