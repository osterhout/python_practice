#!/usr/bin/python

import os
os.system('clear')

def start():
	global num
	global num2
	while True:
		try:
		        num = int(raw_input("Enter a number: "))
			num2 = int(raw_input("Enter another number: "))
		except ValueError:
		        print (" please enter an integer")
		else:   
		        break

start()

if num == 0 or num2 == 0:
        print ("Zero is cheating, so let's try again...")
	start()

check = num % num2
check2 = num2 % num

while True:
	if check == 0:
		print (str(num) + " is divisible by " + str(num2))
		break
	if check2 == 0:
		print (str(num2) + " is divisible by " + str(num))
		preak
	if check != 0:
		print (str(num) + " is not divisible by " + str(num2))
		break
	if check2 != 0:
		print (str(num2) + " is not divisible by " + str(num2))
		break
