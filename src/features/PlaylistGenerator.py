from features.ALSReader import ALSReader
from features.TagsReader import TagsReader
from features.CoreLinkReader import CoreLinkReader
from features.Word2VecReader import Word2VecReader



class PlaylistGenerator:
    def __init__(self, tags, user_id, playlist_length):
        self.als_reader = ALSReader(user_id)
        self.tags_reader = TagsReader(tags)
        self.playlist_length = playlist_length
        self.core_link_reader = CoreLinkReader()
        self.word2vec_reader = Word2VecReader(user_id)

    def get_predictions(self):
        als_predictions = self.als_reader.get_predictions()
        tags_predictions = self.get_mapped_tags_predictions()
        preds = tags_predictions.join(als_predictions.set_index('id'), on='id', how='outer')
        preds["score"] = preds[["sum", "rating"]].sum(axis=1)
        word2vec_pred = self.word2vec_reader.get_songs()
        for song in word2vec_pred:
            preds.loc[preds.index[preds['id'] == song], 'score'] += 1

        return preds.sort_values(by='score', ascending=False).head(self.playlist_length)

    def get_mapped_tags_predictions(self):
        tags_score = self.tags_reader.get_score()
        id_mapping = self.core_link_reader.get_mapping()
        return tags_score.join(id_mapping.set_index('external_id'), on='external_id')

    def get_recommendation(self):
        preds = self.get_predictions()
        link_and_title = self.core_link_reader.get_link_and_title()
        preds = preds.join(link_and_title.set_index('id'), on='id')
        return preds.get(["title", "url", "score"])
