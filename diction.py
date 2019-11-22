def sockMerchant(ar):
	dict = {}
	sum = 0
	for i in ar:
		if i in dict:
			dict[i] += 1
		else:
			dict[i] = 1
		if dict[i] == 2:
	#		print(dict[i])
			sum += 1
	print(sum)
arr = [1,1,1,2,2,3,3,4,5,6,7,8]
sockMerchant(arr)
