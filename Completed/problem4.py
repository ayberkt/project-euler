def isPal(n):
    n = str(n)
    if n == n[::-1]: return True
    return False

max = 0
for i in range(100, 1001):
    for j in range(100, 1001):
        if isPal(i*j):
            if i*j>max:
                max = i*j
    
print max
