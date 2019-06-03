total_sum = 0

for x in range(1,1001):
    total_sum += (x**x)

sum_str = str(total_sum)

print(sum_str[-10:])
