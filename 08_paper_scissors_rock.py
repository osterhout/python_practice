#!/usr/bin/python

import os
os.system('clear')

def start():
	opener = ("\n \nLet's play a game! \n \nPaper Scissors Rock! \n \nYou know how this goes... \n \n")
	print opener
	return ins

def ins():
	global p1
	global p2
	p1 = str(raw_input("\nPlayer 1: \nChoose either Rock (r), Paper (p), or Scissors (s): "))

	p2 = str(raw_input("\nPlayer 2: \nChoose either Rock (r), Paper (p), or Scissors (s): "))
	return
def check():
	allowed = ["p", "r", "s", "Paper", "Scissors", "Rock"]
	if p1 not in allowed.lower or p2 not in allowed.lower:
		print ("\nNo Bueno... \n\nYou must choose either Rock (r), Paper (p), or Scissors (s).  Start again please!\n")
		ins()
	comp()

def comp():
	p1_wins = "\nCongrats! Player One is the winner of this round!\n"
	p2_wins = "\nCongrats! Player Two is the winner of this round!\n"
	tie = "\nBoring, it's a tie...\n"
	if p1 == "r":
		if p2 == "r":
			print tie
		elif p2 == "s":
			print p1_wins
		elif p2 == "p":
			print p2_wins
	if p1 == "p":
		if p2 == "r":
			print p2_wins
		elif p2 == "s":
			print p1_wins
		elif p2 == "p":
			print tie
	if p1 == "s":
		if p2 == "r":
			print p2_wins
		elif p2 == "s":
			print tie
		elif p2 == "p":
			print p1_wins

def again():
	yn = str(raw_input("\nWould you like to play again? (y/n):  "))
	if yn == "y":
		os.system('clear')
		ins()
	elif yn == "n":
		exit()
	if ValueError:
		again()



start ()
ins ()
check ()
again ()
