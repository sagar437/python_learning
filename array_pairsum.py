def array_pairsum(arr,k):
	for i in range(len(arr)):
		for j in range(len(arr) - 1,0,-1):
			print(arr[i] + "," + arr[j])
		#	sum = int(arr[i]) + int(arr[j])
		#	if int(sum) == int(k):
		#		print(arr[i] + "," + arr[j])
		
brr = input().split(' ') 
#brr = [int(num) for num in str_arr]	
x = int(input("enter a number"))
array_pairsum(brr,x)
