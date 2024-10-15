from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

# Using FWI : fire weather index

# import ridge regressor and standard scaler pickle files

ridge_model = pickle.load(open('Models/ridge.pkl', 'rb'))
standard_scaler = pickle.load(open('Models/scaler.pkl', 'rb'))


app = Flask(__name__)
#app = application

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictdata', methods=['GET','POST'])
def predict_datapoint():
    if request.method == 'POST':
        Temperature = float(request.form.get('Temperature')) 
        RH = float(request.form.get('RH'))    # Relative Humidity
        Ws = float(request.form.get('Ws'))   # Wind Speed
        Rain = float(request.form.get('Rain')) # Rainfall
        FFMC = float(request.form.get('FFMC')) # Fine Fuel Moisture Code
        DMC = float(request.form.get('DMC')) # Duff Moisture Code
        ISI = float(request.form.get('ISI')) # Initial Spread Index
        Classes = float(request.form.get('Classes')) # Classes
        Region = float(request.form.get('Region')) # Region

        new_data_scaled = standard_scaler.transform([[Temperature, RH, Ws, Rain, FFMC, DMC, ISI, Classes, Region]])
        result = ridge_model.predict(new_data_scaled)

        return render_template('home.html', results = result[0])


    else:
        return render_template('home.html')

if __name__ == '__main__':
    app.run(host = "0.0.0.0")