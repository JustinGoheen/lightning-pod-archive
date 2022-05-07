import os
from torch.utils.data import DataLoader, random_split
from torchvision import transforms
from torchvision.datasets import MNIST


def _download(datapath):
    dataset = MNIST(datapath, download=True, transform=transforms.ToTensor())
    return dataset


def _fetch_data(datapath):
    if os.listdir(datapath):
        dataset = MNIST(datapath, download=False, transform=transforms.ToTensor())
    else:
        dataset = _download(datapath)
    return dataset


def _split(dataset):
    train_set_size = int(len(dataset) * 0.8)
    test_set_size = len(dataset) - train_set_size
    train, test = random_split(dataset, lengths=[train_set_size, test_set_size])
    return train, test


def get_data(return_loader=True, split=True, num_workers=5):
    rootpath = os.getcwd()
    datapath = "".join([rootpath, "/", "data", "/", "cache"])
    if not os.path.isdir(datapath):
        os.mkdir(datapath)
    dataset = _fetch_data(datapath)
    if not return_loader:
        if not split:
            return dataset
        else:
            train, test = _split(dataset)
            return train, test
    else:
        if not split:
            return DataLoader(dataset, num_workers=num_workers)
        else:
            train, test = _split(dataset)
            train = DataLoader(train, num_workers=num_workers)
            test = DataLoader(test, num_workers=num_workers)
            return train, test
