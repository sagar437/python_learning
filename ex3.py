#!/usr/bin/python
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
c = int(input("enter a number: "))
b = [ ]
for num in a:
	if (num < c):
		b.append(num)
print(b)
