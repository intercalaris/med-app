import pandas as pd
import json
import requests

# function to fetch data from API
def fetch_data(query):
    url = "https://uts-ws.nlm.nih.gov/rest/search"
    params = {
        "string": query,
        "ticket": "d859402d493b54d71e4055b0b25687295f07"
    }
    response = requests.get(url, params=params)
    data = json.loads(response.text)
    return data

# function to preprocess data
def preprocess_data(data):
    print(data)
    df = pd.json_normalize(data['result']['results'])

    # convert json to dataframe
    df = pd.json_normalize(data['result']['results'])
    # extract relevant columns
    df = df[['ui', 'name', 'rootSource', 'semanticType', 'description']]
    # rename columns
    df = df.rename(columns={'ui': 'code', 'name': 'diagnosis', 'rootSource': 'source', 'semanticType': 'type', 'description': 'text'})
    # preprocess text column
    df['text'] = df['text'].str.lower()
    df['text'] = df['text'].str.replace('[^\w\s]','')
    # return preprocessed data
    return df

# fetch data from API
data = fetch_data("headache")

# preprocess data
df = preprocess_data(data)
