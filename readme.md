# JavPlexAgent.bundle
[![Latest Release](https://img.shields.io/badge/latest%20release-v1.2.0-5D87BF.svg)](https://github.com/nickwph/JavPlexAgent.bundle/releases)
![Python](https://img.shields.io/badge/python-2.7-3776AB.svg?logo=python&logoColor=white)
![Build](https://github.com/nickwph/JavPlexAgent.bundle/workflows/build/badge.svg)
[![codecov](https://codecov.io/gh/nickwph/JavPlexAgent.bundle/branch/master/graph/badge.svg)](https://codecov.io/gh/nickwph/JavPlexAgent.bundle)

## Summary

This is a Plex agent you know what it does, otherwise you wouldn't have found this page. Basically it is a pure Python-based project that does everything without companion servers or other stuff. 

## Usage
1. Star this repository
2. Locate the `Plug-Ins` folder according to [this article](https://support.plex.tv/articles/201106098-how-do-i-find-the-plug-ins-folder/)
3. Pick the [latest stable release](https://github.com/nickwph/JavPlexAgent.bundle/releases)
4. Unzip it and place it into the `Plug-Ins` folder
5. In your library setting, select `Plex Movie Scanner` as scanner and `Jav Media` as the agent

## File naming rules 
| Services      | Fromat examples      | Other format variants that also work                  |
| ------------- | -------------------- | ----------------------------------------------------- |
| Fanza         | `SSNI-558`           | `SSNI-558`, `SSNI00558`                               |
| Caribeancom   | `CARIB-123456-123`   | `CARIBBEAN-123456-123`, `CARIBBEANCOM-123456-123`     |
| CaribeancomPR | `CARIBPR-123456_123` | `CARIBBEANPR-123456_123`, `CARIBBEANCOMPR-123456_123` |
| Heyzo         | `HEYZO-2272`         |                                                       |
| 1Pondo        | `1PON-121015_001`    |                                                       |
| KnightVisual  | `KV-094`             | `KV094`                                               |

## Folder structure rules
| Type                     | Formats                    | Format examples                    |
| ------------------------ | -------------------------- | ---------------------------------- |
| Single file              | `ID.EXT`                   | `SSNI-558.MP4`                     |
| Single file in folder    | `ID/WHATEVER.EXT`          | `SSNI-558/INDEX.MP4`               |
| Multiple files           | `ID-ALPHABET.EXT`          | `SSNI-558-A.MP4`, `SSNI-558-B.MP4` |
| Multiple files in folder | `ID-ALPHABET/WHATEVER.EXT` | `SSNI-558/SSNI-558-A.MP4`          |

## Features and roadmap
- [x] Fanza basic support
- [x] Fanza to pick highest resolution poster from sample images (some plaforms are not supported)
- [x] Fanza to retrieve high resolution poster from S1
- [x] Fanza to retrieve high resolution poster from Idea Pocket
- [x] Fanza to crop medium resolution poster from cover image (some plaforms are not supported)
- [x] Fanza to yuse low resolution poster if no higher resolution images found)
- [x] Knights Visual basic support
- [x] Caribbeancom basic support
- [x] CaribbeancomPR basic support
- [x] Heyzo basic support
- [x] 1Pondo basic support
- [x] S-cute basic support (since version 1.3.0)

## Platform supports
- [x] MacOS
- [x] Ubuntu
- [ ] Windows (`numpy`: Importing the multiarray numpy extension module failed)

## Feature requests
[![Donate](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=UKKJEAK6TGKGE&source=url)
1. Make sure you have submitted donations 
2. Star this repository
3. Create an issues here

## Contribute and get started
1. [MacOS](docs/contribute-macos.md)
2. [Ubuntu](docs/contribute-ubuntu.md)
3. [Windows](docs/contribute-windows.md)
