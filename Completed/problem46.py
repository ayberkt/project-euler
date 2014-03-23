import math

def isPrime(n):
    if n == 2: return True
    sqrtSet = range(2, int(math.sqrt(n))+2)
    for i in sqrtSet:
        if n%i == 0:
        	return False
    return True

def squares(n):
	squares = []
	i = 1
	while (i**2)*2 < n:
		squares.append(i**2)
		i += 1
	return squares

def nextOddComp(n):
	while True:
		n += 1
		if not isPrime(n) and n % 2 != 0: 
			return n

input = 9
results = []
while True:
	for i in squares(input):
		results.append(isPrime(input - 2*i))
	if True in results:
		input = nextOddComp(input)
	else:
		print "Conjecture refuted: " + str(input)
		break
	results = []