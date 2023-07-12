import pickle

import os
import sys

with open('../model_v2.pkl', 'rb') as f:
        rf = pickle.load(f)

def make_prediction(input_data:list):
    new_variables = [input_data]
    return int(rf.predict(new_variables)[0])

