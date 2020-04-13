# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 17:14:58 2020

@author: Shivam
"""
from linked_list_basics import node,LinkedList

mergelist = LinkedList()

mergelist.printlist()

def mergetwolist(firstlist,secondlist,mergedlist):
    
    currentfirst = firstlist.head
    currentsecond = secondlist.head
    
    while True:
        if currentfirst is None:
            mergelist.insert(currentsecond)
            break
        if currentsecond is None:
            mergelist.insert(currentfirst)
            break
        
        if currentfirst.data < currentsecond.data:
            currentfirstnext = currentfirst.next
            currentfirst.next = None
            mergelist.insert(currentfirst)
            currentfirst  = currentfirstnext
        currentsecondnext = currentsecond.next
        currentsecond.next = None
        mergelist.insert(currentsecond)
        currentsecond = currentsecondnext
        
        
node1 = node(1)
node2 = node(2)
node3 = node(3)
node4 = node(4)
node5 = node(5)
node6 = node(6)
node7 = node(7)

# 1>3>5>6>7

firstlist = LinkedList()
firstlist.insert(node1)
firstlist.insert(node3)
firstlist.insert(node5)
firstlist.insert(node6)
firstlist.insert(node7)

#2>4
secondlist = LinkedList()
secondlist.insert(node2)
secondlist.insert(node4)

firstlist.printlist()
secondlist.printlist()


mergetwolist(firstlist,secondlist,mergelist)

mergelist.printlist()
