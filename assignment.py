# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 21:20:27 2019

"""
import csv
import statistics
from random import seed
from random import randint
#function to load the csv file
def load_from_csv(fname):
   #read the csv file
   with open(fname, 'r') as f:
       reader = csv.reader(f)
       data_list = list(reader)
       return data_list
# get distance between two lists
def get_distance(list1,list2):
    #process the first list
    list1.sort()
    n = len(list1) 
    res1 = 0
    sum1 = 0
    for i in range(n):
        res1 += (float(list1[i]) * i - sum1)
        sum1 += float(list1[i])
    # process the second list
    list2.sort()
    n = len(list2) 
    res2 = 0
    sum2 = 0
    for i in range(n):
        res2 += (float(list2[i]) * i - sum2)
        sum2 += float(list2[i])
    return res1 + res2
# get maximum from the specified coloumn  
def get_max(matrix,n):
    max = matrix[0][n-1]
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if j == n-1:
                if matrix[i][j] > max:
                    max = matrix[i][j]
    return max
#get minimum from the specified coloumn
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
#convert the matrix to standard matrix
def get_standardised_matrix(matrix):
    standardized_data = []
    col_sum=0
    col_max=0
    col_min=0
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            col_matrix = column(matrix,j)
            col_max = get_max(matrix,j+1)
            col_min = get_min(matrix,j+1)
            for k in range(len(matrix)):
                col_sum = col_sum+col_matrix[k]
            col_avg = col_sum/3 
            # taken from appendix start
            standardized_data[i][j] = matrix[i][j] - col_avg*float(col_max) - col_min 
            col_sum = 0
    return standardized_data
def get_median(matrix, n):
    col_matrix = column(matrix,n-1)
    return statistics.median(col_matrix)
#check if the key exist in list
def checkKey(dict, key): 
    if key in dict.keys(): 
        return 1 
    else: 
        return 0
def get_groups(matrix, K):
    seed(1)
    c = [] # to hold the cluster
    a = [] # temp variable
    S = {} # to hold S list 
    for k in range(K):
        a.append("c"+str(k))
    d = {el:0 for el in a}
    for k in range(K):
    	value = randint(0, K)
    	c.append(matrix[value])
    min_distance = 0
    min_distance_index = 0
    for i in range(len(matrix)):
        for j in range(K):
            #logic the check the distance of c1,c2..ck to Di
            distance=get_distance(matrix[i],c[j])
            if(min_distance == 0):
                min_distance = distance
                min_distance_index = 0
            if(min_distance > distance):
                min_distance = distance
                min_distance_index = j
            key = 'c'+str(j)
            if(checkKey(d, key)):
                c4 = {key:c[j]}
                d.update(c4)
        S.update({i:min_distance_index})
        min_distance_index = 0
        min_distance = 0
    return S
def get_centroids(matrix,S, K):
    cluster = S.values()
    for i in cluster:
        print(matrix[i-1])
    return 1
#run_test function to impliment test runs
def run_test():
    matrix = load_from_csv("Data.csv")
    #K=5
    #K=4
    K=3
    S=get_groups(matrix,K)
    get_centroids(matrix,S,K)
    return 1

run_test()