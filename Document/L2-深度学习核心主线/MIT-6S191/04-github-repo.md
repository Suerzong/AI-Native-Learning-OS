[Skip to content](#start-of-content)

You signed in with another tab or window. [Reload]() to refresh your session. You signed out in another tab or window. [Reload]() to refresh your session. You switched accounts on another tab or window. [Reload]() to refresh your session. Dismiss alert

{{ message }}

[ MITDeepLearning ](/MITDeepLearning) / **[introtodeeplearning](/MITDeepLearning/introtodeeplearning) ** Public

  * [ Notifications ](/login?return_to=%2FMITDeepLearning%2Fintrotodeeplearning) You must be signed in to change notification settings
  * [ Fork 4.5k ](/login?return_to=%2FMITDeepLearning%2Fintrotodeeplearning)
  * [ Star  8.6k ](/login?return_to=%2FMITDeepLearning%2Fintrotodeeplearning)

[](/MITDeepLearning/introtodeeplearning)

master

[Branches](/MITDeepLearning/introtodeeplearning/branches)[Tags](/MITDeepLearning/introtodeeplearning/tags)

[](/MITDeepLearning/introtodeeplearning/branches)[](/MITDeepLearning/introtodeeplearning/tags)

Go to file

Code

Open more actions menu

## Folders and files

Name| Name| Last commit message| Last commit date
---|---|---|---

## Latest commit

## History

[736 Commits](/MITDeepLearning/introtodeeplearning/commits/master/)[](/MITDeepLearning/introtodeeplearning/commits/master/)736 Commits
[assets](/MITDeepLearning/introtodeeplearning/tree/master/assets "assets")| [assets](/MITDeepLearning/introtodeeplearning/tree/master/assets "assets")|  |
[lab1](/MITDeepLearning/introtodeeplearning/tree/master/lab1 "lab1")| [lab1](/MITDeepLearning/introtodeeplearning/tree/master/lab1 "lab1")|  |
[lab2](/MITDeepLearning/introtodeeplearning/tree/master/lab2 "lab2")| [lab2](/MITDeepLearning/introtodeeplearning/tree/master/lab2 "lab2")|  |
[lab3](/MITDeepLearning/introtodeeplearning/tree/master/lab3 "lab3")| [lab3](/MITDeepLearning/introtodeeplearning/tree/master/lab3 "lab3")|  |
[mitdeeplearning](/MITDeepLearning/introtodeeplearning/tree/master/mitdeeplearning "mitdeeplearning")| [mitdeeplearning](/MITDeepLearning/introtodeeplearning/tree/master/mitdeeplearning "mitdeeplearning")|  |
[xtra_labs](/MITDeepLearning/introtodeeplearning/tree/master/xtra_labs "xtra_labs")| [xtra_labs](/MITDeepLearning/introtodeeplearning/tree/master/xtra_labs "xtra_labs")|  |
[.gitignore](/MITDeepLearning/introtodeeplearning/blob/master/.gitignore ".gitignore")| [.gitignore](/MITDeepLearning/introtodeeplearning/blob/master/.gitignore ".gitignore")|  |
[LICENSE.md](/MITDeepLearning/introtodeeplearning/blob/master/LICENSE.md "LICENSE.md")| [LICENSE.md](/MITDeepLearning/introtodeeplearning/blob/master/LICENSE.md "LICENSE.md")|  |
[README.md](/MITDeepLearning/introtodeeplearning/blob/master/README.md "README.md")| [README.md](/MITDeepLearning/introtodeeplearning/blob/master/README.md "README.md")|  |
[setup.cfg](/MITDeepLearning/introtodeeplearning/blob/master/setup.cfg "setup.cfg")| [setup.cfg](/MITDeepLearning/introtodeeplearning/blob/master/setup.cfg "setup.cfg")|  |
[setup.py](/MITDeepLearning/introtodeeplearning/blob/master/setup.py "setup.py")| [setup.py](/MITDeepLearning/introtodeeplearning/blob/master/setup.py "setup.py")|  |
[test.py](/MITDeepLearning/introtodeeplearning/blob/master/test.py "test.py")| [test.py](/MITDeepLearning/introtodeeplearning/blob/master/test.py "test.py")|  |
View all files

## Repository files navigation

[![banner](/MITDeepLearning/introtodeeplearning/raw/master/assets/banner.png)](http://introtodeeplearning.com)

This repository contains all of the code and software labs for [MIT Introduction to Deep Learning](http://introtodeeplearning.com)! All lecture slides and videos are available on the program website.

# Instructions

[](#instructions)

MIT Introduction to Deep Learning software labs are designed to be completed at your own pace. At the end of each of the labs, there will be instructions on how you can submit your materials as part of the lab competitions. These instructions include what information must be submitted and in what format.

## Opening the labs in Google Colaboratory:

[](#opening-the-labs-in-google-colaboratory)

The 2026 Introduction to Deep Learning labs will be run in Google's Colaboratory, a Jupyter notebook environment that runs entirely in the cloud, so you don't need to download anything. To run these labs, you must have a Google account.

On this Github repo, navigate to the lab folder you want to run (`lab1`, `lab2`, `lab3`) and open the appropriate python notebook (*.ipynb). Click the "Run in Colab" link on the top of the lab. That's it!

## Running the labs

[](#running-the-labs)

Now, to run the labs, open the Jupyter notebook on Colab. Navigate to the "Runtime" tab --> "Change runtime type". In the pop-up window, under "Runtime type" select "Python 3", and under "Hardware accelerator" select "GPU". Go through the notebooks and fill in the `#TODO` cells to get the code to compile for yourself!

### MIT Deep Learning package

[](#mit-deep-learning-package)

You might notice that inside the labs we install the `mitdeeplearning` python package from the Python Package repository:

`pip install mitdeeplearning`

This package contains convienence functions that we use throughout the course and can be imported like any other Python package.

`>>> import mitdeeplearning as mdl`

We do this for you in each of the labs, but the package is also open source under the same license so you can also use it outside the class.

## Lecture Videos

[](#lecture-videos)

[![](/MITDeepLearning/introtodeeplearning/raw/master/assets/video_play.png)](https://www.youtube.com/watch?v=njKP3FqW3Sk&list=PLtBw6njQRU-rwp5__7C0oIVt26ZgjG9NI&index=1)

All lecture videos are available publicly online and linked above! Use and/or modification of lecture slides outside of MIT Introduction to Deep Learning must reference:

> © MIT Introduction to Deep Learning
>
> <http://introtodeeplearning.com>

## License

[](#license)

All code in this repository is copyright 2026 [MIT Introduction to Deep Learning](http://introtodeeplearning.com). All Rights Reserved.

Licensed under the MIT License. You may not use this file except in compliance with the License. Use and/or modification of this code outside of MIT Introduction to Deep Learning must reference:

> © MIT Introduction to Deep Learning
>
> <http://introtodeeplearning.com>

## About

Lab Materials for MIT 6.S191: Introduction to Deep Learning

### Topics

[ mit ](/topics/mit "Topic: mit") [ computer-vision ](/topics/computer-vision "Topic: computer-vision") [ deep-learning ](/topics/deep-learning "Topic: deep-learning") [ tensorflow ](/topics/tensorflow "Topic: tensorflow") [ deep-reinforcement-learning ](/topics/deep-reinforcement-learning "Topic: deep-reinforcement-learning") [ pytorch ](/topics/pytorch "Topic: pytorch") [ neural-networks ](/topics/neural-networks "Topic: neural-networks") [ tensorflow-tutorials ](/topics/tensorflow-tutorials "Topic: tensorflow-tutorials") [ deeplearning ](/topics/deeplearning "Topic: deeplearning") [ jupyter-notebooks ](/topics/jupyter-notebooks "Topic: jupyter-notebooks") [ music-generation ](/topics/music-generation "Topic: music-generation") [ pytorch-tutorial ](/topics/pytorch-tutorial "Topic: pytorch-tutorial")

### Resources

[ Readme ](#readme-ov-file)

### License

[ MIT license ](#MIT-1-ov-file)

###  Uh oh!

There was an error while loading. [Please reload this page]().

[ Activity](/MITDeepLearning/introtodeeplearning/activity)

[ Custom properties](/MITDeepLearning/introtodeeplearning/custom-properties)

### Stars

[ **8.6k** stars](/MITDeepLearning/introtodeeplearning/stargazers)

### Watchers

[ **311** watching](/MITDeepLearning/introtodeeplearning/watchers)

### Forks

[ **4.5k** forks](/MITDeepLearning/introtodeeplearning/forks)

[ Report repository ](/contact/report-content?content_url=https%3A%2F%2Fgithub.com%2FMITDeepLearning%2Fintrotodeeplearning&report=MITDeepLearning+%28user%29)

##  [Releases 13](/MITDeepLearning/introtodeeplearning/releases)

[ v0.7.4 Latest  Jan 8, 2025 ](/MITDeepLearning/introtodeeplearning/releases/tag/v0.7.4)

[\+ 12 releases](/MITDeepLearning/introtodeeplearning/releases)

##  [Packages 0](/orgs/MITDeepLearning/packages?repo_name=introtodeeplearning)

###  Uh oh!

There was an error while loading. [Please reload this page]().

###  Uh oh!

There was an error while loading. [Please reload this page]().

##  [Contributors](/MITDeepLearning/introtodeeplearning/graphs/contributors)

  *   *   *

###  Uh oh!

There was an error while loading. [Please reload this page]().

## Languages

  * [ Jupyter Notebook 97.2% ](/MITDeepLearning/introtodeeplearning/search?l=jupyter-notebook)
  * [ Python 2.8% ](/MITDeepLearning/introtodeeplearning/search?l=python)

You can’t perform that action at this time.
