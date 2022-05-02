# lightning-pod
[![](https://img.shields.io/badge/PyTorch_Lightning-Code-informational?style=flat&logo=pytorchlightning&logoColor=white&color=2bbc8a)](#)
[![](https://img.shields.io/badge/Grid.ai-Compute-informational?style=flat&logo=grid.ai&logoColor=white&color=2bbc8a)](#)
[![](https://img.shields.io/badge/Gitpod-DevEnv-informational?style=flat&logo=gitpod&logoColor=white&color=2bbc8a)](#)


A template repo for [PyTorch Lightning](https://www.pytorchlightning.ai/) in [Gitpod](https://www.gitpod.io/).

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/JustinGoheen/lightning-pod)

<!-- Refer to the [wiki](https://github.com/JustinGoheen/lightning-pod/wiki) for additional guides. -->

## The basics

This template can aid in creating and sharing reproducible projects structured according to potential best practices for researchers.

The intent is that you clone the repo each time you need to begin a fresh project. The repo can be cloned from within [VS Code](https://code.visualstudio.com/docs/editor/github#_cloning-a-repository), [PyCharm](https://www.jetbrains.com/help/pycharm/manage-projects-hosted-on-github.html#clone-from-GitHub), [GitKraken](https://www.gitkraken.com/learn/git/git-clone), or in terminal with:

```sh
git clone https://github.com/JustinGoheen/lightning-pod.git --depth 1 --branch main --single-branch
```

Please star this repo if you use it.

## The environment

Installing pytorch-lightning also installs: 

- [PyTorch](https://pytorch.org/docs/stable/index.html)
- [torchmetrics](https://torchmetrics.readthedocs.io/en/stable/)
- [NumPy](https://numpy.org/)
- [TensorBoard](https://www.tensorflow.org/tensorboard)

In addition to PyTorch Lightning, requirements.txt will also install: 
- [Grid.ai](https://www.grid.ai/)
- [lightning-transformers](https://lightning-transformers.readthedocs.io/en/latest/)
- [torchvision](https://pytorch.org/vision/stable/index.html)
- [torchaudio](https://pytorch.org/audio/stable/index.html)
- [torchtext](https://pytorch.org/text/stable/index.html)
- [datasets](https://huggingface.co/docs/datasets/index), curated datasets by Hugging Face
- [SymPy](https://www.sympy.org/en/index.html) (symbolic mathematics)
- [Plotly](https://plotly.com/python/) (data visualization)
- [Black](https://black.readthedocs.io/en/stable/) (formatting)
- [MyPy](https://github.com/python/mypy/tree/38f1e30e8137ccc1aad6a4f113eb4360c6206539) (static type checker)
- [pre-commit](https://pre-commit.com/) (code review)
- [PyTest](pytest) (testing utility)
- [easy-sphinx](https://github.com/JustinGoheenOrg/easy-sphinx) (Sphinx-autodoc + [material for mkdocs](https://squidfunk.github.io/mkdocs-material/))

Security minded engineers can opt for [deepsource](https://deepsource.io/), [pyre/pysa](https://pyre-check.org/), or [Bandit](https://github.com/PyCQA/bandit). This template uses deepsource (account required) and GitHub's [CodeQL](https://github.com/github/codeql-action).

> remove the `.deepsource.toml` file if using pyre/pysa or bandit

### M1 powered Macs

Individuals using conda and miniforge on M1 powered macs can replicate the environment locally with:

```sh
cd {{ path_to_clone }}
conda env create --file environment.yml
```

Using the above will create a new conda env titled `lightning-base`.

## Using the built-in example

> running the following example will download the MNIST dataset to `data/cache/MNIST` in the cloned directory and will run a trainer with fast_dev_run

Once the repo has been cloned, open the project in your editor of choice and install an editable version of the package with

```sh
pip install -e .
```

and then run 

```sh
python lightning_pod/network/trainer.py 
```

the results are shown below

![](https://github.com/JustinGoheen/lightning-pod/blob/main/docs/imgs/example_run.png)

## Suggested use

This template is mostly for distributed teams who can benefit from a tool like Gitpod. Individuals who wish to share open source work can use this template as a guideline for creating reproducible projects. Use of Gitpod is not required for individuals who do not fit into one of those two categories; these individuals can still benefit from forking the repo as a template and simply removing the `.gitpod.yml` file from the project directory. 

> It is not recommended to start a Grid Session from within a Gitpod Workspace; doing so may accrue compute hours in both platforms.

The best practice would be to: develop in Gitpod using a development-sized (toy) dataset (i.e. [fast_dev_run](https://pytorch-lightning.readthedocs.io/en/stable/common/debugging.html#quick-unit-testing) in PyTorch Lightning) and then start the Grid Session locally from your machine (i.e. all updates have been pushed to GitHub and the Gitpod Workspace has been shutdown).

Once the full project requirements have been determined, it is best to replace the current requirements.txt with

```sh
pip freeze > requirements.txt
```

## TensorBoard

VS Code users can learn more about PyTorch development and TensorBoard on the [official](https://code.visualstudio.com/docs/datascience/pytorch-support) VS Code site.

Grid.ai support TensorBoard in the [Runs](https://docs.grid.ai/features/runs/Analyzing%20Runs/metric-charts#tensorboard) web interface.

## Learning PyTorch Lightning

Rather than diving into PyTorch Lightning by building a model, it is suggested to watch the following 4 videos by the PyTorch Lightning team; these videos help to familiarize users with the codebase:

1. [Lightning Code Base Hardcore Deep Dive](https://youtu.be/aEeh9ucKUkU)
2. [Deep Dive into a Single Example Code Flow](https://youtu.be/NEpRYqdsm54)
3. [Part 3 Lightning Codebase Deep Dive](https://youtu.be/x4d4RDNJaZk)
4. [Fault Tolerance](https://youtu.be/aUtn7H1jYl4)

After watching the videos, one can use the official [guides](https://pytorch-lightning.readthedocs.io/en/latest/expertise_levels.html) to level up their skills.

## Why PyTorch Lightning

PyTorch Lightning is an easy to use, cloud-training ready framework equipped with robust utilities that allows researchers to focus on research, and not engineering.

Instructors will benefit from using PyTorch Lightning in courses because it enables students to focus on the conceptual purpose of algorithms as opposed to facing teaching and learning barriers associated with from-scratch utilities code. 

PyTorch Lightning is well [documented](https://pytorch-lightning.readthedocs.io/en/latest/), and comes packed with basic, intermediate, advanced, and expert [guides](https://pytorch-lightning.readthedocs.io/en/latest/expertise_levels.html) and [examples](https://pytorch-lightning.readthedocs.io/en/latest/notebooks/course_UvA-DL/01-introduction-to-pytorch.html).

PyTorch Lightning has a large community of users who are active in [Slack](https://join.slack.com/t/pytorch-lightning/shared_invite/zt-12iz3cds1-uyyyBYJLiaL2bqVmMN7n~A) and GitHub [Discussions](https://github.com/PyTorchLightning/pytorch-lightning/discussions).

PyTorch Lightning models are ready for distributed training with [Grid.ai](https://www.grid.ai/). Scaling training environments can be as easy as logging into Grid's web interface, connecting a GitHub repo, selecting a machine type [CPU, GPU, TPU, IPU, HPU] from a cost-transparent list, and connecting to a [datastore](https://docs.grid.ai/features/datastores).
