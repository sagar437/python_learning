def equal(a, b, c):
	if a == b and b != c:
		return 2
	elif b == c and b != a:
		return 2
	elif a == b == c:
		return 3
	else:
		return 0

x = equal(1,1,1)
print(x)
