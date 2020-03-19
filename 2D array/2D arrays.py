# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 15:22:10 2020

@author: Shivam
"""

n = 1


arr = [[-1, 1, -1, 0, 0, 0], 
       [0, -1, 0, 0, 0, 0],
       [-1, -1, -1, 0, 0, 0],
       [0, -9, 2, -4, -4, 0],
       [-7, 0, 0, -2, 0, 0],
       [0, 0, -1, -2, -4, 0]]

def hour(arr):
    su = []
    f = []
    s = []
    t = []
    for i in range(4):
        for j in range(4):
            first = sum(arr[i][j:j+3])
            second = int(arr[i+1][j+1])
            third = sum(arr[i+2][j:j+3])
            c = first+second+third
            f.append(first)
            s.append(second)
            t.append(third)
            su.append(c)
    print(su)
    print(f)
    print(s)
    print(t)
    
hour(arr)

