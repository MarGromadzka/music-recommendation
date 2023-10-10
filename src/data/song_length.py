from mutagen.mp3 import MP3
import pandas as pd
from math import floor


if __name__ == "__main__":

    external_disk_path = "../../../../../../Volumes/Maxtor/raw_audio/"
    files_names = pd.read_csv("../../data/processed/core_link.csv")["external_id"].array
    columns_names = ['id', 'length', 'no_spec']

    df = pd.DataFrame(columns=columns_names)
    try:
        for file in files_names:
            try:
                audio = MP3(external_disk_path + file + ".mp3")
                song_length = audio.info.length
            except Exception as e:
                continue
            length = len(df)
            print(length)
            df.loc[length] = [file, song_length, floor(song_length / 15)]
    except Exception:
        df.to_csv("../../data/processed/songs_length.csv")

    df.to_csv("../../data/processed/song_length.csv")
