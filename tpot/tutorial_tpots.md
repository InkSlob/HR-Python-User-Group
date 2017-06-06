# Based on [MeetUp Event](https://www.meetup.com/757-Python-Users-Group/events/240506687/)
## SETTING UP
```
$ jessewright$ mkdir tpot
$ jessewright$ git checkout -b tpot

Switched to a new branch 'tpot'
```

Suggests you have Python 3
*Installing Python 3 Mac*

```
$ brew install python3
```

Brew may not have rights to write to certain paths

```
$ sudo chown -R ‘<user name>':admin /usr/local/lib
```

Now address the errors that occurred when installing.  For me it was xz and python3

```
$ brew doctor xz
$ brew link xz

$ brew doctor python3
$ brew link python3
```

*Create a virtual environment*

```
$ virtualenv -p python3 venv_tpot
```

Activate venv

```
$ source venv_tpot/bin/activate
```

## TPOTS INSTALLATION
[Source](https://rhiever.github.io/tpot/installing/)

*Install sci-kit learn*

```
$ pip3 install -U scikit-learn
````

DEAP, update_checker, and tqdm can be installed with pip via the command

```
$ pip3  install deap update_checker tqdm
```

Install TPOT

```
$ pip3 install tpot
```

Make virtual environment relocatable

```
$ virtualenv --relocatable venv_tpot
```

## USING TPOT
With the default TPOT settings (100 generations with 100 population size), TPOT will evaluate 10,000 pipeline configurations before finishing. Meaning it is intended to run for hours or days to find the best solution.

