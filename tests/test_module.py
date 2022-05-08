from lightning_pod.network.module import LitModel, Encoder, Decoder


def test_module_not_abstract():
    """
    example: https://github.com/PyTorchLightning/pytorch-lightning/blob/15fa5389387b3a220bc044dd30eb0be1e8f64944/tests/core/test_lightning_module.py#L29
    """
    _ = LitModel()


def test_encoder_not_abstract():
    _ = Encoder()


def test_decoder_not_abstract():
    _ = Decoder()
