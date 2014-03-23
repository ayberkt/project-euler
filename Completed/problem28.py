side_length = 1001
nums = range(1, (side_length**2)+1)

total, index = 0, 0
for i in range(2, side_length, 2):
	for j in range(4):
		total += nums[index]
		index += i

print total + nums[-1]