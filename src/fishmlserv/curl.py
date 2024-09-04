import requests
import json

def ans_get(l, w, url="http://localhost:8765/fish_ml_predictor"):
    headers = {
        'accept': 'application/json',
    }

    params = {
        'length': l,
        'weight': w,
    }

    response = requests.get(url, params=params, headers=headers)
    data = json.loads(response.text)
    r=data['prediction']
    
    return r
