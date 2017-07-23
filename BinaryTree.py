# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 11:30:25 2017

@author: JIN
"""
# Binary Tree classification

class BiTree:
    def __init__(self,rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self,new_Left_Node):
        if self.leftChild == None:
            self.leftChild = BiTree(new_Left_Node)
        else:
            t = BiTree(new_Left_Node)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self,new_Right_Node):
        if self.rightChild == None:
            self.rightChild = BiTree(new_Right_Node)
        else:
            t = BinaryTree(new_Right_Node)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootValue(self,value):
        self.key = value

    def getRootValue(self):
        return self.key


r = BiTree('a')
print(r.getRootValue())
print(r.getLeftChild())
r.insertLeft('b')
print(r.getLeftChild())
print(r.getLeftChild().getRootValue())
r.insertRight('c')
print(r.getRightChild())
print(r.getRightChild().getRootValue())
r.getRightChild().setRootValue('hello')
print(r.getRightChild().getRootValue())