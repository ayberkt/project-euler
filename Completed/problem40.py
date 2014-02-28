i, product, constant = 2, 1, "1"
while len(constant) < 1000000:
	constant += str(i)
	i += 1
for i in range(1, 6):
	index = (10**i) - 1
	product *= int(constant[index])
print product