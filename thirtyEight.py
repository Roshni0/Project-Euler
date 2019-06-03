a=[]
for i in range(1,10000):
    s=""
    for j in range(1,5):
        if len(s)<9:
           s+=str(i*j)
    if len(s)==9:
        t=list(s)
        t.sort()
        if t==['1','2','3','4','5','6','7','8','9']:
           a.append(s)
a.sort()
a.reverse()
print (a[0])