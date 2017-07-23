# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 16:48:38 2017

@author: JIN
"""

from collections import deque

queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")  
queue.append("Graham")

print(queue)
print(queue.popleft())
queue.insert("Eric",1)
print(queue)
