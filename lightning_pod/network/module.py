"""
This example expands on basic exaples provided in PL docs. A key difference being that forward() is 
implemented in the LightningModule in order to enable persisting the model with ONNX or torchscript.
If forward() is not implemented, PyTorch will raise an NotImplementedError and the model will not be
saved.
"""

import pytorch_lightning as pl
import torch.nn.functional as F
from torch import nn, optim


class Encoder(nn.Module):
    """an encoder layer

    Args:
        None: no arguments are required at initialization.

    Returns:
        an encoded image.
    """

    def __init__(self):
        super().__init__()
        self.l1 = nn.Sequential(
            nn.Linear(
                in_features=28 * 28,
                out_features=64,
                bias=True,  # default
            ),
            nn.ReLU(
                inplace=False,  # default
            ),
            nn.Linear(
                in_features=64,
                out_features=3,
                bias=True,  # default
            ),
        )

    def forward(self, x):
        return self.l1(x)


class Decoder(nn.Module):
    """a decoder layer

    Args:
        None: no arguments are required at initialization.

    Returns:
        a decoded image.
    """

    def __init__(self):
        super().__init__()
        self.l1 = nn.Sequential(
            nn.Linear(
                in_features=3,
                out_features=64,
                bias=True,  # default
            ),
            nn.ReLU(
                inplace=False,  # default
            ),
            nn.Linear(
                in_features=64,
                out_features=28 * 28,
                bias=True,  # default
            ),
        )

    def forward(self, x):
        return self.l1(x)


class LitModel(pl.LightningModule):
    """a custom PyTorch Lightning Module

    Args:
        encoder (nn.Module): an encoder layer.
        decoder (nn.Module): a decoder layer.

    Returns:
        a LightningModule fit to the training dataset.
    """

    def __init__(self):
        super().__init__()
        self.encoder = Encoder()
        self.decoder = Decoder()

    def forward(self, x):
        x = x.view(x.size(0), -1)
        z = self.encoder(x)
        output = self.decoder(z)
        return output

    def training_step(self, batch, batch_idx):
        # training_step defines the train loop.
        x, y = batch
        x = x.view(x.size(0), -1)
        z = self.encoder(x)
        x_hat = self.decoder(z)
        loss = F.mse_loss(x_hat, x)
        self.log("loss", loss)
        return loss

    def configure_optimizers(self):
        optimizer = optim.Adam(self.parameters(), lr=1e-3)
        return optimizer
