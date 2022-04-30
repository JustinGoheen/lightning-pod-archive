# code example is from:
# https://pytorch-lightning.readthedocs.io/en/latest/common/lightning_module.html


import os
import pytorch_lightning as pl
from torch.utils.data import DataLoader
from torchvision.datasets import MNIST
from torchvision import transforms
from .model import LitModel

if __name__ == "__main__":

    rootpath = os.getcwd()
    datapath = "".join([rootpath, "/", "data", "/", "cache"])

    if not os.path.isdir(datapath):
        os.mkdir(datapath)

    download = True if not os.listdir(datapath) else False

    train_loader = DataLoader(
        MNIST(datapath, download=download, transform=transforms.ToTensor())
    )

    trainer = pl.Trainer(max_epochs=1, fast_dev_run=True)
    model = LitModel()

    trainer.fit(model, train_dataloaders=train_loader)
