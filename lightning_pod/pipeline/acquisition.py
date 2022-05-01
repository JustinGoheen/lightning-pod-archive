import os
from torch.utils.data import DataLoader
from torchvision import MNIST, transforms


def _download(datapath):
    dataset = MNIST(datapath, download=True, transform=transforms.ToTensor())
    return dataset


def _fetch_data(datapath):
    if os.listdir(datapath):
        dataset = MNIST(datapath, download=False, transform=transforms.ToTensor())
    else:
        dataset = _download(datapath)
    return dataset


def get_data(return_loader=True):
    rootpath = os.getcwd()
    datapath = "".join([rootpath, "/", "data", "/", "cache"])
    dataset = _fetch_data(datapath)
    if not return_loader:
        return dataset
    else:
        return DataLoader(dataset)
