num = int(input("enter as number"))
check = int(input("enter a new number"))
if num%4 == 0:
	print("multiple of 4")
elif num%check == 0:
	print("num is a multiple of check")

elif num%2 != 0:
	print("odd")

else:
	print("even")
