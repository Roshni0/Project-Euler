prime = [2, 3]
    
def isprime(n):
    for p in prime:
        if n < p * p:
            break
            
        if n % p == 0:
            return False			

    while n > p * p:
        p += 2
        
        if n % p == 0:
            print n, p
            return False

    return True

def enum(limit):
    n = prime[-1]
      
    while True:
        if isprime(n) and n != prime[-1]:
            prime.append(n)
    
        n += 2
        
        if n > limit:
            break
    
import time

enum(1000000)

print sum(prime)
