# -*- coding: utf-8 -*-
"""
Keep Track of our predictions


I need to take record of what you have predicted about who so that 
it is possible to revisit later on to do come additional analysis 
and possibly compare with the true outcome.

In order to this I will need to sart work with a database. The database
will keep track of the observations, the predictions we have provided
for them as well the true outcome should we be luckly enough to find
out


When working with databases in code, you generally want to be using
a layer of abstraction called ORM. In this case the ORM that I will
be using will be peewee
"""
from flask import Flask, request, jsonify
import json 
import pandas as pd 
import pickle
import joblib
from peewee import (
        Sqlitedatabase, Postgresqldatabase,Model,
        Integerfield, Floatfield, Booleanfield,
        Textfield
        )
from playhouse.shortcuts import model_to_dict

# Begining of Database
'''
Create a sqlite database that will be stored in a file 
called predictions.db
'''
DB = Sqlitedatabase('predictions.db')

'''
Defining the data model
'''
class Prediction(Model):
    observation_id = Integerfield(unique=True)
    observation = Textfield()
    proba = Integerfield()
    true_class = Integerfield(null=True)
    
    class Meta:
        database = DB

'''
This line of code, creates the table that will store the 
information previously mentioned.
'''
DB.create_tables([Prediction],safe=True)

# End of the Database

# Unpickle previous trained Model 
## Deserializing Columns
with open('columns.json', 'r') as fh:
    columns = json.load(fh)

## Unpickle Dtypes
with open('dtypes.pickle', 'rb') as fh:
    dtypes = pickle.load(fh)

## Unpickle Model    
with open('pipeline.pickle', 'rb') as fh:
    pipeline = pickle.load(fh)
    
# End of Unpickling 
    
# Begin Webserver Stuff
jv_capstone_project = Flask(__name__)

@jv_capstone_project.route('/predict', methods = ['POST'])

def predict():
    #receving a new observation 
    obs_dict = request.get_json()
    
    _id = obs_dict['id']

    observation = obs_dict['observation']
    
    obs =  pd.DataFrame([observation],columns=columns).astype(dtypes)
    
    proba = pipeline.predict(obs)
    
    response = {'prediction' : proba}
    
    p = Prediction(
            observation_id = _id,
            proba=proba,
            observation = request.data,
            )
    try:
        p.save()
    except IntegrityError:
        error_msg = "ERROR: observation ID '{}' already exists".format(_id)
        response["error"] = error_msg
        print(error_msg)
        #The line of code I believe it prevents from storing 
        DB.rollback()
    
    return jsonify(response)

# End of WebServer Stuff

if __name__ == "__main__":
    jv_capstone_project.run(debug = True)
    
# Adding Another End Point 
'''
The objective of this endpoint is to receive updates about
predictions that we have judged

This is the step that will enable us to have the true labels
in case they are availables
'''

@jv_capstone_project.route('/update', methods = ['POST'])

def update():
    obs = request.get_json()
    
    try:
        p = Prediction.get(Prediction.observation_id == obs['id'])
        
        p.true_class == obs['true_class']
        
        p.save()
        
        return jsonify(model_to_dict(p))
    
    except Prediction.DoesNotExist:
        error_msg = 'Observation ID: "{}" does not exist'.format(obs['id'])
        
        return jsonify({'error' : error_msg})
