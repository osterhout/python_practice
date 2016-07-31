#!/usr/bin/python3.3

# solution for http://www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html

while True:
	try:
		io = int(raw_input("Enter a number: "))
	except ValueError:
		print (" please enter an integer")
	else:
		break

if int(io) == 0:
	print ("Zero is cheating, but...") 

check = io % 2
frs = io % 4


while check == 0:
	if frs == 0:
		print (str(io) + " is divisible by 4")
		break
	elif frs != 0:
		print (str(io) + " is an even number")
		break
if check != 0:
	print (str(io) + " is an odd number")












##io2 = int(io)
#
#
#io = True
#
#while True:
#	try: 
#		if 
#
#
#
#
#if type(io2) is not int:
#	print ("wtf")
#
#elif type(io2) is int:
#	print (io + " is an integer")






#while True:
#	try:
#		check = int(io)
#		break
#	except ValueError:
#		#print ("wtf")






#def ins():
#	global io 
#	io = raw_input("enter a number: ")
#	try:
#		io == int 
#		print ("it is an integer")
#
#
#		return mod()
#	except ValueError:
#		return ins()
#
#
#def mod():
#	rem = int(io) % 2
#	if rem =! 0:
#		print ("hi")
#	if rem == 0:
#		print ("even")
#	
#





#ins()









#		if io:
#			try:
#				input_number = int(io)
#			except ValueError:
#				print ("*** these are not the droids you're looking for ***")
#				return usin()
#			else:
#				print 
##		break
#
#
#def check():
#	if io == int:
#		print io
#	else:
#		return io()
#
#check()


