import os
import errno
import torch
import hydra
from pathlib import Path
from torch.utils.data import TensorDataset
from pytorch_lightning import Trainer, seed_everything
from pytorch_lightning.loggers import TensorBoardLogger
from pytorch_lightning.profiler import PyTorchProfiler
from pytorch_lightning.callbacks import ModelCheckpoint, EarlyStopping
from lightning_pod.network.module import LitModel
from lightning_pod.pipeline.datamodule import LitDataModule


def create_target_path(filepath, target_directory):
    sep = os.path.sep
    real_path = os.path.realpath(filepath).split(sep)
    real_path = list(reversed(real_path))
    if target_directory in real_path:
        target_path_idx = real_path.index(target_directory) - 1
        target_path = filepath.parents[target_path_idx]
        return target_path
    else:
        raise NotADirectoryError(
            errno.ENOENT, os.strerror(errno.ENOENT), target_directory
        )


# SET PATHS
filepath = Path(__file__)
NETWORKPATH = create_target_path(filepath, "network")
PROJECTPATH = create_target_path(filepath, "lightning-pod")


@hydra.main(config_path=NETWORKPATH, config_name="hydra_config.yaml")
def main(cfg):
    # SET LOGGER
    logs_dir = os.path.join(PROJECTPATH, "logs")
    logger = TensorBoardLogger(logs_dir, name="lightning_logs")
    # SET PROFILER
    profile_dir = os.path.join(logs_dir, "profiler")
    profiler = PyTorchProfiler(dirpath=profile_dir, filename="profiler")
    # SET CHECKPOINT CALLBACK
    chkpt_dir = os.path.join(PROJECTPATH, "models", "checkpoints")
    checkpoint_callback = ModelCheckpoint(dirpath=chkpt_dir, filename="model")
    # SET EARLYSTOPPING CALLBACK
    early_stopping = EarlyStopping(monitor="loss", mode="min")
    # SET CALLBACKS
    callbacks = [checkpoint_callback, early_stopping]
    # SET SEED
    seed_everything(42, workers=True)
    #  GET DATALOADER
    datamodule = LitDataModule()
    #  SET MODEL
    model = LitModel()
    # SET TRAINER
    trainer = Trainer(
        max_epochs=cfg.trainer.max_epochs,
        limit_train_batches=cfg.trainer.limit_train_batches,
        limit_predict_batches=None,
        limit_test_batches=None,
        limit_val_batches=None,
        accelerator=cfg.trainer.accelerator,
        devices=cfg.trainer.devices,
        deterministic=cfg.trainer.deterministic,
        strategy=cfg.trainer.strategy,
        precision=cfg.trainer.precision,
        enable_model_summary=cfg.trainer.enable_model_summary,
        enable_checkpointing=cfg.trainer.enable_checkpointing,
        enable_progress_bar=cfg.trainer.enable_progress_bar,
        logger=logger,
        profiler=profiler,
        callbacks=callbacks,
        plugins=None,
        default_root_dir=None,
        gradient_clip_val=None,
        gradient_clip_algorithm=None,
        num_nodes=1,
        num_processes=None,
        gpus=None,
        auto_select_gpus=False,
        tpu_cores=None,
        ipus=None,
        overfit_batches=0.0,
        track_grad_norm=-1,
        check_val_every_n_epoch=1,
        fast_dev_run=False,
        accumulate_grad_batches=None,
        min_epochs=None,
        max_steps=-1,
        min_steps=None,
        max_time=None,
        val_check_interval=None,
        flush_logs_every_n_steps=None,
        log_every_n_steps=50,
        sync_batchnorm=False,
        weights_save_path=None,
        weights_summary="top",
        num_sanity_val_steps=2,
        resume_from_checkpoint=None,
        benchmark=None,
        reload_dataloaders_every_n_epochs=0,
        auto_lr_find=False,
        replace_sampler_ddp=True,
        detect_anomaly=False,
        auto_scale_batch_size=False,
        amp_backend="negative",
        amp_level=None,
        move_metrics_to_cpu=False,
        multiple_trainloader_mode="max_size_cycle",
    )
    # TRAIN MODEL
    trainer.fit(model=model, datamodule=datamodule)
    # TEST MODEL
    trainer.test(ckpt_path="best", datamodule=datamodule)
    # PERSIST MODEL
    pretrained_dir = os.path.join(PROJECTPATH, "models", "production")
    modelpath = os.path.join(pretrained_dir, "model.onnx")
    input_sample = datamodule.train_data.dataset[0][0]
    model.to_onnx(modelpath, input_sample=input_sample, export_params=True)
    # PREDICT
    predictions = trainer.predict(model, datamodule.val_dataloader())
    # EXPORT PREDICTIONS
    predictions = torch.vstack(predictions)
    predictions = TensorDataset(predictions)
    predictions_dir = os.path.join(PROJECTPATH, "data", "predictions")
    prediction_fname = os.path.join(predictions_dir, "predictions.pt")
    torch.save(predictions, prediction_fname)
    # EXPORT ALL DATA SPLITS FOR REPRODUCIBILITY
    split_dir = os.path.join(PROJECTPATH, "data", "training_split")
    train_split_fname = os.path.join(split_dir, "train.pt")
    test_split_fname = os.path.join(split_dir, "test.pt")
    val_split_fname = os.path.join(split_dir, "val.pt")
    torch.save(datamodule.train_data.dataset, train_split_fname)
    torch.save(datamodule.test_data.dataset, test_split_fname)
    torch.save(datamodule.val_data.dataset, val_split_fname)


if __name__ == "__main__":
    main()
