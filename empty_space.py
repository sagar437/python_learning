def check_space(str):
	sp = []
	for i in range(len(str),0):
		if str[i] == ' ':
			pass
		else:
			sp.append(str[i])
	sp.reversed()
	print(sp)
cha = input("enter a string")
check_space(cha)		
			
