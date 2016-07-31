#!/usr/bin/python

# solution for http://www.practicepython.org/exercise/2014/02/26/04-divisors.html

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

b = int(raw_input("Pick a positive integer: "))

print ([i for i in a if i < b])

	

