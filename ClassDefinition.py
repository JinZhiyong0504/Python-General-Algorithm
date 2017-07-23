# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 10:15:07 2017

@author: JIN
"""

class MyClass:
    """A simple example class"""
    i = 12345
    def __init__(self):
        self.data = []

    def f(self):
        return 'hello world'
    
a = MyClass()
print(a.f())

class Complex:
    r = None
    i = None
    alpha = None

    def __init__(self,realpart,imagpart,alpha):
        self.r = realpart
        self.i = imagpart
        self.alpha = alpha
        print(self.r,self.i,self.alpha)
        
    def print(self):
        print(self.r,self.i)
        
C = Complex(3,3,4)



for i in range(10,0,-1):
    print(i)
    
