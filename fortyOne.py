from itertools import *
from math import *

def main():
    l=[]
    for i in range(1,10):
        l.append(str(i))
    
    maximum=0
    for i in range(10):
        perm=list(permutations(l[0:i+1]))
        for pandigital in perm:
            n=""
            for j in pandigital:
                n+=j
            n=int(n)
            if n>maximum and isPrime(n):
                maximum=n
    print(maximum)


def isPrime(n):
    for i in range(2,int(sqrt(n))+2):
        if n%i==0:
            return False
    return True
       
    
main()
