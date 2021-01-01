# Changelog

## [Unreleased]

**Updates in this version:**
- Added support for S-Cute
- Improved debugging environment in released versions

## [1.2.0]

**Updates in this version:**
- Added support for CaribbeancomPR, Heyzo and 1Pondo
- Added code to add paddings to poster images, to avoid cropping too many pixels
- Reduce time needed for each updating each item be limiting maximum artwork count
- Restructured code to a become a compile-based structure and allow subdirectory modules in code
- Compiled bundle size is reduced to size at around 55MB as libraries for other platforms are no longer included
- Improved development support in Ubuntu and MacOS

**Known issues**
- Windows is still not supported as it is still failing with error "Importing the multiarray numpy extension module failed"

## [1.1.0]

**Updates in this version:**
- Converted titles to proper bongos
- Multiplied score by 1.5 to increase the chance of matching products
- Fixed product description with Fanza
- Fixed crashes when label is not available from Fanza API
- Fixed crashes when sampleImageURL is not available from Fanza API
- Fixed issue with that sometimes Caribbeancom information get scrambled with other items
- Added tag and genre supports for Fanza and Caribbeancom
- Removed Windows support for picking poster from sample images and cropping poster from cover image

## [1.0.0]

**Updates in this version:**
- Fanza basic support
- Fanza to download actress images
- Fanza to pick highest resolution poster from sample images (some plaforms are not supported)
- Fanza to retrieve high resolution poster from S1
- Fanza to retrieve high resolution poster from Idea Pocket
- Fanza to crop medium resolution poster from cover image (some plaforms are not supported)
- Fanza to use low resolution poster if no higher resolution images found
- Knights Visual basic support
- Caribbeancom basic support

**Known issues**
- Windows is not supported as it is still failing in with error "DLL load failed: The specified module could not be found"

[Unreleased]: https://github.com/nickwph/JavPlexAgent.bundle/compare/v1.2.0...HEAD
[1.2.0]: https://github.com/nickwph/JavPlexAgent.bundle/releases/tag/v1.2.0
[1.1.0]: https://github.com/nickwph/JavPlexAgent.bundle/releases/tag/v1.1.0
[1.0.0]: https://github.com/nickwph/JavPlexAgent.bundle/releases/tag/v1.0.0