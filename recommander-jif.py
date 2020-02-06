# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 22:26:48 2020

@author: iub
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
df_train = pd.read_csv('sp18-for-weka-2020-01-19-jif-clean.csv')
#df_train = pd.read_csv('fall-17-for-weka-65-2019-04-12_py.csv')
survived_train = df_train.Programme
#survived_train = df_train.Admission_Quota
#print(survived_train.values)

data = df_train
data = pd.get_dummies(data, columns=['Domicile','Programme'], drop_first=True)
#data = pd.get_dummies(data, columns=['Quota','Hafiz-e-Quran','Admission_Quota'], drop_first=True)
print(data.values)

data = data[['Domicile_OPEN', 'Merit Score']]
print(data.head())

data_train = data.iloc[:1087]
data_test = data.iloc[1087:]
X = data_train.values
y = survived_train.values

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
                     class_names=['BS CS','BS Mathematics','BBA (Hons) after 12 years of education',
                                  'BS Applied Psychology','BS Economics','BSc (Hons) Agriculture',
                                  'BS Statistics','BS Physics',
                                  'BS Geography','BS Chemistry (E)',
                                  'BS IT','BS Commerce',
                                  'BS Islamic Studies','BS Social Work','BEd 4-years (after FA/FSc)',
                                  'BS Secondary Education',
                                  'BS Political Science','BS Public Administration','BS Media Studies',
                                  'BS Library & Information Science','BA(Hons) English'],  
                     filled=True, rounded=True,  
                     special_characters=True)  
graph = graphviz.Source(dot_data)  
graph.render("dtree_jif") 
