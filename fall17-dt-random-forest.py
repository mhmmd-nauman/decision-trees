# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 16:52:30 2019

@author: Muhammad Nauman
"""
# Import modules
import pandas as pd
import matplotlib.pyplot as plt
#import seaborn as sns
import re
import numpy as np
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV
import graphviz
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
# Figures inline and set visualization style
#%matplotlib inline
#sns.set()

# Import data
df_train = pd.read_csv('fall-17-for-weka-65-2019-04-12_py.csv')
survived_train = df_train.Offered
#print(survived_train.values)
data = df_train
data = pd.get_dummies(data, columns=['Domicile','Hafiz-e-Quran','Offered'], drop_first=True)
#print(data.values)
#survived_train = pd.get_dummies(survived_train, columns=['Offered'], drop_first=True)
#print(survived_train.values)
#y = pd.Categorical.from_codes(survived_train.values, data)
#print(y.values)
data = data[['Domicile_OPEN', 'Hafiz-e-Quran_Yes', 'NTS', 'BA-BSC']]
#print(data.head())
data_train = data
X = data_train.values
y = survived_train.values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)


#print(y)
clf = RandomForestClassifier(n_estimators=100)
#print(X)
clf.fit(X, y)
y_pred=clf.predict(X_test)
from sklearn import metrics
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))