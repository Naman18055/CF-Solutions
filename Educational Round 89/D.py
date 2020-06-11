import sys
import math
input = sys.stdin.readline
n = int(input())
a = list(map(int,input().split()))
x = 5*(10**3)
s = [-1 for i in range(x+1)]
for i in range(2,x+1):
	if s[i]==-1:
		for j in range(2*i,x+1,i):
			s[j] = i
p = []
for i in range(2,len(s)):
	if s[i]==-1:
		p.append(i)
# factors = {}
# for i in p[20:]:
# 	for j in range(i,10**7+1,i):
# 		if j in factors and len(factors[j])==2:
# 			continue
# 		if j not in factors:
# 			factors[j] = [i]
# 		else:
# 			factors[j].append(i)

a1,a2 = [],[]
mem = {}
for i in range(n):
	if a[i] not in mem:
		f = []
		for j in p[:20]:
			if j>=a[i]:
				break
			if a[i]%j==0:
				f.append(j)
		if len(f)>=2:
			a1.append(f[0])
			a2.append(f[1])
		else:
			for j in p[20:]:
				if a[i]%j==0:
					f.append(j)
					break
				if a[i]%j==0:
					f.append(j)
			if len(f)>=2:
				a1.append(f[0])
				a2.append(f[1])
			elif len(f)==1:
				if a[i]//f[0]!=1 and math.gcd(f[0]+a[i]//f[0],a[i])==1:
					a1.append(f[0])
					a2.append(a[i]//f[0])
				else:
					a1.append(-1)
					a2.append(-1)
			else:
				a1.append(-1)
				a2.append(-1)
		mem[a[i]] = (a1[-1],a2[-1])
	else:
		a1.append(mem[a[i]][0])
		a2.append(mem[a[i]][1])

print (" ".join(map(str,a1)))
print (" ".join(map(str,a2)))
