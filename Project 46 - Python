import math

def prime(N):
    y=int(math.sqrt(N))
    for i in range(2,y+1):
        if N%i==0:
            return False
    return True


Primes=[]
for N in range(3,6000,2):
    if prime(N)==True:
        Primes.append(N)


Odd=[2*n+1 for n in range(1,3000)]

for i in range(len(Primes)):
    y=Primes[i]
    if y in Odd:
        Odd.remove(y)   

def rang(N):                      
    for i in range(len(Primes)):
        if Primes[i]>N:
            return i-1                     

def goldbach(N):              
    e=int(math.sqrt(N))
    t=rang(N)
    for i in range(1,e+1):
        for j in range(t+1):
            O=Primes[j]+2*i**2
            if O==N:
                return True
    return False

for i in range(1,len(Odd)):        
    N=Odd[i]
    K=goldbach(N)
    if K==False:
        print(N)
        break
