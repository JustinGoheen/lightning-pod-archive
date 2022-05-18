import os
from lightning_pod.pipeline.datamodule import LitDataModule


def test_module_not_abstract():
    _ = LitDataModule()


def test_setup():
    data_module = LitDataModule()
    data_module.setup()
    data_keys = ["train_data", "test_data", "val_data"]
    assert all([key in dir(data_module) for key in data_keys])
