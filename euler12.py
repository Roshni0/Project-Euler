def num_divis(n):
    if n % 2 == 0: 
      n = n/2
    divis = 1
    count = 0
    while n % 2 == 0:
        count += 1
        n = n/2
    divis = divis * (count + 1)
    p = 3
    while n != 1:
        count = 0
        while n % p == 0:
            count += 1
            n = n/p
        divis = divis * (count + 1)
        p += 2
    return divis
 
def find_triangular_index(factor_limit):
    n = 1
    lnum, rnum = num_divis(n), num_divis(n+1)
    while lnum * rnum < 500:
        n += 1
        lnum, rnum = rnum, num_divis(n+1)
    return n
 
index = find_triangular_index(500)
triangle = (index * (index + 1)) / 2

 
print (triangle)
