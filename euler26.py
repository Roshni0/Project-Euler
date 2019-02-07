maxden= 0
maxvin = 0
for x in range(2,1000):
  l = []
  n = 1
  while 1:
    n = (n%x)*10
    if n>0:
      if n in l:
        vin = len(l)-l.index(n)
        if vin>maxvin:
          maxvin=vin
          maxden=x
        break
      l += [n]
    else:
      break
print (maxden)
