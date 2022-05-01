# code example is from:
# https://pytorch-lightning.readthedocs.io/en/latest/model/train_model_basic.html

import os
import pytorch_lightning as pl
from lightning_pod.network.model import LitModel, Encoder, Decoder
from lightning_pod.pipeline.acquisition import get_data

if __name__ == "__main__":

    # data
    train_loader = get_data(return_loader=True)
    # trainer
    trainer = pl.Trainer(max_epochs=1, fast_dev_run=True)
    # model
    autoencoder = LitModel(Encoder(), Decoder())
    # train model
    trainer.fit(model=autoencoder, train_dataloaders=train_loader)
