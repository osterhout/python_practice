#!/usr/bin/python

from random import randint

s = sorted([randint(1, 10) for i in range(10)])


print ("\nSolution using loops:\n")

print ("Starting random list:  " + str(s))

g = []


for i in s: 
	if i not in g:
		g.append(i)
	i = i + 1

g.sort()

print ("Finished simple list:  " + str(g))

print ("Solution using sets:   " + str(list(sorted(set(s)))) + "\n")



