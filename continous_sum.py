def cont_sum(arr):
	sum = 0
	for num in arr:
		sum_new = int(sum) + int(num)
		if int(sum_new) > int(sum):
			sum = sum_new
		else:
			pass
	return sum

brr = input("enter a numbers").split(' ')
print(cont_sum(brr))	
