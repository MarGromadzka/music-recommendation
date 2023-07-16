from musicnn.extractor import extractor
import pandas as pd


if __name__ == "__main__":
    file_path = "../../../../../../Volumes/Elements SE/melodice/raw_audio"

    external_disk_path = "../../../../../../Volumes/Maxtor/raw_audio/"
    files_names = pd.read_csv("../../data/processed/core_link.csv")["external_id"].array

    columns_names = ['id', 'guitar', 'classical', 'slow', 'techno', 'strings', 'drums', 'electronic', 'rock', 'fast', 'piano', 'ambient', 'beat', 'violin', 'vocal', 'synth', 'female', 'indian', 'opera', 'male', 'singing', 'vocals', 'no vocals', 'harpsichord', 'loud', 'quiet', 'flute', 'woman', 'male vocal', 'no vocal', 'pop', 'soft', 'sitar', 'solo', 'man', 'classic', 'choir', 'voice', 'new age', 'dance', 'male voice', 'female vocal', 'beats', 'harp', 'cello', 'no voice', 'weird', 'country', 'metal', 'female voice', 'choral']
    df = pd.DataFrame(columns=columns_names)
    try:
        for file in files_names:
            try:
                taggram, tags, features = extractor(external_disk_path + file + ".mp3", model='MTT_musicnn', extract_features=True)
            except Exception as e:
                continue
            length = len(df)
            print(length)
            df.loc[length] = [file] + [max(taggram[:, i]) for i in range(0, len(columns_names) - 1)]
    except Exception:
        df.to_csv("../../data/processed/tagged_music.csv")

    df.to_csv("../../data/processed/tagged_music.csv")
