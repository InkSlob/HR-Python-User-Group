# Based on [MeetUp Event](https://www.meetup.com/757-Python-Users-Group/events/240506687/)
## SETTING UP
```
$ mkdir tpot
$ git checkout -b tpot

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
The tutorial on TPOTs is based on the TPOTs webpage linked below.
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

Example code for a test run.  This uses a dataset from SciKit Learn.

```
from tpot import TPOTClassifier from sklearn.datasets 
import load_digits from sklearn.model_selection 
import train_test_split 

digits = load_digits()
X_train, X_test, y_train, y_test = train_test_split(digits.data, digits.target, train_size=0.75, test_size=0.25) 

pipeline_optimizer = TPOTClassifier(generations=5, population_size=20, cv=5, random_state=42, verbosity=2) 

pipeline_optimizer.fit(X_train, y_train)
print(pipeline_optimizer.score(X_test, y_test)) pipeline_optimizer.export('tpot_exported_pipeline.py')
```

Running in VENV

```
(venv_tpot) Jesses-MacBook-Pro:tpot jessewright$ python tpot_digits.py
Warning: xgboost.XGBClassifier is not available and will not be used by TPOT.
Generation 1 - Current best internal CV score: 0.9799999582843577               
Generation 2 - Current best internal CV score: 0.9799999582843577               
Generation 3 - Current best internal CV score: 0.9799999582843577               
Generation 4 - Current best internal CV score: 0.9814483571231394               
Generation 5 - Current best internal CV score: 0.9814483571231394               
                                                                                
Best pipeline: KNeighborsClassifier(input_matrix, KNeighborsClassifier__n_neighbors=10, 
                                    KNeighborsClassifier__p=DEFAULT, 
                                    KNeighborsClassifier__weights=distance)
0.982222222222
```

The TPOT optimized pipeline is exported to the *tpot_exported_pipeline.py* file.

```
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

# NOTE: Make sure that the class is labeled 'class' in the data file
tpot_data = np.recfromcsv('PATH/TO/DATA/FILE', delimiter='COLUMN_SEPARATOR', dtype=np.float64)
features = np.delete(tpot_data.view(np.float64).reshape(tpot_data.size, -1), tpot_data.dtype.names.index('class'), axis=1)
training_features, testing_features, training_target, testing_target = \
    train_test_split(features, tpot_data['class'], random_state=42)

exported_pipeline = KNeighborsClassifier(n_neighbors=10, weights="distance")

exported_pipeline.fit(training_features, training_target)
results = exported_pipeline.predict(testing_features)
```

## What did TPOT Do?

POT is a Python tool that automatically creates and optimizes machine learning pipelines using genetic programming.  TPOT will automate the most tedious part of machine learning by intelligently exploring thousands of possible pipelines to find the best one for your data.  

![An example machine learning pipeline](https://github.com/InkSlob/HR-Python-User-Group/tree/master/tpot/images/tpot_ml_pipeline.PNG)

Once TPOT is finished searching (or you get tired of waiting), it provides you with the Python code for the best pipeline it found so you can tinker with the pipeline from there.  

![An example TPOT pipeline](https://github.com/InkSlob/HR-Python-User-Group/tree/master/tpot/images/tpot_pipeline_example.PNG)

## Resources & Articles 

[TPOT: A Python Tool for Automating Data Science](http://www.kdnuggets.com/2016/05/tpot-python-automating-data-science.html/2)
[Machine Learning Tool Seeks to Automate Data Science](https://www.datanami.com/2015/10/19/machine-learning-tool-seeks-to-automate-data-science/)
[Data Science Automation: Debunking Misconceptions](http://www.kdnuggets.com/2016/08/data-science-automation-debunking-misconceptions.html)
[auto-sklearn Manual](https://automl.github.io/auto-sklearn/stable/manual.html#manual)
