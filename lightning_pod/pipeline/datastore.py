import os
from pathlib import Path
from lightning_pod.pipeline.datamodule import LitDataModule


if __name__ == "__main__":

    network_path = Path(__file__).parent
    project_path = network_path.parents[1]
    data_path = os.path.join(project_path, "data", "cache")
    datamodule = LitDataModule()
    dataset = datamodule.dataset
    storename = dataset.__name__
    os.system(f"grid datastore create {data_path} --name {storename}")
