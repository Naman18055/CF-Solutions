import math
for nt in range(int(input())):
	a,b = map(int,input().split())
	if math.gcd(a,b)==1:
		print ("Finite")
	else:
		print ("Infinite")