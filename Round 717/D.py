import sys
input = sys.stdin.readline
from collections import Counter
def sieve(n):
	prime = [-1]*(n+1)
	for i in range(2,n+1):
		if prime[i]==-1:
			for j in range(i,n+1,i):
				prime[j] = i
	return prime
prime = sieve(100010)
fac_loc = {}
fac = {}

n, q = map(int,input().split())
a = list(map(int,input().split()))
reach = [n]*n
for i in range(n-1, -1, -1):
	if a[i] not in fac:
		p = []
		num = a[i]
		while num!=1:
			f = prime[num]
			p.append(f)
			while num%f==0:
				num = num//f
		fac[a[i]] = p
	p = fac[a[i]]
	minn = 10**18
	for j in p:
		if j in fac_loc:
			minn = min(minn, fac_loc[j])
		fac_loc[j] = i
	if minn != 10**18:
		reach[i] = minn
	if i!=n-1:
		reach[i] = min(reach[i+1], reach[i])

dp = [[0 for i in range(20)] for j in range(n)]
for j in range(20):
	for i in range(n):
		if j==0:
			dp[i][j] = reach[i]
		else:
			if dp[i][j-1]==n:
				dp[i][j] = n
			else:
				dp[i][j] = dp[dp[i][j-1]][j-1]


for i in range(q):
	l, r = map(int,input().split())
	l -= 1
	r -= 1
	ans = 0
	if l==r:
		print (1)
		continue

	while l<r:
		for j in range(20):
			if dp[l][j]>r:
				if j!=0:
					ans += 2**(j-1)
				l = dp[l][j-1]
				break
			elif dp[l][j]==r:
				ans += 2**j
				l = r
				break
	print (ans + 1)





