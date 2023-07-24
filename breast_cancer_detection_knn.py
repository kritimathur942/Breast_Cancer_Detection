# -*- coding: utf-8 -*-
"""Breast_Cancer_Detection_KNN.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_eW-sYpx3Wk0-MKDYGCFx8rc1qXjuqS2

# K-Nearest Neighbour

## Importing libraries
"""

import pandas as pd
import numpy as np
import matplotlib as plt
import matplotlib.pyplot as plt

"""## Importing dataset"""

data_set = pd.read_csv("/content/Breast Cancer Detection.csv")
X = data_set.iloc[:, :-1].values
y = data_set.iloc[:, -1].values

print(X)
print(y)

"""## Splitting the dataset into Training & Test set"""

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.4, random_state = 42)

"""## Feature Scaling"""

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

"""## KNN Training on Training set"""

from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors= 5, metric = 'minkowski', p = 2)
classifier.fit(X_train, y_train)

"""# Predicting Test set results"""

y_pred = classifier.predict(X_test)
print(np.concatenate((y_pred.reshape(len(y_pred), 1), y_test.reshape(len(y_test), 1)),1))

"""## Confusion Matrix"""

from sklearn.metrics import confusion_matrix, accuracy_score
cm = confusion_matrix(y_test, y_pred)
print(cm)
acs = accuracy_score(y_test, y_pred)
print(acs)