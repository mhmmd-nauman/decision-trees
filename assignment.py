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
   #read the csv file in readonly mode
   with open(fname, 'r') as f:
       reader = csv.reader(f)
       #create the data list
       data_list = list(reader)
       return data_list
# get distance between two lists
def get_distance(list1,list2):
    #get the Manhattan distance formula inplace
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
    # return the final distance 
    return res1 + res2
# get maximum from the specified coloumn  
def get_max(matrix,n):
    #set the first element to max by default
    max = matrix[0][n-1]
    #iterate through array to find max element in coulumn
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            #check if its required coulumn number then look for maximum number
            if j == n-1:
                if matrix[i][j] > max:
                    max = matrix[i][j]
    #return the maximum number
    return max
#get minimum from the specified coloumn
def get_min(matrix,n):
    #set the first element as minimum by default
    min = matrix[0][n-1]
    #iterate throgh array list 
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            #if its required coumn number then find the min
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
    #iterate through the array
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            #get the coulumn of the matrix
            col_matrix = column(matrix,j)
            #get the maximun value
            col_max = get_max(matrix,j+1)
            #get the minimum value
            col_min = get_min(matrix,j+1)
            #calculations for standarizaton of the matrix
            for k in range(len(matrix)):
                col_sum = col_sum+col_matrix[k]
            col_avg = col_sum/3 
            # taken from appendix start
            standardized_data[i][j] = matrix[i][j] - col_avg*float(col_max) - col_min 
            col_sum = 0
    return standardized_data
#get the median of the coloumn matrix
def get_median(matrix, n):
    #get the coulmn matrix 
    col_matrix = column(matrix,n-1)
    #get the median of coloumn matrix
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
    #make the keys for cluster classes c0,c1,c2,c3 etc
    for k in range(K):
        a.append("c"+str(k))
    d = {el:0 for el in a}
    for k in range(K):
    	value = randint(0, K)
    	c.append(matrix[value])
    min_distance = 0
    min_distance_index = 0
    #compare the cluster class with all rows in data set
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
        #update the S list 
        S.update({i:min_distance_index})
        min_distance_index = 0
        min_distance = 0
    return S
#get centriod function
def get_centroids(matrix,S, K):
    cluster = S.values()
    # print the S List
    for i in cluster:
        print(matrix[i-1])
    return 1
#run_test function to impliment test runs
def run_test():
    matrix = load_from_csv("Data.csv")
    #K=5
    #K=4
    K=3
    #create the groups 
    S=get_groups(matrix,K)
    #get centriods 
    get_centroids(matrix,S,K)
    return 1

run_test()