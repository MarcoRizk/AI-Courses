import pandas as pd
from fastapi import Request, FastAPI
from joblib import load
from prometheus_client import Summary
from prometheus_client import start_http_server

from preprocess import preprocess

s = Summary('request_latency_seconds', 'Description of summary')

clf = load('cov19model.joblib')
start_http_server(9095)

app = FastAPI()


@app.post("/")
async def predict(request: Request):
    with s.time():
        body = await request.json()
        row = preprocess(pd.DataFrame(body, index=[0]))

        pred = clf.predict(row).astype(int)[0]

        return {"prediction": bool(pred)}
