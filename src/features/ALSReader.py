import pandas as pd
import re

class ALSReader:

    def __init__(self, user_id):
        self.user_id = re.split(r'\D+', user_id)[0]
        self.predictions = pd.read_pickle("data/processed/ALSpredictions.pkl")


    def get_predictions(self):
        try:
            preds = self.predictions.loc[self.predictions['cookieid'].astype('str') == self.user_id]['recommendations'][0]
            preds = pd.DataFrame(preds, columns=["id", "rating"])
            max_pred = preds.rating.astype('float64').max()
            if max_pred >= 1:
                preds["rating"] = preds["rating"] / max_pred
        except KeyError:
            return pd.DataFrame(columns=["id", "rating"])
        return preds
