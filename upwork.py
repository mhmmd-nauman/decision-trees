# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 21:20:27 2019

"""
import csv
from sklearn.preprocessing import StandardScaler
import statistics
from random import seed
from random import randint
def load_from_csv(fname):
   with open(fname, 'r') as f:
       reader = csv.reader(f)
       data_list = list(reader)
       return data_list
def get_distance(list1,list2):
    list1.sort()
    n = len(list1) 
    res1 = 0
    sum1 = 0
    for i in range(n):
        res1 += (float(list1[i]) * i - sum1)
        sum1 += float(list1[i])
    # second list
    list2.sort()
    n = len(list2) 
    res2 = 0
    sum2 = 0
    for i in range(n):
        res2 += (float(list2[i]) * i - sum2)
        sum2 += float(list2[i])
    return res1 + res2 
def get_max(matrix,n):
    max = matrix[0][n-1]
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if j == n-1:
                if matrix[i][j] > max:
                    max = matrix[i][j]
    return max
def get_min(matrix,n):
    min = matrix[0][n-1]
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if j == n-1:
                if matrix[i][j] < min:
                    min = matrix[i][j]
    return min
#get single column of matrix 
def column(matrix, i):
    return [row[i] for row in matrix]
def get_standardised_matrix(matrix):
    standardized_data = []
    col_sum=0
    col_max=0
    col_min=0
    for i in range(len(matrix)):
        #print(i)
        for j in range(len(matrix)):
            #print(matrix[i][j])
            col_matrix = column(matrix,j)
            col_max = get_max(matrix,j+1)
            col_min = get_min(matrix,j+1)
            for k in range(len(matrix)):
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
def get_groups(matrix, K):
    seed(1)
    c = []
    a = []
    S = {}
    for k in range(K):
        a.append("c"+str(k))
    
    d = {el:0 for el in a}
    #print(d)
    for k in range(K):
    	value = randint(0, K)
    	c.append(matrix[value])
    
    min_distance = 0
    min_distance_index = 0
    for i in range(len(matrix)):
        for j in range(K):
            distance=get_distance(matrix[i],c[j])
            if(min_distance == 0):
                min_distance = distance
                min_distance_index = 0
            if(min_distance > distance):
                min_distance = distance
                min_distance_index = j
            ##print(str(i) + " " + str(j) + " "+str(distance))
            key = 'c'+str(j)
            if(checkKey(d, key)):
                c4 = {key:c[j]}
                d.update(c4)
            #print(d)
        #print(min_distance_index)
        #print(min_distance)
        S.update({i:min_distance_index})
        #S needs to be adjusted here
        min_distance_index = 0
        min_distance = 0
        #print("done")
        #print(S)
    return S
def get_centroids(matrix,S, K):
    cluster = S.values()
    for i in cluster:
        print(matrix[i-1])
    return 1
matrix = load_from_csv("Data.csv")
K=7 
#print(get_distance(x, y))
#a = [[1,2,3],[2,4,5],[3,5,10]]
for row in matrix:
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
S=get_groups(matrix,K)
#print(S)
get_centroids(matrix,S,K)