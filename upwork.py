# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 21:20:27 2019

@author: Muhammad Nauman
"""
import csv
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
load_from_csv("Data.csv")
x = [ -1, 1, 3, 2 ] 
y = [ 5, 6, 5, 3 ] 
print(get_distance(x, y))
a = [[1,2,3],[3,4,5],[6,4,5]]
for row in a:
    print(' '.join([str(elem) for elem in row]))
print(get_min(a,1))