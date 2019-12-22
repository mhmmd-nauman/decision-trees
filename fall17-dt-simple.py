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
# Figures inline and set visualization style
#%matplotlib inline
#sns.set()

# Import data
df_train = pd.read_csv('fall-17-simple-for-weka-65-2019-04-12_py.csv')
survived_train = df_train.Result
#print(survived_train.values)
data = df_train
data = pd.get_dummies(data, columns=['Quota','Hafiz-e-Quran','Result'], drop_first=True)
#print(data.values)
#survived_train = pd.get_dummies(survived_train, columns=['Offered'], drop_first=True)
#print(survived_train.values)
#y = pd.Categorical.from_codes(survived_train.values, data)
#print(y.values)
data = data[['Quota_OPEN', 'Hafiz-e-Quran_Yes', 'NTS', 'BA-BSC']]
#print(data.head())
data_train = data.iloc[:112]
data_test = data.iloc[112:]
X = data_train.values
y = survived_train.values

#print(y)
clf = tree.DecisionTreeClassifier()
#print(X)
clf.fit(X, y)

tree.DecisionTreeClassifier(class_weight=None, criterion='entropy', max_depth=3,
            max_features=None, max_leaf_nodes=None,
            min_impurity_decrease=0.0, min_impurity_split=None,
            min_samples_leaf=1, min_samples_split=2,
            min_weight_fraction_leaf=0.0, presort=False, random_state=None,
            splitter='best')

dot_data = tree.export_graphviz(clf, out_file=None, 
                     feature_names=['Quota_OPEN', 'Hafiz-e-Quran_Yes', 'NTS', 'BA-BSC'],  
                     class_names=['Admitted','Rejected'],  
                     filled=True, rounded=True,  
                     special_characters=True)  
graph = graphviz.Source(dot_data)  
graph.render("dtree-simple") 