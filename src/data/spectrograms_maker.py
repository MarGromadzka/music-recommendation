import pandas as pd
import os
from pydub import AudioSegment
import tempfile
import librosa
import matplotlib.pyplot as plt
import numpy as np
from math import floor

external_disk_path = "../../../../../../Volumes/Elements SE/melodice/raw_audio"

files_names = pd.read_csv("../../data/processed/core_link.csv")["external_id"].array

fragment_length = 15


if __name__ == "__main__":
    for file in files_names:
        if os.path.exists(f"../../data/processed/spectrograms/{file}_{0}.png"):
            continue
        counter = 0
        try:
            mp3_audio = AudioSegment.from_file(external_disk_path + f"/{file}.mp3", format="mp3")  # read mp3
        except Exception as e:
            continue

        with tempfile.NamedTemporaryFile(suffix=".wav", delete=True) as tmpfile:
            mp3_audio.export(tmpfile.name, format="wav")
            audio, sr = librosa.load(tmpfile.name, sr=44100)

        for i in range(0, floor(audio.size/(sr * fragment_length))):
            start = sr*i*fragment_length
            stop = sr*(i+1)*fragment_length
            fragment = audio[start:stop]
            melspec = librosa.feature.melspectrogram(y=fragment, sr=sr)
            fig, ax = plt.subplots()
            S_dB = librosa.power_to_db(melspec, ref=np.max)
            img = librosa.display.specshow(S_dB, x_axis='time',
                                           y_axis='mel', sr=sr,
                                           fmax=8000, ax=ax)
            fig.colorbar(img, ax=ax, format='%+2.0f dB')
            try:
                plt.savefig(f"../../data/processed/spectrograms/{file}_{i}.png")
            except Exception as e:
                pass
            plt.clf()
            plt.close()
            ax.cla()
            del melspec
        del audio, sr
