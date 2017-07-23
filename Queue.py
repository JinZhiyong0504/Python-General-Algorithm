# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 12:15:59 2017

@author: JIN
"""

class Queue(object):
    
    def __init__(self):
        self.items = list([])
    
    def isEmpty(self):
        return len(self.items)==0
    
    def append(self, item):
        self.items.append(item)
        
    def insert(self,index,item):
        self.items.insert(index-1,item)
        
    def pop(self):
        return self.items.pop(0) 
    
    def size(self):
        return len(self.items)
    
    def print(self):
        return print(self.items)
    


q = Queue()
q.append("s")
q.append("p")
q.append("s1")
q.append("t")
q.insert(2,"s2")
print(q.items)