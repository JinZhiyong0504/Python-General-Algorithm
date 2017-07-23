# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 15:48:17 2017

@author: JIN
"""

##liked list
class Node(object):

    def __init__(self,item):
        self._item = item
        self._next = None
    
    def getItem(self):
        return self.item
    
    def getNextItem(self):
        return self._next    


class OneDirectLinkedList(object):
    def __init__(self):
        self.head = None
        
    def setItem(self,item):
        self.head.item = item
        
    def appendItem(self, item):
        
        if self.head == None:
            self.head =item
        else:
            
            loopi = self.head
            while loopi.getItem != None:
                loopi = loopi.getNextItem
            loopi._next = item
        
    def deletItem(self, item):
        loopi = self.head
        while loopi.getItem() != item.getItem():
            loopi = loopi.nextItem()
            
    def print(self):
        loopi = self.head
        
        while loopi != None:
            print(loopi.getItem)
            loopi = loopi.getNextItem
            
head = OneDirectLinkedList()
a = Node("1")
head.appendItem(a)
b = Node("2")
head.appendItem(b)
c = Node("3")
head.appendItem(c)
head.print()
        
    