# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 11:58:30 2017

@author: JIN
"""

class Stack(object):
    
    def __init__(self):
        self.items = list([])
    
    def isEmpty(self):
        return len(self.items)==0
    
    def push(self, item):
        self.items.push(item)
        
    def pop(self):
        return self.items.pop() 
    
    def size(self):
        return len(self.items)
    
    def print(self):
        return print(self.items)


list1 = ['a','f',True,False,"N"]

s1 = Stack()

for i in range(0,len(list1)):
    s1.push(list1[i])
    
    
s1.print()

for i in range(0,len(list1)):
    list1[i] = s1.pop()
    print(list1[i])
    
print("reverse :",list1)
