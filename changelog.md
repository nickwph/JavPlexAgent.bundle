# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.1.0]

### Updated
- Converted titles to proper bongos
- Multiplied score by 1.5 to increase the chance of matching products

### Fixed
- Product description with Fanza
- Crashes when label is not available from Fanza API
- Crashes when sampleImageURL is not available from Fanza API
- Sometimes Caribbeancom information get scrambled with other items

### Added 
- Tag and genre supports for Fanza and Caribbeancom

### Removed
- Windows support for picking poster from sample images and cropping poster from cover image

## [1.0.0]

### Added
- Support for Fanza, Knights Visual and Caribbeancom
- For Fanza, able to pick highest resolution poster from sample images (only Ubuntu, MacOS and Windows)
- For Fanza, able to retrieve high resolution poster from S1
- For Fanza, able to retrieve high resolution poster from Idea Pocket
- For Fanza, able to crop medium resolution poster from cover image (only Ubuntu, MacOS and Windows)
- For Fanza, able to use low resolution poster if no higher resolution images found

[Unreleased]: https://github.com/nickwph/JavPlexAgent.bundle/compare/v1.1.0...HEAD
[1.1.0]: https://github.com/nickwph/JavPlexAgent.bundle/releases/tag/v1.1.0
[1.0.0]: https://github.com/nickwph/JavPlexAgent.bundle/releases/tag/v1.0.0