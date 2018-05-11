#!/usr/bin/python
name = input("enter a string: ").strip( )
number = int(len(name))
print(number)
rev = [ ]
while number > 0:

	rev.append(name[number - 1])
	number = number - 1
	
reverse_name = ''.join(rev)
#reverse_name = name[::-1]
print(reverse_name)
if name == reverse_name:
	print("palindrome")
else:
	
	print("not a palindrome")
