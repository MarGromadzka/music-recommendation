import pandas as pd


class ALSReader:

    def __init__(self, user_id):
        self.user_id = user_id
        self.predictions = pd.read_csv("data/processed/ALSpredictions.csv")

    def get_predictions(self):
        return self.predictions.loc[self.predictions['cookieid'].astype('str') == self.user_id]
