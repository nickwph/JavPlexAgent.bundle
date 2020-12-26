## Contribute and get started

1. Star and fork this repository.

2. You need Python `2.7.17` installed, recommended to use `pyenv`.
```shell script
brew install pyenv
pyenv install 2.7.17
pyenv local 2.7.17
```

3. Then install virtualenv:
```shell script
pip install virtualenv
```

4. Get the source code and dependencies ready.
```shell script
git clone git@github.com:nickwph/JavPlexAgent.bundle.git && cd _
virtualenv venv --python $(pyenv which python)
source venv/bin/activate
pip install -r requirements.txt -r requirements_dev.txt
```

5. When you need to test:
```shell script
python build.py
```

6. PyCharm is recommended. 

7. Ask or figure our yourself if you want to do the same in other platforms. 

8. Create a pull request for your changes, tests must pass.

## Mapped file has no cdhash, completely unsigned?

The reason is the `Python` that Plex for Mac uses is signed, while the native libraries PIL and numpy 
cannot be signed with that certificate. The solution is the remove the signature of the `Python`:
```shell script
codesign --remove-signature /Applications/Plex\ Media\ Server.app/Contents/MacOS/Plex\ Script\ Host
``` 

## Fatal error: 'X11/Xlib.h' file not found

https://stackoverflow.com/questions/11465258/xlib-h-not-found-when-building-graphviz-on-mac-os-x-10-8-mountain-lion

```shell script
export XCODE_DEVELOPER=$(xcode-select -p)
export MACOS_SDK=$XCODE_DEVELOPER/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk
export X11=$MACOS_SDK/System/Library/Frameworks/Tk.framework/Versions/8.5/Headers/X11
ln -s $X11 /usr/local/include/X11
```