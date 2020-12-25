## Contribute and get started (Ubuntu)

1. Star and fork this repository.

2. You need Python `2.7.17` with ucs2 enabled.
```shell script
export PYTHON_CONFIGURE_OPTS="--enable-unicode=ucs2"
brew install pyenv
pyenv install 2.7.12
pyenv local 2.7.12
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

## UnsupportedOperation: fileno

Patch the file `ImageFile.py` file in `Pillow 1.7.8` because of an incompatible issue.  
Otherwise you get this error: [UnsupportedOperation: fileno](https://stackoverflow.com/a/33300044)

```shell script
patch Virtualenv/lib/python2.7/site-packages/PIL/ImageFile.py < ImageFilePatch.diff
```

## IOError: decoder jpeg not available

1. Plex plugins only work with `Pillow 1.7.8`, make sure to get it's dependency working before the next step.  
Otherwise you get this error: [decoder JPEG not available](https://stackoverflow.com/q/8915296)
```shell script
sudo apt-get install libjpeg-dev
```

2. After this you probably need to force re-install pillow without cache
```shell script
pip install --ignore-installed --force-reinstall --no-cache-dir --upgrade  pillow==1.7.8
```

3. Probably you have to [patch ImageFile.py](#unsupportedoperation-fileno-linux) again.

## Delete and reset cached images

Hate that the posters and backgrounds are sticking around? You have to delete a couple folders to do that. 
The following can be used in Ubuntu, other platform might have different paths.
```shell script
cd "/var/lib/plexmediaserver/Library/Application Support/Plex Media Server" # In Ubuntu
sudo rm -rf Media
sudo rm -rf Metadata
sudo rm -rf Cache
sudo service plexmediaserver restart
```

