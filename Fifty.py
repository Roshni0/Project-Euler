import time
now = time.time()
def GenPrime(limit):
    a = [True] * limit
    a[0]=a[1]=False

    for counter, candidate in enumerate(a):
        if not counter % 2:
            a[counter] = False
        if candidate:
            yield counter
            for n in range(counter**2, limit, counter): 
                a[n] = False

PrimeSet = set(GenPrime(1000000))

i = 3000

while True:
    i+=1
    if sum(list(GenPrime(i))) > 1000000:
        break
    
MaxList = list(GenPrime(i-1))
MaxSum = sum(MaxList)


for i in range(0, len(MaxList)):
    if MaxSum not in PrimeSet:
        MaxSum-=MaxList[i]
    else:
        print(MaxSum)
        print(time.time()-now)
        break