#!/usr/bin/python

from random import randint

q = int(randint(1,10))
guess = []
def ins():
	userin = guess.append(int(raw_input("Guess an integer between 1 and 10: ")))
	while q not in guess:
		if guess[-1] > q:
			print("You're too high")
			ins()
		elif guess[-1] < q:
			print("You're too low")
			ins()
		elif IndexError:
			ins()
	else:
		return
ins()

print("Correct, the number was " + str(q))
print("Number of tries it took you to complete: " + str(len(guess)))

