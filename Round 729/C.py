import math
mod = 10**9+7
for nt in range(int(input())):
	n = int(input())
	left = n
	num = 1
	lcm = [1]
	hcf = 1
	for i in range(2, 50):
		hcf = math.gcd(lcm[-1], i)
		lcm.append((lcm[-1]*i)//hcf)

	done = 0
	ans = 0
	i = len(lcm)-1
	while i>=0 and left!=0:
		num = lcm[i]
		c = n//num
		ans += (c - done)*(i+2)
		done = c
		ans = ans%mod
		# print (ans, c, done, num)
		i -= 1
	print (ans)

