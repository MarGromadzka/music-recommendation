import pandas as pd


class CoreLinkReader:

    def __init__(self):
        self.core_link = pd.read_csv("data/processed/core_link.csv")

    def get_mapping(self):
        return self.core_link.get(["id", "external_id"])

    def get_link_and_title(self):
        return self.core_link.get(["id", "title", "url"])
