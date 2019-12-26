# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 21:20:27 2019

@author: Muhammad Nauman
"""
import csv
from sklearn.preprocessing import StandardScaler
import statistics
from random import seed
from random import randint
def load_from_csv(fname):
   with open(fname, 'r') as f:
       reader = csv.reader(f)
       your_list = list(reader)
       print(your_list)
def get_distance(list1,list2):
    list1.sort()
    n = len(list1) 
    res1 = 0
    sum1 = 0
    for i in range(n):
        res1 += (list1[i] * i - sum1)
        sum1 += list1[i]
    # second list
    list2.sort()
    n = len(list2) 
    res2 = 0
    sum2 = 0
    for i in range(n):
        res2 += (list2[i] * i - sum2)
        sum2 += list2[i]
    return res1 + res2 
def get_max(matrix,n):
    max = matrix[0][n-1]
    for i in range(3):
        for j in range(3):
            if j == n-1:
                if matrix[i][j] > max:
                    max = matrix[i][j]
    return max
def get_min(matrix,n):
    min = matrix[0][n-1]
    for i in range(3):
        for j in range(3):
            if j == n-1:
                if matrix[i][j] < min:
                    min = matrix[i][j]
    return min
#get single column of matrix 
def column(matrix, i):
    return [row[i] for row in matrix]
def get_standardised_matrix(matrix):
    standardized_data = [[0,0,0],[0,0,0],[0,0,0]]
    col_sum=0
    col_max=0
    col_min=0
    for i in range(3):
        #print(i)
        for j in range(3):
            #print(matrix[i][j])
            col_matrix = column(matrix,j)
            col_max = get_max(matrix,j+1)
            col_min = get_min(matrix,j+1)
            for k in range(3):
                col_sum = col_sum+col_matrix[k]
            col_avg = col_sum/3    
            standardized_data[i][j] = matrix[i][j] - col_avg*float(col_max) - col_min 
            col_sum = 0
                    
    #standardized_data = StandardScaler().fit_transform(matrix)
    return standardized_data
def get_median(matrix, n):
    col_matrix = column(matrix,n-1)
    #print(col_matrix)
    return statistics.median(col_matrix)
def checkKey(dict, key): 
      
    if key in dict.keys(): 
        return 1 
    else: 
        return 0
def get_centroids(matrix,S, K):
    seed(1)
    c = []
    a = []
    dict2 = {'c0': 'female' }
    for k in range(K):
        a.append("c"+str(k))
    
    d = {el:0 for el in a}
    print(d)
    for k in range(K):
    	value = randint(0, 2)
        #a.append("c"+str(k))
    	c.append(matrix[value])
        
        #d = {el:0 for el in a}
        #print(d)
    for i in range(3):
        for j in range(2):
            mlist=get_distance(matrix[i],c[j])
            #cluster[c1].append(c[j])
            print(matrix[i])
            print(c[j])
            key = 'c'+str(j)
            if(checkKey(d, key)):
                c4 = {key:[[1,3],[4,2]]}
                #d.update("c0"=[[1,3],[4,2]])
                d.update(c4)
            c2=[]
            #c2 = clusters.get(ms)
            c2.append([4,4])
            #clusters.update(ms=c2)
          #  myDict.update(c1=[3,4])
            print(d)
        print("done")
    return 1
#load_from_csv("Data.csv")
x = [ -1, 1, 3, 2 ] 
y = [ 5, 6, 5, 3 ] 
#print(get_distance(x, y))
a = [[1,2,3],[2,4,5],[3,5,10]]
for row in a:
    print(' '.join([str(elem) for elem in row]))
#print(get_max(a,1))

#standardized_data = get_standardised_matrix(a)
#print(standardized_data)
#for row in standardized_data:
    #print(' '.join([str(elem) for elem in row]))
#standardized_data_result = StandardScaler().fit_transform(a)
#for row in standardized_data_result:
    #print(' '.join([str(elem) for elem in row]))
#print(get_median(a,1))
get_centroids(a,[1,2,4],2)