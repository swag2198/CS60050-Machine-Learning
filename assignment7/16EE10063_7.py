#16EE10063
#Swagatam Haldar
#Assignment 7
#Execute as 'python 16EE10063_7.py'

from __future__ import print_function, division
import numpy as np

dataset = np.genfromtxt('data7.csv', delimiter = ',')
x = dataset

(m,n) = x.shape

def dist(x, y):
    return np.linalg.norm(x-y)

cent = np.zeros((2,8))
for i in range(2):
    cent[i] = x[np.random.randint(0, m - 1)]

label = np.zeros((m, 1))

for i in range(10):
    for j in range(m):
        d1 = dist(x[j], cent[0])
        d2 = dist(x[j], cent[1])
        if d1<d2:
            label[j][0] = 1
        else:
            label[j][0] = 2
    count1 = 0
    count2 = 0
    sum1 = np.zeros((1,8))
    sum2 = np.zeros((1,8))
    for k in range(m):
        if(label[k][0] == 1):
            sum1 = sum1 + x[k]
            count1 = count1 + 1
        else:
            sum2 = sum2 + x[k]
            count2 = count2 + 1
    cent[0] = sum1/count1
    cent[1] = sum2/count2

f = open('16EE10063_7.out', 'w')

for i in range(m):
        if label[i][0] == 1:
            f.write('1 ')
        else:
            f.write('2 ')
    
f.close()