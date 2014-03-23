from math import factorial

def nCr(n,r):
	combination = factorial(n) / (factorial(r) * factorial(n-r))
	return combination

scope = range(1, 100)
counter = 0

for i in range(1, 101):
	for j in range(1, i+1):
		if nCr(i,j) > 1000000:
			counter += 1

print counter
