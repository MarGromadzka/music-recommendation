from CustomImageDataset import CustomImageDataset
import torch
import numpy as np
from sklearn.metrics import multilabel_confusion_matrix
import pandas as pd
import time

def train_model(model, device, optimizer, criterion, tags_list, epochs):
    for epoch in range(epochs):
        for index in range(4, 180):
            img_path = f"/content/sorted_spec/content/drive/MyDrive/musicrecom/sorted_spectrograms/{index}/"
            tags_path = f"/content/drive/MyDrive/musicrecom/melodice/tags/tagged_music_after_drop_{index}.csv"
            train_dataset = CustomImageDataset(tags_path, img_path, tags_list)
            train_loader = torch.utils.data.DataLoader(train_dataset, batch_size=64, shuffle=True)
            for i, data in enumerate(train_loader, 0):
                inputs, labels = data
                inputs, labels = inputs.to(device).to(torch.float32), labels.to(device).to(torch.float32)
                optimizer.zero_grad()
                outputs = model(inputs)
                loss = criterion(outputs, labels)
                loss.backward()
                optimizer.step()
    return model


def test_model(model, device, tags_list):
    tp = 0
    tn = 0
    fp = 0
    fn = 0
    total = 0
    model.eval()
    with torch.no_grad():
        for i in range(0, 4):
            img_path = f"/content/sorted_spec/content/drive/MyDrive/musicrecom/sorted_spectrograms/{i}/"
            tags_path = f"/content/drive/MyDrive/musicrecom/melodice/tags/tagged_music_after_drop_{i}.csv"
            test_dataset = CustomImageDataset(tags_path, img_path, tags_list)
            test_loader = torch.utils.data.DataLoader(test_dataset, shuffle=True)
            for batch_i, (data, target) in enumerate(test_loader):
                pred = model(data.to(device).to(torch.float32))
                pred = np.array(pred.cpu() > 0.5, dtype=float)
                total += target.size(0)*21
                conf_mat = multilabel_confusion_matrix(target.to(torch.float32), pred)
                for label in conf_mat:
                    tp += label[1][1]
                    tn += label[0][0]
                    fp += label[0][1]
                    fn += label[1][0]
    return tp, tn, fp, fn, pred


def print_metrics(tp, tn, fp, fn):
    print(f"Accuracy: {(tp + tn) / (tp + tn + fp + fn)}")
    print(f"Precision: {tp / (tp + fp)}")
    print(f"Recall: {tp / (tp + fn)}")


def save_metrics(params, tp, tn, fp, fn, dir_path):
    params["tp"] = tp
    params["tn"] = tn
    params["fp"] = fp
    params["fn"] = fn
    params["accuracy"] = (tp + tn) / (tp + tn + fp + fn)
    params["precision"] = tp / (tp + fp)
    params["recall"] = tp / (tp + fn)
    params_str = {key: str(params[key]) for key in params.keys()}
    df = pd.DataFrame(params_str, index=[0])
    df.to_csv(dir_path + str(time.time()) + ".csv")

