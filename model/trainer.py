# code example is from:
# https://pytorch-lightning.readthedocs.io/en/latest/common/lightning_module.html

import os
import pytorch_lightning as pl
from torch.utils.data import DataLoader
from torchvision.datasets import MNIST
from torchvision import transforms
from .model import LitModel

if __name__ == "__main__":

    train_loader = DataLoader(MNIST(os.getcwd(), download=True, transform=transforms.ToTensor()))
    trainer = pl.Trainer(max_epochs=1)
    model = LitModel()

    trainer.fit(model, train_dataloaders=train_loader)