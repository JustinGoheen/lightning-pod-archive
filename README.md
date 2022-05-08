# Lightning Pod
---

<div align="center">

A template environment and system architecture for [PyTorch Lightning](https://www.pytorchlightning.ai/) and [Grid.ai](https://www.grid.ai/) in [Gitpod](https://www.gitpod.io/).

![](https://img.shields.io/badge/PyTorch_Lightning-Code-informational?style=flat&logo=pytorchlightning&logoColor=white&color=2bbc8a)
![](https://img.shields.io/badge/Grid.ai-Compute-informational?style=flat&logo=grid.ai&logoColor=white&color=2bbc8a)
![](https://img.shields.io/badge/Gitpod-DevEnv-informational?style=flat&logo=gitpod&logoColor=white&color=2bbc8a)

[![codecov](https://codecov.io/gh/JustinGoheen/lightning-pod/branch/main/graph/badge.svg)](https://codecov.io/gh/JustinGoheen/lightning-pod)
![CircleCI](https://circleci.com/gh/JustinGoheen/lightning-pod.svg?style=shield)

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/JustinGoheen/lightning-pod)

</div>

---

## Overview

Gitpod is to be used (if needed) during the initial development phases, and Grid [Sessions](https://docs.grid.ai/features/sessions) should be used to test on the desired machine type once the LightningModule and Trainer are functioning as intended in Gitpod or locally. Once a model is out of development and is ready to be trained, a Grid [Run](https://docs.grid.ai/features/runs/README) should be used to train the model.

Refer to the [wiki](https://github.com/JustinGoheen/lightning-pod/wiki) for additional information and guides.