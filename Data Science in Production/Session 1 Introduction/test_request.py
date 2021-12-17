import json

import pandas as pd
import requests

df = pd.read_csv('data/dataset.csv')
for i in df.index:
    json_row = json.loads(df.loc[i].to_json())
    req = requests.post('http://localhost:8000/', json=json_row)
    print(f"Prediction:{req.json()['prediction']}")
