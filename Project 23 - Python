abundant_number = []
answer = []
n = 28123

for x in range(2, n+1):
    sum_div = 1
    for d in range((x/2),1,-1):
        if x%d == 0:
            sum_div += d
            if sum_div > x:
                abundant_number.append(x)
                break

for i in range(1, n+1):
    for an in abundant_number:
        if (i-an) in abundant_number:
            break
    else:
        answer.append(i)

s = 0
for y in answer: 
  s+=y
print (s)
