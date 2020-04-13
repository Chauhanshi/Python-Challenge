# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 15:39:06 2020

@author: Shivam
"""

class node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
    def islistempty(self):
        if self.head is None:
            return True
        return False
        
class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self,newnode):
        if self.head is None:
            self.head = newnode
        else:
            lastnode = self.head
            while True:
                if lastnode.next is None:
                    break
                else:
                    lastnode = lastnode.next
            lastnode.next = newnode
    
    def printlist(self):
        if self.head is None:
            print("list is empty")
            return
        else:
            lastnode = self.head
            while True:
                print(lastnode.data)

                if lastnode.next is None:
                    break
                else:
                    lastnode = lastnode.next
    
    
    def inserthead(self,newheadnode):
        temp = self.head
        self.head = newheadnode
        newheadnode.next = temp
        del temp
    
    def listlength(self):
        length = 0
        currentnode = self.head
        while currentnode.next is not None:
            length += 1
            currentnode = currentnode.next
        return length
    
    def insertat(self,newnode,position):
        if position<0 or position>self.listlength():
            print("invalid position")
            return
        if position is 0:
            self.inserthead(newnode)
            return
        currentnode = self.head
        currentpos = 0
        
        while True:
            if currentpos == position:
                previousnode.next = newnode
                newnode.next = currentnode
                break
            else:
                previousnode = currentnode
                currentnode = currentnode.next
                currentpos += 1
            
    def dellast(self):
        currentnode = self.head
        while currentnode.next is not None:
            previousnode = currentnode
            currentnode = currentnode.next
        previousnode.next = None
        
    def delat(self,position):
        if position<0 or position>self.listlength():
            print("invalid position")
            return
        if position == self.listlength():
            self.dellast()
            return
        if position == 0:
            self.delhead()
            return
        cur_pos = 0
        currentnode = self.head
        while cur_pos != position:
            previousnode = currentnode
            currentnode = currentnode.next
            cur_pos += 1
        previousnode.next = currentnode.next
        currentnode.next = None
        
    def delhead(self,position):
        if position ==0:
            if self.islistempty():
                print("list is empty")
            else:
                tempnode = self.head
                self.head = tempnode.next
                tempnode.next = None
        

