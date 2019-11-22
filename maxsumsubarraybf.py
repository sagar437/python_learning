def max_sum(arr,k):
	result = []
	for i in range(len(arr) - k):
		sum = 0
		for j in range(i,i+k):
			sum += arr[j]
		result.append(sum/k)
	return result
def main():
  result = max_sum([1, 3, 2, 6, -1, 4, 1, 8, 2], 5)
  print("Averages of subarrays of size K: " + str(result))


main()
