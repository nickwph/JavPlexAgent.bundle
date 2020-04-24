# JavPlexAgent.bundle

[![Latest Release](https://img.shields.io/badge/latest%20release-v1.0.0-5D87BF.svg)](https://github.com/nickwph/JavPlexAgent.bundle/releases)
![Master Version](https://img.shields.io/badge/master%20version-v1.1.0.alpha-5D87BF.svg)
![Python](https://img.shields.io/badge/python-2.7-3776AB.svg?logo=python&logoColor=white)
![Build](https://github.com/nickwph/JavPlexAgent.bundle/workflows/build/badge.svg)
[![codecov](https://codecov.io/gh/nickwph/JavPlexAgent.bundle/branch/master/graph/badge.svg)](https://codecov.io/gh/nickwph/JavPlexAgent.bundle)

## Summary

This is a Plex agent you know what it does, otherwise you wouldn't have found this page.

A pure Python based project that does everything without companion servers or other stuff. 

## Usage

1. Star this repository.
2. Locate the Plug-Ins folder according to [this article](https://support.plex.tv/articles/201106098-how-do-i-find-the-plug-ins-folder/).
3. Pick the [latest stable release](https://github.com/nickwph/JavPlexAgent.bundle/releases) or download this latest source code
4. Unzip it and place it into the Plug-Ins folder.
5. In your library setting, select `Jav Media` as the agent.

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
- [x] Fanza (Actress images)
- [x] Fanza (Pick highest resolution poster from sample images) - [disabled if not supported by your platform](#platform-supports-for-features-that-involves-image-processing)
- [x] Fanza (Retrieve high resolution poster from S1)
- [x] Fanza (Retrieve high resolution poster from Idea Pocket)
- [x] Fanza (Crop medium resolution poster from cover image) - [disabled if not supported by your platform](#platform-supports-for-features-that-involves-image-processing)
- [x] Fanza (Use low resolution poster if no higher resolution images found)
- [x] Knights Visual
- [ ] Knights Visual (Actress images)
- [x] Caribbeancom
- [ ] Caribbeancom (Actress images)
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

## Contribute and get started (in Ubuntu)

1. Star and fork this repository.
2. You need Python `2.7.12` installed, recommended to use `pyenv`.
```shell script
export PYTHON_CONFIGURE_OPTS="--enable-unicode=ucs2" # Ubuntu Plex server supports only UCS2
pyenv install 2.7.12
pyenv global 2.7.12
pip install virtualenv
```
3. Get the source code and dependencies ready.
```shell script
cd "/var/lib/plexmediaserver/Library/Application Support/Plex Media Server/Plug-ins/JavPlexAgent.bundle"
git clone git@github.com:nickwph/JavPlexAgent.bundle.git
cd JavPlexAgent.bundle
virtualenv Virtualenv
source Virtualenv/bin/activate
pip install -r Requirements-Platform.txt -r Requirements-Shared.txt -r Requirements-Test.txt
```
4. Make sure you have [installed JEPG decoder](#ioerror-decoder-jpeg-not-available-linux) and you have [patched ImageFile.py](#unsupportedoperation-fileno-linux).
5. PyCharm is recommended. 
6. Ask or figure our yourself if you want to do the same in other platforms. 
6. Create a pull request for your changes, tests must pass.

## UnsupportedOperation: fileno (Linux)

Patch the file `ImageFile.py` file in `Pillow 1.7.8` because of an incompatible issue.  
Otherwise you get this error: [UnsupportedOperation: fileno](https://stackoverflow.com/a/33300044)
```shell script
patch Virtualenv/lib/python2.7/site-packages/PIL/ImageFile.py < ImageFilePatch.diff
```

## IOError: decoder jpeg not available (Linux)

1. Plex plugins only work with `Pillow 1.7.8`, make sure to get it's dependency working before the next step.  
Otherwise you get this error: [decoder JPEG not available](https://stackoverflow.com/q/8915296)
```shell script
sudo apt-get install libjpeg-dev
```
2. After this you probably need to force re-install pillow without cache
```shell script
pip install -I --force-reinstall --no-cache-dir -v --upgrade  pillow==1.7.8
```
3. Probably you have to [patch ImageFile.py](#unsupportedoperation-fileno-linux) again.

## Error: Microsoft Visual C++ 14.0 is required (Windows)

Download and install from [here](https://www.microsoft.com/en-us/download/details.aspx?id=44266)

## Remarks: Delete and reset cached images

Hate that the posters and backgrounds are sticking around? You have to delete a couple folders to do that. 
The following can be used in Ubuntu, other platform might have different paths.
```shell script
cd "/var/lib/plexmediaserver/Library/Application Support/Plex Media Server" # In Ubuntu
sudo rm -rf Media
sudo rm -rf Metadata
sudo rm -rf Cache
sudo service plexmediaserver restart
```


