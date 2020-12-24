# Contribute and get started (MacOS)

1. Star and fork this repository.

2. You need Python `2.7.17` installed, recommended to use `pyenv` . 
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
pip install -r requirements.txt -r requirements_platform.txt -r requirements_test.txt
```

5. when you need to test:
```shell script
python build.py ~/Library/Application\ Support/Plex\ Media\ Server/Plug-ins
```

6. PyCharm is recommended. 

7. Ask or figure our yourself if you want to do the same in other platforms. 

8. Create a pull request for your changes, tests must pass.