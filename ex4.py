#!/usr/bin/python
num = int(input("enter a number: "))
b = [ ]
for i in range(2,num):
	if (num % i == 0):
		b.append(i)
print(b)
