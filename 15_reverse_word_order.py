#!/usr/bin/python

i = raw_input("Please type a sentence: ")
p = i.split(" ")

#print p[1]

b = []
x = 0

for i in p: #range(len(p)):
	b.append (p[x -1])
 	x = x -1

f = " ".join(b)

print f
