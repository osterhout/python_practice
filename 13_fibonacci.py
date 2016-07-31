#!/usr/bin/python


ins = int(raw_input("Give me a positive integer: ")) # user input to define how many list items to generate
rg = range (ins) #[i for i in range(ins, ins+1)]

fib = [] # sequence is a list

#print range(ins)

def F():
	for i in rg:

		if i == 0:
			fib.append(1)
		elif i == 1:
			fib.append(1)
		else:
			fib.append(fib[i-1] + fib[i-2])
	print fib
F()
