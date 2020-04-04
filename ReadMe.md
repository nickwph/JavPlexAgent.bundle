JavPlexAgent.bundle
===

<python_version> <build_status> <test_coverage>

# Summary

This is a Plex agent you know what it does, otherwise you won't find this page.

# Usage

1. Download this source

2. In your library setting, select `Jav Media` as the agent.

# Features and Roadmap

These are the supported data source. Checked means supported, while unchecked means will support in the future.

[x] Fanza
[x] Fanza with S1 higher resolution posters 
[x] Fanza with Idea Pocket higher resolution posters 
[x] Caribbeancom
[ ] S-cute
[ ] 1Pondo

# Feature Requests

1. Make sure you have submitted donations.

<form action="https://www.paypal.com/cgi-bin/webscr" method="post" target="_top">
<input type="hidden" name="cmd" value="_s-xclick" />
<input type="hidden" name="hosted_button_id" value="UKKJEAK6TGKGE" />
<input type="image" src="https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif" border="0" name="submit" title="PayPal - The safer, easier way to pay online!" alt="Donate with PayPal button" />
<img alt="" border="0" src="https://www.paypal.com/en_US/i/scr/pixel.gif" width="1" height="1" />
</form>

[Donate](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=UKKJEAK6TGKGE&source=url)

2. Create an issues here

# Contribute and Get Started

1. You need Python 2.7 installed 

2. Get the source code dependencies ready
```shell script
cd <path_to_plex_plugin_directory>
git clone git@github.com:nickwph/JavPlexAgent.bundle.git
cd JavPlexAgent.bundle
virtualenv --python=<path_to_your_python_2.7> Virtualenv
source Virtualenv/bin/activate
pip install -r Requirements.txt
```

3. PyCharm is recommended

4. Create a pull request for your changes, tests must pass 