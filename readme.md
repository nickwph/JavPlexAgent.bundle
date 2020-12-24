# JavPlexAgent.bundle

[![Latest Release](https://img.shields.io/badge/latest%20release-v1.1.0-5D87BF.svg)](https://github.com/nickwph/JavPlexAgent.bundle/releases)
![Master Version](https://img.shields.io/badge/master%20version-v1.2.0-5D87BF.svg)  
![Python](https://img.shields.io/badge/python-2.7-3776AB.svg?logo=python&logoColor=white)
![Build](https://github.com/nickwph/JavPlexAgent.bundle/workflows/build/badge.svg)
[![codecov](https://codecov.io/gh/nickwph/JavPlexAgent.bundle/branch/master/graph/badge.svg)](https://codecov.io/gh/nickwph/JavPlexAgent.bundle)

## Summary

This is a Plex agent you know what it does, otherwise you wouldn't have found this page.

A pure Python based project that does everything without companion servers or other stuff. 

## Usage

1. Star this repository.
2. Locate the `Plug-Ins` folder according to [this article](https://support.plex.tv/articles/201106098-how-do-i-find-the-plug-ins-folder/).
3. Pick the [latest stable release](https://github.com/nickwph/JavPlexAgent.bundle/releases) or download this latest source code
4. Unzip it and place it into the `Plug-Ins` folder.
5. In your library setting, select `Jav Media` as the agent.

## File naming rules

Normal video files

| Format                  | Example                  |
|-------------------------|--------------------------|
| `/<ID>`                 | `/SSNI558.mp4`           |
| `/<ID_WITH_DASH>`       | `/SSNI-558.mp4`          |
| `/<ID_IN_DIGITAL_FORM>` | `/SSNI00558.mp4`         |
| `/<ID>/<ID>`            | `/SSNI-558/SSNI-558.mp4` |
| `/<ID>/<WHATEVER>`      | `/SSNI-558/WHATEVER.mp4` |
| `/<WHATEVER>/<ID>`      | `/WHATEVER/SSNI-558.mp4` |

Caribbean video files

| Format                   | Example                                  |
|--------------------------|------------------------------------------|
| `/<CARIB_ID_SHORT>`      | `/Carib-123456-123.mp4`                  |
| `/<CARIB_ID_REGULAR>`    | `/Caribbean-123456-123.mp4`              |
| `/<CARIB_ID_LONG>`       | `/Caribbeancom-123456-123.mp4`           |
| `/<CARIB_ID>/<CARIB_ID>` | `/Carib-123456-123/Carib-123456-123.mp4` |
| `/<CARIB_ID>/<WHATEVER>` | `/Carib-123456-123/WHATEVER.mp4`         |
| `/<WHATEVER>/<CARIB_ID>` | `/WHATEVER/Carib-123456-123.mp4`         |

Multipart video files

| Format                               | Example                       |
|--------------------------------------|-------------------------------|
| `/<ID>-<PART_CHARACTER>`             | `/SIVR067-A.mp4`              |
| `/<ID>-Part<PART_NUMBER>`            | `/SIVR067-Part1.mp4`          |
| `/<ID>/<PART_CHARACTER>`             | `/SIVR067/A.mp4`              |
| `/<ID>/Part<PART_NUMBER>`            | `/SIVR067/Part1.mp4`          |
| `/<ID>/<ID>-<PART_CHARACTER>`        | `/SIVR067/SIVR067-A.mp4`      |
| `/<WHATEVER>/<ID>-<PART_CHARACTER>`  | `/WHATEVER/SIVR067-A.mp4`     |
| `/<WHATEVER>/<ID>-Part<PART_NUMBER>` | `/WHATEVER/SIVR067-Part1.mp4` |

## Features and roadmap

These are the supported data source. Checked means supported, while unchecked means will support in the future.  

- [x] Fanza
- [ ] Fanza (English support)
- [x] Fanza (Actress images)
- [x] Fanza (Pick highest resolution poster from sample images) - [disabled if not supported by your platform](#platform-supports-for-features-that-involves-image-processing)
- [x] Fanza (Retrieve high resolution poster from S1)
- [x] Fanza (Retrieve high resolution poster from Idea Pocket)
- [x] Fanza (Crop medium resolution poster from cover image) - [disabled if not supported by your platform](#platform-supports-for-features-that-involves-image-processing)
- [x] Fanza (Use low resolution poster if no higher resolution images found)
- [x] Knights Visual
- [ ] Knights Visual (Actress images)
- [ ] Knights Visual (English support)
- [x] Caribbeancom
- [ ] Caribbeancom (Actress images)
- [ ] Caribbeancom (English support)
- [ ] S-cute
- [ ] 1Pondo

## Platform supports for features that involves image processing

This agent uses `PIL` and `Numpy` to find higher resolution poster images, and not all platforms support it.

- [x] MacOS
- [x] Ubuntu
- [ ] Windows (`Numpy` - DLL load failed: The specified module could not be found)

## Feature requests

1. Make sure you have submitted donations.  
[![Donate](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=UKKJEAK6TGKGE&source=url)
2. Star this repository.
3. Create an issues here.

## Error: Microsoft Visual C++ 14.0 is required (Windows)

Download and install from [here](https://www.microsoft.com/en-us/download/details.aspx?id=44266)

## Contribute and get started
1. MacOS
2. Ubuntu
3. Windows
