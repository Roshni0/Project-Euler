from math import sqrt
from itertools import count

def isTriangle(x):
    n = (sqrt(8*x+1)-1)/2
    return n%1 == 0

def isPentagonal(x):
    n = (sqrt(6*x+0.25)+0.5)/3
    return n%1 == 0

def genHexagonal(hexagonal):
    start,total = hexagonal
    for i in count(start+1):
        total += (4*i-3)
        yield total
        
def search():
    hexagonal = (143,40755)
    for i in genHexagonal(hexagonal):
        if isPentagonal(i) and isTriangle(i):
            return i

print(search())
