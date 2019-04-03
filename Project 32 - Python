import math
t = set()
for x in range(1,99):
   a = str(x)
   if (not('0' in a)):
      if (len(set(a)) == len(a)):
         for y in range(123, int(5000/math.sqrt(x))):
            z = x*y
            if (z < 9877):
               b = str(y)
               if (not('0' in b)):
                  c = str(z)
                  if (not('0' in c)):
                     if (len(a+b+c) == 9):
                        if (len(set(a+b+c)) == 9):
                           t.add(z)

print (sum(list(t)))
