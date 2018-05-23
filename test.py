arr = [1,2,3,4,5]
x = int(len(arr))
sum_new = [ ]
for i in range(0,x):
	result = int(sum(arr)) - int(arr[i])
#	print(arr[i])
	print(result)
	sum_new.append(result)
print(sum_new)
print(max(sum_new))

