def rever(str):
	str_new = str.split(' ')
	str_nosp=[]
#	for i in range(len(str_new)):
#		if str_new[i] != '':
#			str_nosp.append(str_new[i])
#	print(str_nosp)
	j = len(str_new) - 1
	while j >= 0:
		if str_new[j] != '':
			str_nosp.append(str_new[j])
		j = j - 1
	new_str = ' '.join(str_nosp)		
	print(new_str)
	
	

		
cha = input("input a sentence")
rever(cha)
