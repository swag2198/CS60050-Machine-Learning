#16EE10063
#Swagatam Haldar
#Assignment 6
#Execute as 'python 16EE10063_6.py'

from __future__ import print_function, division
import numpy as np

def sigmoid(x):
    return 1/(1+np.exp(-x))

def give_sum(w, x):
    sums = np.zeros(x.shape[0],)
    for i in range(x.shape[0]):
        sums[i] = np.dot(w, x[i]) 
    return sums

def give_class(sig):
    for i in range(sig.shape[0]):
        if sig[i] > 0.5:
            sig[i] = 1
        else:
            sig[i] = 0
    return sig

def give_error(y, y_pred):
    error = 0
    for i in range(y.shape[0]):
        error = error + (y[i] - y_pred[i])*(y[i] - y_pred[i])
    return 0.5*error

def dE_dw(x_, y, y_pred, w):
    grad = np.zeros(w.shape[0],)
    for i in range(w.shape[0]):
        q = 0
        for j in range(x.shape[0]):
            q = q - (y[j] - y_pred[j])*y_pred[j]*(1 - y_pred[j])*x_[j][i]
        grad[i] = q
    return grad

def test(testset, weights):
    sums = give_sum(weights, testset)
    y_pred = sigmoid(sums)
    #print(y_pred)
    return(give_class(y_pred))

dataset = np.genfromtxt('data6.csv', delimiter = ',')
x = dataset[:, :-1]
y = dataset[:, -1]

testset = np.genfromtxt('test6.csv', delimiter = ',')
test_ = np.insert(testset, 0, 1, axis = 1)

x_ = np.insert(x, 0, 1, axis = 1)
w = np.random.randn(x_.shape[1],)

for n in range(10):
    sums = give_sum(w, x_)
    y_pred = sigmoid(sums)
    grad = dE_dw(x_, y, y_pred, w)
    w = w - 0.1*grad

f = open('16EE10063_6.out', 'w')
res = test(test_, w)

for i in range(res.shape[0]):
        if res[i] == 1:
            f.write('1 ')
        else:
            f.write('0 ')
    
f.close()

