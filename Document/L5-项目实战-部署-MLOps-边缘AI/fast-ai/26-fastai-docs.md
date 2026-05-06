[ fastai ](./index.html)

  * [ __ ](https://github.com/fastai/fastai)

[ __ ]( "Toggle reader mode")

__

  1. [Welcome to fastai](./index.html)

  * [ Welcome to fastai](./index.html)

  * [ Quick start](./quick_start.html)

  * Tutorials __

    * [ Tutorials](./tutorial.html)

    * Beginner __

      * [ Computer vision intro](./tutorial.vision.html)

      * [ Text transfer learning](./tutorial.text.html)

      * [ Tabular training](./tutorial.tabular.html)

      * [ Collaborative filtering tutorial](./tutorial.collab.html)

    * Intermediate __

      * [ Data block tutorial](./tutorial.datablock.html)

      * [ Training Imagenette](./tutorial.imagenette.html)

      * [ Mid-tier data API - Pets](./tutorial.pets.html)

      * [ Chest X-ray model](./tutorial.medical_imaging.html)

      * [ Transformers](./tutorial.transformers.html)

      * [ Wikitext data tutorial](./tutorial.wikitext.html)

      * [ Notebook distributed training](./tutorial.distributed.html)

    * Advanced __

      * [ Custom transforms](./tutorial.albumentations.html)

      * [ Custom new task - siamese](./tutorial.siamese.html)

      * [ Image sequences](./tutorial.image_sequence.html)

    * Migrating from Other Libs __

      * [ Pure PyTorch to fastai](./examples/migrating_pytorch.html)

      * [ Pytorch to fastai details](./examples/migrating_pytorch_verbose.html)

      * [ Ignite with fastai](./examples/migrating_ignite.html)

      * [ Lightning with fastai](./examples/migrating_lightning.html)

      * [ Catalyst with fastai](./examples/migrating_catalyst.html)

  * Training __

    * [ Learner, Metrics, Callbacks](./learner.html)

    * [ Optimizers](./optimizer.html)

    * [ Metrics](./metrics.html)

    * [ Interpretation of Predictions](./interpret.html)

    * [ Distributed training](./distributed.html)

    * [ Mixed precision training](./callback.fp16.html)

    * [ Channels Last training](./callback.channelslast.html)

    * Callbacks __

      * [ Callbacks](./callback.core.html)

      * [ Model hooks](./callback.hook.html)

      * [ Progress and logging](./callback.progress.html)

      * [ Hyperparam schedule](./callback.schedule.html)

      * [ Data Callbacks](./callback.data.html)

      * [ MixUp and Friends](./callback.mixup.html)

      * [ Predictions callbacks](./callback.preds.html)

      * [ Callback for RNN training](./callback.rnn.html)

      * [ Tracking callbacks](./callback.tracker.html)

      * [ Training callbacks](./callback.training.html)

  * Data __

    * [ Data block](./data.block.html)

    * [ Data core](./data.core.html)

    * [ DataLoaders](./data.load.html)

    * [ External data](./data.external.html)

    * [ Data transformations](./data.transforms.html)

  * Core __

    * [ Torch Core](./torch_core.html)

    * [ Layers](./layers.html)

    * [ Loss Functions](./losses.html)

  * Vision __

    * [ Core vision](./vision.core.html)

    * [ Vision data](./vision.data.html)

    * [ Vision augmentation](./vision.augment.html)

    * [ Vision learner](./vision.learner.html)

    * Models __

      * [ XResnet](./vision.models.xresnet.html)

      * [ Dynamic UNet](./vision.models.unet.html)

    * [ GAN](./vision.gan.html)

    * [ Vision utils](./vision.utils.html)

    * [ Vision widgets](./vision.widgets.html)

  * Text __

    * [ Text core](./text.core.html)

    * [ Text data](./text.data.html)

    * [ Text learner](./text.learner.html)

    * Models __

      * [ Core text modules](./text.models.core.html)

      * [ AWD-LSTM](./text.models.awdlstm.html)

  * Tabular __

    * [ Tabular core](./tabular.core.html)

    * [ Tabular data](./tabular.data.html)

    * [ Tabular learner](./tabular.learner.html)

    * [ Tabular model](./tabular.model.html)

    * [ Collaborative filtering](./collab.html)

  * Medical __

    * [ Medical Imaging](./medical.imaging.html)

    * [ Medical Text](./medical.text.html)

  * Integrations __

    * [ Wandb](./callback.wandb.html)

    * [ Captum](./callback.captum.html)

    * [ Comet.ml](./callback.comet.html)

    * [ Tensorboard](./callback.tensorboard.html)

    * [ Hugging Face Hub](./huggingface.html)

  * fastai Development __

    * [ Pull requests made easy](./dev-setup.html)

    * [ git Notes](./dev/git.html)

    * [ fastai Abbreviation Guide](./dev/abbr.html)

    * [ fastai coding style](./dev/style.html)

    * [ Working with GPU](./dev/gpu.html)

    * [ Notes For Developers](./dev/develop.html)

## On this page

  * Installing
  * Learning fastai
  * About fastai
  * Migrating from other libraries
  * Windows Support
  * Tests
  * Contributing
  * Docker Containers

  * [__Report an issue](https://github.com/fastai/fastai/issues/new)

## Other Formats

  * [ __CommonMark](index.html.md)

# Welcome to fastai

fastai simplifies training fast and accurate neural nets using modern best practices 

[](https://github.com/fastai/fastai/actions/workflows/main.yml) [](https://pypi.org/project/fastai/#description) [](https://anaconda.org/fastai/fastai)

## Installing

You can use fastai without any installation by using [Google Colab](https://colab.research.google.com/). In fact, every page of this documentation is also available as an interactive notebook - click “Open in colab” at the top of any page to open it (be sure to change the Colab runtime to “GPU” to have it run fast!) See the fast.ai documentation on [Using Colab](https://course19.fast.ai/start_colab.html) for more information.

You can install fastai on your own machines with: `pip install fastai`.

To ensure that you have the best available version of PyTorch on your machine, recommend [installing](https://pytorch.org/get-started/locally/) that first.

If you plan to develop fastai yourself, or want to be on the cutting edge, you can use an editable install (if you do this, you should also use an editable install of [fastcore](https://github.com/fastai/fastcore) to go with it.) First install PyTorch, and then:
    
    
    git clone https://github.com/fastai/fastai
    pip install -e "fastai[dev]"

## Learning fastai

The best way to get started with fastai (and deep learning) is to read [the book](https://www.amazon.com/Deep-Learning-Coders-fastai-PyTorch/dp/1492045527), and complete [the free course](https://course.fast.ai).

To see what’s possible with fastai, take a look at the [Quick Start](https://docs.fast.ai/quick_start.html), which shows how to use around 5 lines of code to build an image classifier, an image segmentation model, a text sentiment model, a recommendation system, and a tabular model. For each of the applications, the code is much the same.

Read through the [Tutorials](https://docs.fast.ai/tutorial.html) to learn how to train your own models on your own datasets. Use the navigation sidebar to look through the fastai documentation. Every class, function, and method is documented here.

To learn about the design and motivation of the library, read the [peer reviewed paper](https://www.mdpi.com/2078-2489/11/2/108/htm).

## About fastai

fastai is a deep learning library which provides practitioners with high-level components that can quickly and easily provide state-of-the-art results in standard deep learning domains, and provides researchers with low-level components that can be mixed and matched to build new approaches. It aims to do both things without substantial compromises in ease of use, flexibility, or performance. This is possible thanks to a carefully layered architecture, which expresses common underlying patterns of many deep learning and data processing techniques in terms of decoupled abstractions. These abstractions can be expressed concisely and clearly by leveraging the dynamism of the underlying Python language and the flexibility of the PyTorch library. fastai includes:

  * A new type dispatch system for Python along with a semantic type hierarchy for tensors
  * A GPU-optimized computer vision library which can be extended in pure Python
  * An optimizer which refactors out the common functionality of modern optimizers into two basic pieces, allowing optimization algorithms to be implemented in 4–5 lines of code
  * A novel 2-way callback system that can access any part of the data, model, or optimizer and change it at any point during training
  * A new data block API
  * And much more…

fastai is organized around two main design goals: to be approachable and rapidly productive, while also being deeply hackable and configurable. It is built on top of a hierarchy of lower-level APIs which provide composable building blocks. This way, a user wanting to rewrite part of the high-level API or add particular behavior to suit their needs does not have to learn how to use the lowest level.

## Migrating from other libraries

It’s very easy to migrate from plain PyTorch, Ignite, or any other PyTorch-based library, or even to use fastai in conjunction with other libraries. Generally, you’ll be able to use all your existing data processing code, but will be able to reduce the amount of code you require for training, and more easily take advantage of modern best practices. Here are migration guides from some popular libraries to help you on your way:

  * [Plain PyTorch](https://docs.fast.ai/examples/migrating_pytorch.html)
  * [Ignite](https://docs.fast.ai/examples/migrating_ignite.html)
  * [Lightning](https://docs.fast.ai/examples/migrating_lightning.html)
  * [Catalyst](https://docs.fast.ai/examples/migrating_catalyst.html)

## Windows Support

Due to python multiprocessing issues on Jupyter and Windows, `num_workers` of `Dataloader` is reset to 0 automatically to avoid Jupyter hanging. This makes tasks such as computer vision in Jupyter on Windows many times slower than on Linux. This limitation doesn’t exist if you use fastai from a script.

See [this example](https://github.com/fastai/fastai/blob/master/nbs/examples/dataloader_spawn.py) to fully leverage the fastai API on Windows.

We recommend using Windows Subsystem for Linux (WSL) instead – if you do that, you can use the regular Linux installation approach, and you won’t have any issues with `num_workers`.

## Tests

To run the tests in parallel, launch:

`nbdev_test`

For all the tests to pass, you’ll need to install the dependencies specified as part of dev_requirements in settings.ini

`pip install -e .[dev]`

Tests are written using `nbdev`, for example see the documentation for `test_eq`.

## Contributing

After you clone this repository, make sure you have run `nbdev_install_hooks` in your terminal. This install Jupyter and git hooks to automatically clean, trust, and fix merge conflicts in notebooks.

After making changes in the repo, you should run `nbdev_prepare` and make additional and necessary changes in order to pass all the tests.

## Docker Containers

For those interested in official docker containers for this project, they can be found [here](https://github.com/fastai/docker-containers#fastai).

  * [__Report an issue](https://github.com/fastai/fastai/issues/new)
