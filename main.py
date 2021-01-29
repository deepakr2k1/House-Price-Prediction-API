# Import Libraries
import uvicorn
from fastapi import FastAPI
from HouseFeatures import HouseFeatures
import pandas as pd
import numpy as np
import pickle

# Create the app object
app = FastAPI()
model = pickle.load(open("model.pickle","rb"))
columns = pd.read_csv('columns.csv')
columns.drop('Unnamed: 0', axis=1, inplace=True)

# Index route, opens automatically on http://127.0.0.1:8000
@app.get('/')
def index():
    return {'Welcome to House Price Prediction API'}

# Expose the prediction functionality, make a prediction from the passed JSON data and return the predicted Price
@app.post('/predict')
def predict_price(data: HouseFeatures):
    data = data.dict()
    X = pd.DataFrame(columns = columns.columns)
    X = X.append(pd.Series(), ignore_index = True)
    X['total_sqft'] = data['total_sqft']
    X['bath'] = data['bath']
    X['BHK'] = data['bhk']
    if data['location'] in X.columns:
        X[data['location']]=1
    X.fillna(0, inplace = True)
    return (model.predict(X)[0]);

#   Run the API with uvicorn
#   Will run on http://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)

#   run cmd: uvicorn main:app --reload