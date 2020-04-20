# JavPlexAgent.bundle

![Python 2.7.12](https://img.shields.io/badge/python-2.7.12-3776AB.svg?logo=python&logoColor=white)
![Build](https://github.com/nickwph/JavPlexAgent.bundle/workflows/build/badge.svg)
[![codecov](https://codecov.io/gh/nickwph/JavPlexAgent.bundle/branch/master/graph/badge.svg)](https://codecov.io/gh/nickwph/JavPlexAgent.bundle)

## Summary

This is a Plex agent you know what it does, otherwise you wouldn't have found this page.

A pure Python based project that does everything without companion servers or other stuff. 

## Usage

1. Star this repository.
2. Locate the Plug-Ins folder according to [this article](https://support.plex.tv/articles/201106098-how-do-i-find-the-plug-ins-folder/).
3. Download this source, unzip it and place it into the Plug-Ins folder.
4. In your library setting, select `Jav Media` as the agent.

## File naming rules

Normal video files

| Format                  | Example                |
|-------------------------|------------------------|
| `/<ID>`                 | /SSNI558.mp4           |
| `/<ID_WITH_DASH>`       | /SSNI-558.mp4          |
| `/<ID_IN_DIGITAL_FORM>` | /SSNI00558.mp4         |
| `/<ID>/<ID>`            | /SSNI-558/SSNI-558.mp4 |
| `/<ID>/<WHATEVER>`      | /SSNI-558/WHATEVER.mp4 |
| `/<WHATEVER>/<ID>`      | /WHATEVER/SSNI-558.mp4 |

Caribbean video files

| Format                   | Example                                |
|--------------------------|----------------------------------------|
| `/<CARIB_ID_SHORT>`      | /Carib-123456-123.mp4                  |
| `/<CARIB_ID_REGULAR>`    | /Caribbean-123456-123.mp4              |
| `/<CARIB_ID_LONG>`       | /Caribbeancom-123456-123.mp4           |
| `/<CARIB_ID>/<CARIB_ID>` | /Carib-123456-123/Carib-123456-123.mp4 |
| `/<CARIB_ID>/<WHATEVER>` | /Carib-123456-123/WHATEVER.mp4         |
| `/<WHATEVER>/<CARIB_ID>` | /WHATEVER/Carib-123456-123.mp4         |

Multipart video files

| Format                               | Example                     |
|--------------------------------------|-----------------------------|
| `/<ID>-<PART_CHARACTER>`             | /SIVR067-A.mp4              |
| `/<ID>-Part<PART_NUMBER>`            | /SIVR067-Part1.mp4          |
| `/<ID>/<PART_CHARACTER>`             | /SIVR067/A.mp4              |
| `/<ID>/Part<PART_NUMBER>`            | /SIVR067/Part1.mp4          |
| `/<ID>/<ID>-<PART_CHARACTER>`        | /SIVR067/SIVR067-A.mp4      |
| `/<WHATEVER>/<ID>-<PART_CHARACTER>`  | /WHATEVER/SIVR067-A.mp4     |
| `/<WHATEVER>/<ID>-Part<PART_NUMBER>` | /WHATEVER/SIVR067-Part1.mp4 |

## Features and roadmap

These are the supported data source. Checked means supported, while unchecked means will support in the future.  

- [x] Fanza
- [x] Fanza (Pick highest resolution poster from sample images) - [disabled if not supported by your platform](#platform-supports-for-features-that-involves-image-processing)
- [x] Fanza (Retrieve high resolution poster from S1)
- [x] Fanza (Retrieve high resolution poster from Idea Pocket)
- [x] Fanza (Crop medium resolution poster from cover image) - [disabled if not supported by your platform](#platform-supports-for-features-that-involves-image-processing)
- [x] Fanza (Use low resolution poster if no higher resolution images found)
- [x] Caribbeancom
- [ ] S-cute
- [ ] 1Pondo

## Platform supports for features that involves image processing

This agent uses `PIL` and `Numpy` to find higher resolution poster images, and not all platforms support it.

- [x] MacOS
- [x] Ubuntu
- [ ] Windows (`Numpy` - DLL load failed: The specified module could not be found.)

## Feature requests

1. Make sure you have submitted donations.  
[![Donate](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=UKKJEAK6TGKGE&source=url)
2. Star this repository.
3. Create an issues here.

## Contribute and get started

1. Star and fork this repository.
2. You need Python `2.7.12` installed, use `pyenv`.
```shell script
export PYTHON_CONFIGURE_OPTS="--enable-unicode=ucs2" # Ubuntu Plex server supports only UCS2
pyenv install 2.7.12
pyenv global 2.7.12
pip install virtualenv
```
3. (Linux) Plex plugins only work with `Pillow 1.7.8`, make sure to get it's dependency working before the next step.  
Otherwise you get this error: [decoder JPEG not available](https://stackoverflow.com/q/8915296)
```shell script
sudo apt-get install libjpeg-dev
```
4. (Windows) Pillow 1.7.8 needs Microsoft Visual C++ 9.0. 
Download and install from [here](https://www.microsoft.com/en-us/download/details.aspx?id=44266)
5. Get the source code dependencies ready.
```shell script
cd "/var/lib/plexmediaserver/Library/Application Support/Plex Media Server/Plug-ins/JavPlexAgent.bundle"
git clone git@github.com:nickwph/JavPlexAgent.bundle.git
cd JavPlexAgent.bundle
virtualenv Virtualenv
source Virtualenv/bin/activate
pip install -r Requirements-Shared.txt -r Requirements-Platform.txt -r Requirements-Test.txt
```
6. Patch the file `ImageFile.py` file in `Pillow 1.7.8` because of an incompatible issue.  
Otherwise you get this error: [UnsupportedOperation: fileno](https://stackoverflow.com/a/33300044)
```shell script
patch Virtualenv/lib/python2.7/site-packages/PIL/ImageFile.py < ImageFilePatch.diff
```
7. PyCharm is recommended. 
8. Create a pull request for your changes, tests must pass.

## Add platform support

Assuming you want to add support to a new platform.

1. Find out which path it is using for this platform.
```shell script
Contents/Libraries/MacOSX/i386
```
2. 
```shell script
pip install -t Contents/Libraries/MacOSX/i386 -r Requirements-Platform.txt
``` 
3. Create a pull request with this change.

## Remarks: Delete and reset cached images

Hate that the posters and backgrounds are sticking around? You have to delete a couple folders to do that.
```shell script
cd "/var/lib/plexmediaserver/Library/Application Support/Plex Media Server"
sudo rm -rf Media
sudo rm -rf Metadata
sudo rm -rf Cache
sudo service plexmediaserver restart
```


