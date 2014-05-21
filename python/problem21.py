def d(n): return sum([num for num in range(1, int(n >> 1) + 1) if n % num == 0])

traversed = set()
for a in range(1, 10000):
    b = d(a)
    if d(b) == a and a != b: traversed.update({a, b})

print(sum(traversed))