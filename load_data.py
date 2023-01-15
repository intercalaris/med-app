import requests
import json
import pandas as pd

def fetch_data(query):
    url = "https://uts-ws.nlm.nih.gov/rest/search"
    params = {
        "string": query,
        "ticket": "d859402d493b54d71e4055b0b25687295f07"
    }
    response = requests.get(url, params=params)
    data = json.loads(response.text)
    return data

def load_data(query):
    data = fetch_data(query)
    data_frame = pd.json_normalize(data['result'])
    return data_frame