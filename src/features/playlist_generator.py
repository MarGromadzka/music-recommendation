from models.ALSReader import ALSReader


class PlaylistGenerator:
    def __init__(self, tags, user_id, playlist_length):
        self.als = ALSReader(user_id)
        self.tags = tags
        self.user_id = user_id
        self.playlist_length = playlist_length

    def get_predictions(self):
        return self.als.get_predictions()



