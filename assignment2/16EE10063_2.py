#16EE10063
#Swagatam Haldar
#Assignment 2
#Execute as 'python 16EE10063_2.py'

from __future__ import print_function, division
import numpy as np

dataset = np.genfromtxt('data2.csv', delimiter = ',')
x = dataset[:, :-1]
y = dataset[:, -1]

def total_entropy(data):
    (m,n) = data.shape
    y = data[:,-1]
    n_ = np.count_nonzero(y)
    n__ = m-n_
    p_ = n_/m
    p__ = n__/m
    if p_==0 or p__==0:
        return 0
    else:
        return(-(p_*np.log2(p_) + p__*np.log2(p__)))

def calc_att_entropy(data, i, y):
    (m,n) = data.shape
    A = data[:,i]
    (a_01,a_00,a_11,a_10) = (0,0,0,0)
    for i in range(m):
        if A[i]==0:
            if y[i]==1:
                a_01 = a_01 + 1
            else:
                a_00 = a_00 + 1
        if A[i]==1:
            if y[i]==1:
                a_11 = a_11 + 1
            else:
                a_10 = a_10 + 1
                
    if a_01+a_00==0:
        p_01 = 0
        p_00 = 0
    else:
        p_01 = a_01/(a_01+a_00)
        p_00 = a_00/(a_01+a_00)
        
    if a_11+a_10==0:
        p_11 = 0
        p_10 = 0
    else:
        p_11 = a_11/(a_11+a_10)
        p_10 = a_10/(a_11+a_10)
    
    if p_01==0 or p_00==0:
        E0 = 0
    else:
        E0 = (p_01*np.log2(p_01) + p_00*np.log2(p_00))
    if p_11==0 or p_10==0:
        E1 = 0
    else:
        E1 = (p_11*np.log2(p_11) + p_10*np.log2(p_10))
            
    E0 = (a_01+a_00)*E0
    E1 = (a_11+a_10)*E1
    
    return(-(E0+E1)/m)

def best_splitter(data):
    (m,n) = data.shape
    x = data[:,:-1]
    y = data[:,-1]
    list_entropy = np.zeros(n-1)
    
    for i in range(n-1):
        list_entropy[i] = calc_att_entropy(data, i, y)
    return np.argmin(list_entropy)

class node:
    def __init__(self, value = None):
        self.val = value
        self.left_child = None
        self.right_child = None

bst = node()

def build_tree(data, bst):
    if total_entropy(data) == 0:
        if data[:,-1][0] == 0:
            if bst == None:
                bst = node('N')
            else:   
                bst.val = 'N'
        else:
            if bst == None:
                bst = node('Y')
            else: 
                bst.val = 'Y'       
    else:
        i = best_splitter(data)
        if bst == None:
            bst = node(i)
        else:
            bst.val = i
        bst.left_child = node()
        build_tree(data[data[:,i]==0], bst.left_child)
        bst.right_child = node()
        build_tree(data[data[:,i]>0], bst.right_child)

build_tree(dataset, bst)

testset = np.genfromtxt('test2.csv', delimiter = ',')

def give_result(sample, bst, file):
    if bst.val == 'Y':
        file.write('1 ')
        return
    if bst.val == 'N':
        file.write('0 ')
        return
    if sample[bst.val] == 0:
        give_result(sample, bst.left_child, file)
    else:
        give_result(sample, bst.right_child, file)

def test_tree(testset, bst):
    f = open('16EE10063_2.out', 'w')
    for i in range(testset.shape[0]):
        give_result(testset[i], bst, f)
    f.close()    

test_tree(testset, bst)                                                 