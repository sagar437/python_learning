#/usr/bin/python
import datetime
print("enter your name")
name = input( )
print("enter your age")
age = int(input( ))
now = datetime.datetime.now( )
current_year = int(now.year)
born_year = current_year - age
after_year = born_year + 100
num = int(input("enter number of time you want to display this message"))
for i in range(num):
	print( str(name) + " " + "will turn 100 on" + " " + str(after_year) )
