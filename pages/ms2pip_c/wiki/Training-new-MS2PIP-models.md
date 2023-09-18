---
title: "Training new MS2PIP models"
layout: default
permalink: "/projects/ms2pip_c/wiki/Training-new-MS2PIP-models"
tags: wiki, ms2pip_c
project: "ms2pip_c"
github_project: "https://github.com/compomics/ms2pip"
---

# Training new MS2PIP models
## Write feature vectors for model training
To compile a feature vector dataset you need to supply the MS2 .mgf file (option `-s`) and the name of the file to write the feature vectors to (option `-w`) to `ms2pipC.py`. The `spec_id` column in the `<peptide file>` should match the `TITLE` field of the corresponding MS2 spectrum in the .mgf file and is used to find the targets for the feature vectors.

## Test feature extraction
In the folder `tests`, run `pytest`. This will run the tests in `test_features.py`, which verify if the feature and target extraction are working properly. (The tests must be updated when we add or remove features!) To do this the `pytest` package must be installed (`pip install pytest`)

## Optimize and train XGBoost models
The script
```
usage: train_xgboost_c.py [-h] [-c INT] [-e FILE] [-p] [-g] <_vectors.pkl> <type>

XGBoost training

positional arguments:
  <_vectors.pkl>  feature vector file
  <type>          model type

optional arguments:
  -h, --help      show this help message and exit
  -c INT          number of CPUs to use
  -e FILE         additional evaluation file
  -p              output plots
  -g              perform Grid Search CV to select best parameters
```
reads the pickled feature vector file `<vectors.pkl or .h5>` and trains
an XGBoost model. The `type` option indicates the ion type for which a
model should be trained. This has to match the name of the column in
the vector file that contains the targets for the given ion type. For
instance `B` will match the column `targetsB` and will lead to a model
for b-ions.

Hyper parameters can be optimized by performing a grid search, using
the argument `g`. Be sure to define the appropriate search space. This
is hard coded in the script.

Optionally, an evaluation vector file can be given. In this case
predictions will be made on these vectors using the final model. If no
evaluation file was given, predictions will be made on the test set.

The script will write the XGBoost models as `.c` files that can be
compiled and linked through Cython. Just put the models in the
`/models` folder, change the `#include` directives in
`ms2pipfeatures_c.c`, and recompile the `ms2pipfeatures_pyx.so` model
by running the `compile.sh` script.
