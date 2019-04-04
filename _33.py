from math import floor
from math import sqrt
from math import log10

def exclude(n,d):
	r = [] # The list to return
	n = int(n); n = str(n); n = list(n) # Turn argument 'n' into a list
	d = int(d); d = str(d); d = list(d) # Turn argument 'd' into a list
	n.sort(); d.sort() # Sort the lists, placing the digits numerically
	# There is no interest for a result where the only common digit is zero
	if int(n[0]) != 0 and int(d[0]) != 0 and int(n[1]) != 0 and int(d[1]) != 0:
		# This method is useless if there are no common digits
		if n[0] == d[0] or n[1] == d[1]: 
			# If there are any common digits they will both have the same position
			if n[1] == d[1]: # Check if the biggest digit in each number is common
				n.pop(1); d.pop(1) # If so, remove it from both
			if n[0] == d[0]: # Check if the smallest digit in each number is common
				n.pop(0); d.pop(0) # If so, remove it from both
			if len(n) > 0 and len(d) > 0: # Unless we removed all the digits:
				r.append(str(n[0])) # Append the remaining digit of 'n'
				r.append(str(d[0])) # Append the remaining digiit of 'd'
				return r # Return the list
			else:
				return 0 # All digits were common in both integer, return 0
		else:	
			return 0 # No common digits
	else:
		return 0 # The only common digit was zero

def gcd(a,b):
	while b != 0:
		t = b; b = a % b; a = t
	return a

def simplest(a,b):
	a = int(a); b = int(b)
	c = int(gcd(a,b))
	a = a/c; b = b/c
	r = []; r.append(a); r.append(b)
	return r		

def fraction(n):
	l = sqrt((floor(log10(n)))**2)
	d = 10**l
	n = n*d
	r = simplest(n,d)
	return r

p = 1

for d in range(10,100):
	for n in range(10,d):
		r = exclude(n,d)
		if r != 0:
			x = float(int(n)); y = float(int(d))		
			a = float(int(r[0])); b = float(int(r[1]))
			if a > 0 and b > 0:
				k = x/y # Original
				l = a/b # Calculated
				if k == l:
					s = simplest(n,d)
					a = s[0]; b = s[1]
					a = float(int(a)); b = float(int(b))
					p = p * ( a / b )

r = fraction(p)
print (str(r[1]))