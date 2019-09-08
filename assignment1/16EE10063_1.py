#16EE10063
#Swagatam Haldar
#Assignment 1
#Execute as 'python 16EE10063_1.py data1.csv' (example)

from __future__ import print_function
import numpy as np
import sys
dataset = np.genfromtxt(sys.argv[1], delimiter = ',')
x = dataset[:, :-1]
y = dataset[:, -1]
hyp = x[0]        
for i in range(hyp.shape[0]):
    if hyp[i]==0:
        hyp[i] = -1

for i in range(x.shape[0]-1):
    if(y[i+1]==1):
        for j in range(hyp.shape[0]):
            if hyp[j]==1 and x[i+1][j]==1:
                continue
            elif hyp[j]==1 and x[i+1][j]==0:
                hyp[j] = 0
            elif hyp[j]==-1 and x[i+1][j]==0:
                continue
            elif hyp[j]==-1 and x[i+1][j]==1:
                hyp[j] = 0
count = np.count_nonzero(hyp)      
print(count, end=',')
flag = 0
for i in range(hyp.shape[0]):
    if flag != count-1:
        if hyp[i]==1:
            print(i+1, end=',')
            flag = flag+1
        elif hyp[i]==-1:
            print(-i-1,end=',')
            flag = flag+1
    else:
        if hyp[i]==1:
            print(i+1)
        elif hyp[i]==-1:
             print(-i-1)