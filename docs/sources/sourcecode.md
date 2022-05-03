### Encoder


```python
lightning_pod.network.model.Encoder()
```


an encoder layer

__Arguments__

- __None__: no arguments are required at initialization.

__Returns__

an encoded rank 2 Tensor.


----

### Decoder


```python
lightning_pod.network.model.Decoder()
```


a decoder layer

__Arguments__

- __None__: no arguments are required at initialization.

__Returns__

a decoded rank 2 Tensor.


----

### LitModel


```python
lightning_pod.network.model.LitModel(encoder, decoder)
```


a custom PyTorch Lightning Module

__Arguments__

- __encoder__: an encoder layer.
- __decoder__: a decoder layer.

__Returns__

a LightningModule fit to the training dataset.


----

