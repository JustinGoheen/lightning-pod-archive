"""
This module serves to consolidate basic use cases of PyTorch Lightning and to test
functionality of this template using an encoder-decoder on MNIST. Documentation links are provided below.

example code: https://pytorch-lightning.readthedocs.io/en/latest/model/train_model_basic.html
Trainer: https://pytorch-lightning.readthedocs.io/en/latest/common/trainer.html
Reproducibility: https://pytorch-lightning.readthedocs.io/en/latest/common/trainer.html#reproducibility
TensorBoardLogger: https://pytorch-lightning.readthedocs.io/en/latest/api/pytorch_lightning.loggers.tensorboard.html#tensorboard
SimpleProfiler: https://pytorch-lightning.readthedocs.io/en/latest/api/pytorch_lightning.profiler.SimpleProfiler.html#simpleprofiler
ModelCheckpoint: https://pytorch-lightning.readthedocs.io/en/latest/api/pytorch_lightning.callbacks.ModelCheckpoint.html#modelcheckpoint
"""

import os
from pytorch_lightning import Trainer, seed_everything
from lightning_pod.network.module import LitModel, Encoder, Decoder
from lightning_pod.pipeline.data_loader import get_data
from pytorch_lightning.loggers import TensorBoardLogger
from pytorch_lightning.profiler import SimpleProfiler
from pytorch_lightning.callbacks import ModelCheckpoint

if __name__ == "__main__":

    # GET CURRENT WORKING DIRECTORY
    cwd = os.getcwd()
    # SET LOGGER
    logs_dir = "".join([cwd, "/", "logs"])
    logger = TensorBoardLogger(save_dir=logs_dir, name="lightning_logs")
    # SET PROFILER
    profile_dir = "".join([logs_dir, "/", "profiler"])
    profiler = SimpleProfiler(dirpath=logs_dir, filename="profiler", extended=True)
    # SET CHECKPOINT DIRECTORY
    chkpt_dir = "".join([cwd, "/", "models"])
    checkpoint_callback = ModelCheckpoint(dirpath=chkpt_dir, filename="model")
    # SET CALLBACKS
    callbacks = [checkpoint_callback]
    # SET SEED
    seed_everything(42, workers=True)
    #  GET DATALOADER
    train_loader, test_loader = get_data(return_loader=True, split=True, num_workers=5)
    #  SET MODEL
    autoencoder = LitModel(Encoder(), Decoder())
    # SET TRAINER
    trainer = Trainer(
        max_epochs=5,
        limit_train_batches=0.25,  # reduce training time of example
        enable_checkpointing=True,  # default
        deterministic=True,  # for reproducibility
        logger=logger,
        profiler=profiler,
        callbacks=callbacks,
    )
    # TRAIN MODEL https://pytorch-lightning.readthedocs.io/en/stable/common/trainer.html#fit
    trainer.fit(model=autoencoder, train_dataloaders=train_loader)
