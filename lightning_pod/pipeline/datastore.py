import os
import acquisition

if __name__ == "__main__":

    rootpath = os.getcwd()
    datapath = "".join([rootpath, "/", "data", "/", "cache"])
    dataset = acquisition.get_data(return_loader=False)
    storename = dataset.__class__.__name__
    os.system(f"grid datastore create {datapath} --name {storename}")
