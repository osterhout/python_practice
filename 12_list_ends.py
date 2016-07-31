#!/usr/bin/python

a = [5, 10, 15, 20, 25]

def stend():
	start = a[0]
	end = a[-1]
	ls = [start, end]
	print ls

def list_ends(a):
    print [a[0], a[-1]]

list_ends(a)
