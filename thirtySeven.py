import math
def isprime(t):
    if t == 1:
        return False
    if t == 2:
        return True
    if t % 2 == 0:
        return False
    i = 3
    while i <= math.sqrt(t):
        if t % i == 0:
            return False
        i += 2
    return True
def istruncatable(t):
    for i in range((len(str(t))-1)):
        if not isprime(int(str(t)[:i+1])):
            return False
        if not isprime(int(str(t)[i+1:])):
            return False
    return True
sum = 0
a = 0
i = 10
while a < 11:
    if isprime(i):
        if istruncatable(i):
            a += 1
            sum += i
    i += 1
print (sum)