import numpy as np
import pandas  as pd 
import json
import requests
URL = 'http://localhost:8000/api/cat/'
f = open("./../import/list_cat.txt",'r')


for i in f:   
    print(i.split(":")[1].split("\n")[0])
    data_request={


        'Name' :str(i.split(":")[1].split("\n")[0]),

    }

    r = requests.post(url = URL, data = data_request)