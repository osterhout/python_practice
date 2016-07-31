#!/usr/bin/python

l = raw_input("Type something: ")

w = [l.lower() and l.strip(' ' or '\'' or ',' or '.' or '!' or '\"' or '?') for x in l]

if (w[::-1]) == w:
 print (l + " is a palindrome!")
else:
 print (l + " is not a palindrome...")
