def find_odd(lst):
	dict = {}
	for i in lst:
		if i not in dict:
			dict[i] = 1
		else:
			dict[i] += 1
	for key,val in dict.items():
		if val%2 != 0:
			return key
