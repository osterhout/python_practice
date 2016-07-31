#!/usr/bin/python

n = int(raw_input("Enter a positive integer: "))

d = [i for i in range(1,n+1)]

divs = []

for i in d:
	if n % i == 0:
		divs.append(i)	


print ("The number " + str(n) + " has the following divisors: " + str(divs)) 
