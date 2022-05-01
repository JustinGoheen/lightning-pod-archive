import os
from torch.utils.data import DataLoader
from datasets import load_dataset


def get_data(dataset_name="mnist", return_loader=True):
    rootpath = os.getcwd()
    datapath = "".join([rootpath, "/", "data", "/", "cache"])
    dataset = load_dataset(dataset_name, cache_dir=datapath)
    if not return_loader:
        return dataset
    else:
        return DataLoader(dataset)
