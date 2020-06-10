import math
for nt in range(int(input())):
	n = int(input())
	g = math.gcd(n,180)
	k = n//g
	ans = 180//g
	if k+1==ans:
		print (2*ans)
	else:
		print (ans)