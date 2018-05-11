#!/usr/bin/python
num = int(input("enter a number: "))
if (num % 2 == 0):
	if (num % 4 == 0):
		print("multiple of 4")
	else:
		print("even")
else:
	print("odd")
