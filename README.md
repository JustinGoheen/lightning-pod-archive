# lightning-pod
[![](https://img.shields.io/badge/PyTorch_Lightning-Code-informational?style=flat&logo=pytorchlightning&logoColor=white&color=2bbc8a)](#)
[![](https://img.shields.io/badge/Grid.ai-Compute-informational?style=flat&logo=grid.ai&logoColor=white&color=2bbc8a)](#)
[![](https://img.shields.io/badge/Gitpod-DevEnv-informational?style=flat&logo=gitpod&logoColor=white&color=2bbc8a)](#)


A template repo for [PyTorch Lightning](https://www.pytorchlightning.ai/) in [Gitpod](https://www.gitpod.io/).

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/JustinGoheen/lightning-pod)

## The basics

This template can aid in creating and sharing reproducible projects structured according to potential best practices for researchers.

The intent is that you fork the repo, keep your fork up to date with [fetch upstream](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/syncing-a-fork), and clone the repo each time you need to begin a fresh project. The repo can be cloned from within [VS Code](https://code.visualstudio.com/docs/editor/github#_cloning-a-repository), [PyCharm](https://www.jetbrains.com/help/pycharm/manage-projects-hosted-on-github.html#clone-from-GitHub), [GitKraken](https://www.gitkraken.com/learn/git/git-clone), or in terminal with:

```sh
git clone https://github.com/JustinGoheen/lightning-pod.git --depth 1 --branch main --single-branch
```

## The environment

Installing pytorch-lightning also installs: 

- [PyTorch](https://pytorch.org/docs/stable/index.html)
- [torchmetrics](https://torchmetrics.readthedocs.io/en/stable/)
- [NumPy](https://numpy.org/)
- [TensorBoard](https://www.tensorflow.org/tensorboard)

In addition to PyTorch Lightning, requirements.txt will also install: 
- [lightning-transformers](https://lightning-transformers.readthedocs.io/en/latest/)
- [Grid.ai](https://www.grid.ai/)
- Hugging Face's [datasets](https://huggingface.co/docs/datasets/index)
- [SymPy](https://www.sympy.org/en/index.html) (symbolic mathematics)
- [Plotly](https://plotly.com/python/) (data visualization)
- [Black](https://black.readthedocs.io/en/stable/) (formatting)
- [MyPy](https://github.com/python/mypy/tree/38f1e30e8137ccc1aad6a4f113eb4360c6206539) (static type checker)
- [easy-sphinx](https://github.com/JustinGoheenOrg/easy-sphinx) (Sphinx-autodoc + [material for mkdocs](https://squidfunk.github.io/mkdocs-material/))

Security minded engineers can opt for [deepsource](https://deepsource.io/), [pyre/pysa](https://pyre-check.org/), or [Bandit](https://github.com/PyCQA/bandit). This template uses deepsource (account required).

> remove the `.deepsource.toml` file if using pyre/pysa or bandit

The Gitpod config file installs the Jupyter extension for individuals who also prefer notebook environments.

## Suggested use

This template is mostly for distributed teams who can benefit from a tool like Gitpod. Individuals who wish to share open source work can use this template as a guideline for creating reproducible projects. Use of Gitpod is not required for individuals who do not fit into one of those two categories; these individuals will still benefit from forking the repo as a template and simply removing the `.gitpod.yml` file from the project directory. 

> It is not recommended to start a Grid Session from within a Gitpod Workspace; doing so may accrue compute hours in both platforms.

The best practice would be to: develop in Gitpod using a development-sized (toy) dataset (i.e. fast_dev_run in PyTorch Lightning) and then start the Grid Session locally from your machine (i.e. all updates have been pushed to GitHub and the Gitpod Workspace has been shutdown).

Once the full project requirements have been determined, it is best to replace the current requirements.txt with

```sh
pip freeze > requirements.txt
```

## TensorBoard

VS Code users can learn more about PyTorch development and TensorBoard on the [official](https://code.visualstudio.com/docs/datascience/pytorch-support) VS Code site.

Grid.ai support TensorBoard in the [Runs](https://docs.grid.ai/features/runs/Analyzing%20Runs/metric-charts#tensorboard) web interface.

## Why PyTorch Lightning

PyTorch Lightning is an easy to use, cloud-training ready framework equipped with robust utilities that allows researchers to focus on research, and not engineering.

Instructors will benefit from using PyTorch Lightning in courses because it enables students to focus on the conceptual purpose of algorithms as opposed to facing teaching and learning barriers associated with from-scratch utilities code. 

PyTorch Lightning is well [documented](https://pytorch-lightning.readthedocs.io/en/latest/), and comes packed with basic, intermediate, advanced, and expert [guides](https://pytorch-lightning.readthedocs.io/en/latest/levels/core_skills.html) and [examples](https://pytorch-lightning.readthedocs.io/en/latest/notebooks/course_UvA-DL/01-introduction-to-pytorch.html).

PyTorch Lightning has a large user community of helpful users who are active in [Slack](https://join.slack.com/t/pytorch-lightning/shared_invite/zt-12iz3cds1-uyyyBYJLiaL2bqVmMN7n~A) and GitHub [Discussions](https://github.com/PyTorchLightning/pytorch-lightning/discussions).

PyTorch Lightning models are ready for distributed training with [Grid.ai](https://www.grid.ai/). Scaling to multi-GPU or TPU training environments can be as easy as logging into Grid's web interface, connecting a GitHub repo, selecting a machine type [CPU, GPU, TPU] from a cost-transparent list, and connecting to a [datastore](https://docs.grid.ai/features/datastores).
