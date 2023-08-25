import pandas as pd


class TagsReader:

    def __init__(self, chosen_tags):
        self.chosen_tags = chosen_tags
        self.tagged_songs = pd.read_csv("data/processed/tagged_songs_round.csv")

    def get_score(self):
        self.tagged_songs["sum"] = self.tagged_songs[self.chosen_tags].sum(axis=1)
        return self.tagged_songs.get(["id", "sum"]).rename(columns={"id": "external_id"})
