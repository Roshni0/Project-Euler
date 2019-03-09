from math import sqrt
product,record=41,40
def is_prime(x):
    if x<2:return 0
    if x%2:
        for i in range(3,int(sqrt(x)),2):
            if x%i==0:return 0
    else:return 0
    return 1
for a in range(-999,1000):
    for b in range(0,1000):
        c=0
        while is_prime(c*c+a*c+b)==1:c+=1
        if c>record:
            record,product=c,a*b
print (product)
