from gensim.models import KeyedVectors
import pandas as pd


class Word2VecReader:

    def __init__(self, user_id):
        self.wv = KeyedVectors.load("models/wv/word2vec.wordvectors", mmap='r')
        self.user_song = pd.read_csv('data/processed/user_songs.csv')
        self.user_id = user_id

    def _get_similar_users(self):
        try:
            return [user[0] for user in self.wv.most_similar(positive=[self.user_id])[0:3]]
        except KeyError:
            return []

    def get_songs(self):
        similar_users = self._get_similar_users()
        similar_songs = []
        for user in similar_users:
            similar_songs += self.user_song[self.user_song["cookieid"] == user].sort_values(["count"], ascending=False).head(3)[
                "link_id"].tolist()
        return similar_songs
