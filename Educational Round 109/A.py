import math
for nt in range(int(input())):
	n = int(input())
	if n==0 or n==100:
		print (1)
		continue
	h = math.gcd(n, 100-n)
	print (n//h + (100-n)//h)