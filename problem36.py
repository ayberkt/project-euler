# Problem 36

def isPal(n):
    n = str(n)
    if n == n[::-1]: return True
    return False

def toBinary(i,n):
	return tuple((0,1)[i>>j & 1] for j in xrange(n-1,-1,-1))

def run():
	total = 0
	for i in range(1000001):
		if isPal(i):
			if isPal(int(bin(i))):
				total += i

	print total

if __name__ == "__main__":
	print toBinary(6)
