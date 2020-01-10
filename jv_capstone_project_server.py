from flask import Flask, request, jsonify
import json 
import pandas as pd 
import pickle
import joblib

jv_capstone_project = Flask(__name__)

''' 
I think the server has been created but it does not do anything 
yet
    
In order to do stuff I need to add http endpoints to 
it

If I'm not able to build a custom transformer 
I think I have to introduce the functions for the pre-processing here
and add the process in the predict function.
'''

# Deserializing Columns
with open('columns.json', 'r') as fh:
    columns = json.load(fh)

# Un-pickle Dtypes
with open('dtypes.pickle', 'rb') as fh:
    dtypes = pickle.load(fh)

# Deserializing pipeline
model_fitted = joblib.load('pipeline.pickle')

@jv_capstone_project.route('/predict', methods = ['POST'])

def predict():
    #receving a new observation 
    payload = request.get_json()
    obs = pd.DataFrame([payload],columns=columns).astype(dtypes)
    
    proba = model_fitted.predict(obs)
    return jsonify({'prediction' : proba
                    })

if __name__ == "__main__":
    jv_capstone_project.run(debug = True)
    
    
