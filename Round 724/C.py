import sys
import math
input = sys.stdin.readline

for nt in range(int(input())):
	n = int(input())
	s = input()
	if "D" not in s:
		print (*[i for i in range(1, n+1)])
	elif "K" not in s:
		print (*[i for i in range(1, n+1)])
	else:
		ans = [0]
		d = k = 0
		i = 0
		while d==0 or k==0:
			if s[i]=="D":
				d += 1
			else:
				k += 1
			ans.append(ans[-1]+1)
			i += 1
		ans[-1] = 1
		c = {(d, k) : 1}
		for j in range(i, n):
			if s[j]=="D":
				d += 1
			else:
				k += 1
			td, tk = d//math.gcd(d, k), k//math.gcd(d, k)
			# print (d, k, td, tk)
			if (td, tk) in c:
				ans.append(c[td, tk]+1)
				c[td, tk] += 1
			else:
				c[td, tk] = 1
				ans.append(1)
		print (*ans[1:])
