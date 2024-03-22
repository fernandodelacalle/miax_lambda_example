import pandas as pd
import requests
import json
import os


class BMEApiHandler:

    def __init__(self):
        self.url_base = 'https://miax-gateway-jog4ew3z3q-ew.a.run.app'
        self.competi = 'mia_12'
        self.user_key = os.getenv("MIAX_API_KEY")

    def get_close_data(self, tck) -> pd.Series:
        url = f'{self.url_base}/data/time_series'
        params = {
            'market': 'IBEX',
            'key': self.user_key,
            'ticker': tck
        }
        response = requests.get(url, params)
        tk_data = response.json()
        series_data = pd.read_json(tk_data, typ='series')
        return series_data
