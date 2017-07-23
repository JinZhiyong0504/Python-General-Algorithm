# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 11:01:52 2017

@author: JIN
"""
class SortAlgorithm(object):
    Data = None
    
    def Fast_Sort():
        i=low
        j=high
        
        if i>=j:
            return List

        Key = List[i]

        while i<j:
            
            while i<j and List[j]>= Key:
                j=j-1
                
            List[i]=List[j]
            
            while i<j and List[i]<=Key:
                i=i+1
                
            List[j]=List[i]
            print(i,j)


        List[i]=Key
        
        fast_sort(List,low, i-1)
        fast_sort(List,j+1,high)
        
        
    def Heap_sort():
        

    
class Bag(object):
    data = None
    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)

    def addtwice(self, x):
        self.add(x)
        self.add(x)
    
    def popup(self):
        return(self.data.pop())
    
    def insert(self,index,x):
        return(self.data.insert(index,x))
    
    