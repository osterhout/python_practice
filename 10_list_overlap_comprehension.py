#!/usr/bin/python

from random import randint

a = [randint(0,100) for i in range(25)] 
b = [randint(0,100) for i in range(25)] 
print list(set(i for i in a if i in b))
