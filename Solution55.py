# This program implements a solution to the 55h Project Euler problem.

def isPalindromic(n):
    if str(n) == str(n)[::-1]: 
    	return True
    return False

def isLychrel(n):
    for i in range(50):
        n += int(str(n)[::-1])
        if isPalindromic(n): return False
    return True

total = 0
for i in range(10001):
    i += int(str(i)[::-1])
    if not isPalindromic(i):
        if isLychrel(i): total += 1
print total
