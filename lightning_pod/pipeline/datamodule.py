from audioop import tostereo
import os
from pytorch_lightning import LightningDataModule
from torch.utils.data import Dataset, DataLoader, random_split
from torchvision.datasets import MNIST
from torchvision import transforms


class LitDataModule(LightningDataModule):
    def __init__(
        self,
        dataset: Dataset = MNIST,
        data_dir: str = "data/cache",
        return_loader: bool = True,
        split: bool = True,
        train_size: float = 0.8,
        num_workers: int = 0,
        transforms=transforms.ToTensor(),
    ):
        super().__init__()
        self.data_dir = data_dir
        self.dataset = dataset
        self.split = split
        self.train_size = train_size
        self.num_workers = num_workers
        self.transforms = transforms

    def prepare_data(self):
        self._check_datadir_exists()
        self._check_for_existing_data()

    def setup(self, stage=None):
        if stage == "fit" or stage is None:
            full_dataset = self.dataset(
                self.data_dir, train=True, transform=self.transforms
            )
            train_size = int(len(full_dataset) * self.train_size)
            test_size = len(full_dataset) - train_size
            self.train_data, self.val_data = random_split(
                full_dataset, lengths=[train_size, test_size]
            )
        if stage == "test" or stage is None:
            self.test_data = self.dataset(
                self.data_dir, train=False, transform=self.transforms
            )

    # def teardown(self):
    #     pass

    def train_dataloader(self):
        return DataLoader(self.train_data, num_workers=self.num_workers)

    def test_dataloader(self):
        return DataLoader(self.test_data, num_workers=self.num_workers)

    def val_dataloader(self):
        return DataLoader(self.val_data, num_workers=self.num_workers)

    def _check_datadir_exists(self):
        if not os.path.isdir(self.data_dir):
            os.mkdir(self.data_dir)

    def _download_dataset(self):
        # train, val
        self.dataset(
            self.data_dir, train=True, download=True, transform=self.transforms
        )
        # test
        self.dataset(
            self.data_dir, train=False, download=True, transform=self.transforms
        )

    def _fetch_dataset(self):
        self.dataset = self.dataset(
            self.data_dir, download=False, transform=self.transforms
        )

    def _check_for_existing_data(self):
        if not os.listdir(self.data_dir):
            self._download_dataset()
