import pandas as pd

class ALSReader:

    def __init__(self, user_id):
        self.user_id = user_id
        self.predictions = pd.read_pickle("data/processed/ALSpredictions.pkl")


    def get_predictions(self):
        try:
            preds = self.predictions.loc[self.predictions['cookieid'].astype('str') == self.user_id]['recommendations'][0]
        except KeyError:
            return pd.DataFrame(columns=["id", "rating"])
        return pd.DataFrame(preds, columns=["id", "rating"])