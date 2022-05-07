# lightning-pod
[![](https://img.shields.io/badge/PyTorch_Lightning-Code-informational?style=flat&logo=pytorchlightning&logoColor=white&color=2bbc8a)](#)
[![](https://img.shields.io/badge/Grid.ai-Compute-informational?style=flat&logo=grid.ai&logoColor=white&color=2bbc8a)](#)
[![](https://img.shields.io/badge/Gitpod-DevEnv-informational?style=flat&logo=gitpod&logoColor=white&color=2bbc8a)](#)


A template environment and system architecture for [PyTorch Lightning](https://www.pytorchlightning.ai/) and [Grid.ai](https://www.grid.ai/) in [Gitpod](https://www.gitpod.io/).

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/JustinGoheen/lightning-pod)

Please note that Gitpod is to be used (if needed) during the initial development phases, and Grid [Sessions](https://docs.grid.ai/features/sessions) should be used to test on the desired machine type once the LightningModule and Trainer are functioning as intended on a [fast_dev_run](https://pytorch-lightning.readthedocs.io/en/stable/common/trainer.html#fast-dev-run) in Gitpod or locally. Once a model is out of development and is ready to be trained, a Grid [Run](https://docs.grid.ai/features/runs/README) should be used to train the model.

Refer to the [wiki](https://github.com/JustinGoheen/lightning-pod/wiki) for additional guides.

## The basics

This template can aid in creating reproducible projects that share a common architecture, increasing the readility of codebases and inspection of training logs adhering to the template.

The intent is that you fork this template, and set it as a [template](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-template-repository) repo in GitHub. Setting this repo as a template will allow you to [create a new repo from the template](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template) in GitHub's web interface or CLI. Using the recommended method will also allow you to keep the fork up to date by using [fetch-upstream](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/syncing-a-fork).

Alternatively, one can clone the fork and reset the git history with:

```sh
git clone https://github.com/{{ YOUR_USER_NAME }}/lightning-pod.git --branch main
cd {{ path_to_clone }}
rm -rf .git
git init
```

Once the new git repo is intialized, it can be published to upstream using the desired method.

### Core files

The two most important files are [lightning_pod.network.model](https://github.com/JustinGoheen/lightning-pod/blob/main/lightning_pod/network/model.py) and [lightning_pod.network.trainer](https://github.com/JustinGoheen/lightning-pod/blob/main/lightning_pod/network/trainer.py). `model.py` contains the PyTorch Lightning [LightningModule](https://pytorch-lightning.readthedocs.io/en/stable/common/lightning_module.html) and inner layer torch.nn Modules, and `trainer.py` contains the PyTorch Lightning [Trainer](https://pytorch-lightning.readthedocs.io/en/stable/common/trainer.html). A LightningModule is effectively _the algorithm_ and a Trainer is the training recipe i.e. it is the component used to tell the LightningModule how to train and which plugins and callbacks the system should incorporate.

## The environment

Aside from PyTorch Lightning ecosystem libraries, the template environment provides access to additional tools that enable quality research projects.

### Data
Researchers in need of datasets can leverage the inclusion of torchvision, torchtext, torchaudio, and lighting-bolts to access datasets for projects.

### Add-ons
The template environment includes tools to visualize data transformations with plotly or matplotlib; it includes SymPy to help create LaTeX notation images and code snippets.

> template files will be added to enable source code documentation using sphinx and autodoc for material-for-mkdocs

### Code coverage and security
This template uses [deepsource](https://deepsource.io/) (account required) for coverage and GitHub's [CodeQL](https://github.com/github/codeql-action) for security.

### Installs

> `requirements.txt` has been organized according to purpose so that users can delete unneccesary dependencies prior to installing locally or running in Gitpod

Installing pytorch-lightning also installs: 

- [PyTorch](https://pytorch.org/docs/stable/index.html)
- [torchmetrics](https://torchmetrics.readthedocs.io/en/stable/)
- [NumPy](https://numpy.org/)
- [TensorBoard](https://www.tensorflow.org/tensorboard)

In addition to PyTorch Lightning, requirements.txt will also install: 
- [lightning-grid](https://www.grid.ai/)
- [lightning-transformers](https://lightning-transformers.readthedocs.io/en/latest/)
- [lightning-bolts](https://lightning-bolts.readthedocs.io/en/stable/)
- [lightning-flash](https://lightning-flash.readthedocs.io/en/stable/)
- [torchvision](https://pytorch.org/vision/stable/index.html)
- [torchaudio](https://pytorch.org/audio/stable/index.html)
- [torchtext](https://pytorch.org/text/stable/index.html)
- [SymPy](https://www.sympy.org/en/index.html) (symbolic mathematics)
- [Plotly](https://plotly.com/python/) (data visualization)
- [Black](https://black.readthedocs.io/en/stable/) (formatting)
- [MyPy](https://github.com/python/mypy/tree/38f1e30e8137ccc1aad6a4f113eb4360c6206539) (static type checker)
- [flake8](https://flake8.pycqa.org/en/latest/#) (linting)
- [coverage](https://coverage.readthedocs.io/en/6.3.2/) (measuring code coverage)
- [PyTest](pytest) (testing utility)


### M1 powered Macs

Individuals using conda and miniforge on M1 powered macs can replicate the environment locally with:

```sh
cd {{ path_to_clone }}
conda env create --file environment.yml
```

Using the above will create a new conda env titled `lightning-pod`.

## Using the built-in example

> running the following example will download the MNIST dataset to `data/cache/MNIST` in the cloned directory and will run a trainer with fast_dev_run

Once the repo has been cloned, open the project in your editor of choice and install an editable version of lightning-pod with

```sh
pip install -e .
```

and then run 

```sh
{{ activate the venv or conda env }}
python lightning_pod/network/trainer.py 
```

the intended results are shown below

![](https://github.com/JustinGoheen/lightning-pod/blob/main/docs/imgs/example_run.png)


## VS Code PyTorch Profiler and TensorBoard

VS Code users can learn more about PyTorch integrations on the [official](https://code.visualstudio.com/docs/datascience/pytorch-support) VS Code site.

> Grid.ai supports TensorBoard in the [Runs](https://docs.grid.ai/features/runs/Analyzing%20Runs/metric-charts#tensorboard) web interface.

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
