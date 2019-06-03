solutions = [0] * 1001

for a in xrange(1, 1000):
    for b in xrange(1, 1000 - a):
        for c in xrange(1, 1000 - a - b):
            p = a + b + c
            if p < 1000:
                if a ** 2 + b ** 2 == c ** 2:
                    solutions[p] += 1
max = 0
maxIndex = 0
index = 0
for solution in solutions:
    if solution > max:
        max = solution
        maxIndex = index
    index += 1

print (maxIndex)