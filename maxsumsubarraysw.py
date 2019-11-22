def max_sum(arr,k):
	avg = 0
	result = []
	windowsum, windowstart = 0.0, 0
	for windowend in range(len(arr)):
		windowsum += arr[windowend]
		if windowend >= k-1:
			avg = windowsum/k
			result.append(avg)
			windowsum -= arr[windowstart]
			windowstart += 1
	return result
		
def main():
  result = max_sum([1, 3, 2, 6, -1, 4, 1, 8, 2], 5)
  print("Averages of subarrays of size K: " + str(result))


main()
