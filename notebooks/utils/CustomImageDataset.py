from torch.utils.data import Dataset
from torchvision.io import read_image
import numpy as np
import pandas as pd


class CustomImageDataset(Dataset):
    def __init__(self, annotations_file, img_dir, tags_list):
        self.img_labels = pd.read_csv(annotations_file)
        self.img_dir = img_dir
        self.tags_list = tags_list

    def __len__(self):
        return len(self.img_labels)

    def __getitem__(self, idx):
        img_path = self.img_dir + self.img_labels.iloc[[idx]]["id"].to_string(index=False) + ".png"
        try:
          image = read_image(img_path)
        except RuntimeError:
          return None, None
        label = np.array(self.img_labels.iloc[idx][self.tags_list].tolist())
        return image, label