#16EE10063
#Swagatam Haldar
#Assignment 3
#Execute as 'python 16EE10063_3.py'

from __future__ import print_function, division
import numpy as np

dataset = np.genfromtxt('data3.csv', delimiter = ',')
x = dataset[:, :-1]
y = dataset[:, -1]

def p_y(val, y):
    m = y.shape[0]
    n = np.count_nonzero(y)
    n_ = m-n
    if val == 0:
        return (n_+2)
    else:
        return (n+2)

def pabs_y(val, y):
    m = y.shape[0]
    n = np.count_nonzero(y)
    n_ = m-n
    if val == 0:
        return (n_)/m
    else:
        return (n)/m

def p_a_int_y(a, y, a_val, y_val):
    m = a.shape[0]
    n_int = 1
    for i in range(m):
        if a[i] == a_val and y[i] == y_val:
            n_int = n_int + 1
    return n_int

def p_att(x, y, i, att_val, y_val):
    (m,n) = x.shape
    a = x[:,i]
    n_a1 = np.count_nonzero(a)
    n_a0 = m - n_a1
    if att_val == 0:
        if y_val == 0:
            return p_a_int_y(a, y, 0, 0)/p_y(0, y)
        if y_val == 1:
            return p_a_int_y(a, y, 0, 1)/p_y(1, y)
    elif att_val == 1:
        if y_val == 0:
            return p_a_int_y(a, y, 1, 0)/p_y(0, y)
        if y_val == 1:
            return p_a_int_y(a, y, 1, 1)/p_y(1, y)

testset = np.genfromtxt('test3.csv', delimiter = ',')

def give_prob(x_row, y_val, x_data, y_data):
    v_map = pabs_y(y_val,y)
    for i in range(x_row.shape[0]):
        v_map = v_map * p_att(x_data, y_data, i, x_row[i], y_val)
    return v_map 

def predict_prob(testset, x_data, y_data):
    m = testset.shape[0]
    f = open('16EE10063_3.out', 'w')
    for i in range(m):
        a = give_prob(testset[i,:], 0, x_data, y_data)
        a_ = give_prob(testset[i,:], 1, x_data, y_data)

        if a>a_:
            f.write('0 ')
        else:
            f.write('1 ')
    f.close()
    
predict_prob(testset, x , y)                                               