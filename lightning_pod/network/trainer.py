# code example is from:
# https://pytorch-lightning.readthedocs.io/en/latest/model/train_model_basic.html


import pytorch_lightning as pl
from lightning_pod.network.model import LitModel, Encoder, Decoder
from lightning_pod.pipeline.acquisition import get_data

if __name__ == "__main__":

    #  get dataloader
    train_loader = get_data(return_loader=True)
    # trainer https://pytorch-lightning.readthedocs.io/en/stable/common/trainer.html#trainer-flags
    trainer = pl.Trainer(max_epochs=1, fast_dev_run=True)
    # model https://pytorch-lightning.readthedocs.io/en/stable/common/lightning_module.html#lightningmodule-api
    autoencoder = LitModel(Encoder(), Decoder())
    # train model https://pytorch-lightning.readthedocs.io/en/stable/common/trainer.html#fit
    trainer.fit(model=autoencoder, train_dataloaders=train_loader)
