# code example is from:
# https://pytorch-lightning.readthedocs.io/en/latest/common/lightning_module.html


import os
import pytorch_lightning as pl
from lightning_pod.network.model import LitModel
from lightning_pod.pipeline.acquisition import get_data

if __name__ == "__main__":

    train_loader = get_data(dataset_name="mnist", return_loader=True)

    trainer = pl.Trainer(max_epochs=1, fast_dev_run=True)
    model = LitModel()

    trainer.fit(model, train_dataloaders=train_loader)
