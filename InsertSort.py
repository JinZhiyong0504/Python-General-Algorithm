# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 17:12:40 2017

@author: JIN
"""

def insert_sort(lists):
    count = len(lists)
    for i in range(1, count):
        key = lists[i]
        j = i - 1
        while j >= 0:
            if lists[j] > key:
                lists[j + 1] = lists[j]
                lists[j] = key
            j -= 1
    return lists

a=[200,13,54,21,32,4,10]
p = insert_sort(a)
print(p)