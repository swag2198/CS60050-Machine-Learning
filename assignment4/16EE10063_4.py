#16EE10063
#Swagatam Haldar
#Assignment 4
#Execute as 'python 16EE10063_4.py'

from __future__ import print_function, division
import numpy as np

dataset = np.genfromtxt('data4.csv', delimiter = ',')
x = dataset[:, :-1]
y = dataset[:, -1]

testset = np.genfromtxt('test4.csv', delimiter = ',')

def distance(test_row, x, m):
    dist = 0
    for i in range(x.shape[1]):
        dist = dist + np.square(x[m][i]-test_row[i])
    dist = np.sqrt(dist)
    return dist

def give_list(test_row, x):
    l = np.empty([x.shape[0],2])
    for i in range(x.shape[0]):
        l[i][0] = distance(test_row, x, i)
        l[i][1] = i
    l = l[l[:,0].argsort()] 
    return l[0:5, :]

def give_majority(l, y):
    m = l.shape[0]
    n_zero = 0
    n_one = 0
    for i in range(m):
        if y[int(l[i][1])]==0:
            n_zero = n_zero + 1
        else:
            n_one = n_one + 1
    if n_one > n_zero:
        return 1
    else:
        return 0

def check_testset(testset, x, y):
    f = open('16EE10063_4.out', 'w')
    for i in range(testset.shape[0]):
        l = give_list(testset[i], x)
        p = give_majority(l,y)
        if p==1:
            f.write('1 ')
        else:
            f.write('0 ')
    f.close()                

check_testset(testset, x, y)                     