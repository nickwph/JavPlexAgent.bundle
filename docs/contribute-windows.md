## Contribute and get started (MacOS)

1. Star and fork this repository.

2. You need Python (32-bit) and Git installed. Be reminded that Plex only works with 32-bit Python.
- Python 2.7.17 (32-bit): https://www.python.org/ftp/python/2.7.17/python-2.7.17.msi
- Git: https://git-scm.com/download/win

3. Adding Python and Git into command line path
```
setx path "%path%;C:\Program Files\Git\cmd"
setx path "%path%;C:\Python27"
setx path "%path%;C:\Python27\Scripts"
```
   
3. Then install virtualenv:
```shell script
pip install virtualenv
```

4. Get the source code and dependencies ready.
```shell script
git clone git@github.com:nickwph/JavPlexAgent.bundle.git && cd _
virtualenv venv --python C:\Python27\python.exe
venv\Scripts\activate
pip install -r requirements.txt -r requirements_dev.txt
```

5. When you need to test:
```shell script
python build.py
```

6. PyCharm is recommended. 

7. Ask or figure our yourself if you want to do the same in other platforms. 

8. Create a pull request for your changes, tests must pass.

## Error: Microsoft Visual C++ 14.0 is required

Download and install from here:  
[Microsoft Visual C++ Compiler for Python 2.7](https://www.microsoft.com/en-us/download/details.aspx?id=44266)

## ImportError: DLL load failed: %1 is not a valid Win32 application

Plex only works with 32-bit Python, make sure to install the right version.

## DLL load failed: The specified module could not be found.

And from the description you probably see
```
Importing the multiarray numpy extension module failed.  Most
likely you are trying to import a failed build of numpy.
```

*Still investigating*

## IOError: decoder jpeg not available

https://stackoverflow.com/a/22558977