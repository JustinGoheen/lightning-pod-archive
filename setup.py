from setuptools import setup
from setuptools import find_packages

setup(
    name="lightning-pod",
    version="0.0.1",
    description="A robust PyTorch Lightning research environment",
    url="https://github.com/JustinGoheen/lightning-pod",
    author="Justin Goheen",
    license="MIT",
    install_requires=[
        "pytorch-lightning",
        "lightning-transformers",
        "lightning-grid",
        "lightning-bolts",
        "lightning-flash",
        "torchvision",
        "torchaudio",
        "torchtext",
        "datasets",
        "plotly",
        "matplotlib",
        "sympy",
        "black",
        "mypy",
        "ipywidgets",
        "easy-sphinx @ https://github.com/JustinGoheen/lightning-pod",
    ],
    author_email="",
    packages=find_packages(),
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 3.10",
    ],
)
