# -*- coding: utf-8 -*-
"""

John works at a clothing store. He has a large pile of socks that he must pair by color for sale. Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.

Function Description

Complete the sockMerchant function in the editor below. It must return an integer representing the number of matching pairs of socks that are available.

n: the number of socks in the pile
ar: the colors of each sock


"""

n= 9

ar = [10 ,20 ,20 ,10 ,10 ,30 ,50 ,10 ,20]

def sockMerchant(n, ar):
    a={}
    for i in ar:
        if i not in a:
            a[i] = 1
        else:
            a[i] += 1
    f =[]
    for num in a.values():
       c = num//2
       f.append(c)
    print(sum(f))

sockMerchant(n,ar)
