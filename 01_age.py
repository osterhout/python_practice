#!/usr/bin/python3.3

import datetime

today=datetime.datetime.now()

yr = today.year
age = int(raw_input("How old are you: "))

hundy = str(today.year - age + int(100))

print ("Your 100th birthday will be in " + hundy )

lines = int(raw_input("Enter a random number: "))
while True:
	if 0 < lines < 10:
		break
#		print (lines * (str(lines) + " times. \n"))
	else:
		lines = int(raw_input ("Please choose a number between 1 and 10: "))

print (((str(lines) + " times") + "\n") * lines)

#	else:
#	print ("Choose a number between 1 and 10, please.")
