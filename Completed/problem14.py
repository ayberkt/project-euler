def countCol(n):
	count = 1
	while n > 1:
		count += 1
		if n % 2 == 0:
			n = n/2
		else:
			n = 3*n+1
	return count

peak = 0
for i in range(1, 1000001):
	currentCase = countCol(i)
	if currentCase > peak:
		peak = currentCase
		inputForPeak = i

print inputForPeak