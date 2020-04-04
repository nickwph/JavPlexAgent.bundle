JavPlexAgent.bundle
===

<python_version> <build_status> <test_coverage>

# Summary

This is a Plex agent you know what it does, otherwise you won't find this page.

# Usage

1. Locate the Plug-Ins folde according to [this article](https://support.plex.tv/articles/201106098-how-do-i-find-the-plug-ins-folder/)

2. Download this source, unzip it and place it into the Plug-Ins folder

3. In your library setting, select `Jav Media` as the agent

# Features and Roadmap

These are the supported data source. Checked means supported, while unchecked means will support in the future.

- [x] Fanza
- [x] Fanza with S1 higher resolution posters 
- [x] Fanza with Idea Pocket higher resolution posters 
- [x] Caribbeancom
- [ ] S-cute
- [ ] 1Pondo

# Feature Requests

1. Make sure you have submitted donations

[![Donate](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=UKKJEAK6TGKGE&source=url)

2. Star this repository

3. Create an issues here

# Contribute and Get Started

1. Star and fork this repository

2. You need Python 2.7 installed 

3. Get the source code dependencies ready
```shell script
cd <path_to_plex_plugin_directory>
git clone git@github.com:nickwph/JavPlexAgent.bundle.git
cd JavPlexAgent.bundle
virtualenv --python=<path_to_your_python_2.7> Virtualenv
source Virtualenv/bin/activate
pip install -r Requirements.txt
```

4. PyCharm is recommended

5. Create a pull request for your changes, tests must pass 