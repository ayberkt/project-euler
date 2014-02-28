# This script will eventually implement a solution for the 433rd Project Euler problem.

def gcd(a, b):
	global count
	count += 1
	r = a%b
	if r == 0: return b
	return gcd(b, r)

def stepsGCD(a, b):
	global count
	count = 0
	gcd(a,b)
	return count

def S(n):
	total = 0
	for i in range(1, n+1):
		for j in range(1, n+1):
			total += stepsGCD(i, j)
	return total

# ... Some optimisation required!
print S(1000)