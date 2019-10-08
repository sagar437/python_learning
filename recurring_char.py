def recur_char(str):
	str_new = []
	for i in range(len(str)):
		if str[i] in str_new:
			return(str[i])
			break
		else:
			str_new.append(str[i])
cha = input("enter a string")
print(recur_char(cha))
