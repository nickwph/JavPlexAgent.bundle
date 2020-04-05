# JavPlexAgent.bundle

![Python 2.7](https://img.shields.io/badge/python-2.7-3776AB.svg?logo=python&logoColor=white)
![Build](https://github.com/nickwph/JavPlexAgent.bundle/workflows/build/badge.svg)
[![codecov](https://codecov.io/gh/nickwph/JavPlexAgent.bundle/branch/master/graph/badge.svg)](https://codecov.io/gh/nickwph/JavPlexAgent.bundle)

## Summary

This is a Plex agent you know what it does, otherwise you wouldn't have found this page.

A pure Python based project that does everything without companion servers or other stuff. 

## Usage

1. Locate the Plug-Ins folde according to [this article](https://support.plex.tv/articles/201106098-how-do-i-find-the-plug-ins-folder/).
2. Download this source, unzip it and place it into the Plug-Ins folder.
3. In your library setting, select `Jav Media` as the agent.

## Features and Roadmap

These are the supported data source. Checked means supported, while unchecked means will support in the future.

- [x] Fanza
- [x] Fanza with S1 higher resolution posters 
- [x] Fanza with Idea Pocket higher resolution posters 
- [x] Caribbeancom
- [ ] S-cute
- [ ] 1Pondo

## Feature Requests

1. Make sure you have submitted donations.  
[![Donate](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=UKKJEAK6TGKGE&source=url)
2. Star this repository.
3. Create an issues here.

## Contribute and Get Started

1. Star and fork this repository.
2. You need Python `2.7.12` installed, use `pyenv`.
```shell script
export PYTHON_CONFIGURE_OPTS="--enable-unicode=ucs2" # Ubuntu Plex server supports only UCS2
pyenv install 2.7.12
pyenv global 2.7.12
pip install virtualenv
```
3. Only Pillow 1.7.8 works in the plugin, make sure to get it's dependency working before the next step  
Otherwise you get this error: decoder JPEG not available  
https://stackoverflow.com/q/8915296
```shell script
sudo apt-get install libjpeg-dev
```
4. Get the source code dependencies ready.
```shell script
cd "/var/lib/plexmediaserver/Library/Application Support/Plex Media Server/Plug-ins/JavPlexAgent.bundle"
git clone git@github.com:nickwph/JavPlexAgent.bundle.git
cd JavPlexAgent.bundle
virtualenv --python=~/.pyenv/shims/python Virtualenv
source Virtualenv/bin/activate
pip install -r Requirements.txt
```
5. PyCharm is recommended.
6. Create a pull request for your changes, tests must pass.

## Remarks