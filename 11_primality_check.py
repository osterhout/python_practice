#!/usr/bin/python


n = int(raw_input("Enter a positive integer: "))

d = [i for i in range(1,n+1)]

divs = []

for i in d:
	if n % i == 0:
		divs.append(i)
			
if len(divs) < 3:
	print (str(n) + " is a prime number.")
else:
	print (str(n) + " is not a prime number.")
#if len(divs) > 2:
#	print (n + " is not a prime number.")
