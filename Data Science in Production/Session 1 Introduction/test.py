import json
import unittest

import pandas as pd
from fastapi.testclient import TestClient

from preprocess import preprocess
from webapi import app

client = TestClient(app)


def test_successful_response():
    df = pd.read_csv('data/dataset.csv')
    json_row = json.loads(df.loc[0].to_json())

    response = client.post("/", json=json_row)
    assert response.status_code == 200
    assert "prediction" in response.json()


class TestPrerocessing(unittest.TestCase):
    def test_preprocess_no_target(self):
        df = pd.read_csv('data/dataset.csv')
        processed_df = preprocess(df, include_target=False)
        self.assertFalse("SARS-Cov-2 exam result" in processed_df.columns)

    def test_preprocess_with_target(self):
        df = pd.read_csv('data/dataset.csv')
        processed_df = preprocess(df, include_target=True)
        self.assertTrue("SARS-Cov-2 exam result" in processed_df.columns)
