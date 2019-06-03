from itertools import count

target,end,p,i = 1,1,1,0

while target <= 1000000:
    for i in count(i+1):
        start = end
        end = start + len(str(i))
        if start <= target < end:
            p *= int(str(i)[target-start])
            target *= 10
            break
print (p)