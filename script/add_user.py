# 1-6040
import numpy as np
import pandas  as pd 
import json
import requests
API_ENDPOINT = 'http://localhost:8000/api/auth/register/'
with open('./../import/user_7.json') as json_file:
    data = json.load(json_file)
    for p in data:

        

        user= p['username']
        print(user)
        password =p['password']
        email= p['email']
        data_request={
            'username':user,
            'email': email,
            'password':password
        }
        

        r = requests.post(url = API_ENDPOINT, data = data_request)