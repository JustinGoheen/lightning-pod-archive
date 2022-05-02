import os
from lightning_pod.pipeline.acquisition import get_data

if __name__ == "__main__":

    rootpath = os.getcwd()
    datapath = "".join([rootpath, "/", "data", "/", "cache"])
    dataset = get_data(return_loader=False)
    storename = dataset.__class__.__name__
    os.system(f"grid datastore create {datapath} --name {storename}")
