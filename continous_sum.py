def cont_sum(arr):
	sum = 0
	for num in arr:
		sum_new = max(int(sum) + int(num),int(num))
		max_sum = max(sum_new,max_sum)
	return max_sum

brr = input("enter a numbers").split(' ')
print(cont_sum(brr))	
