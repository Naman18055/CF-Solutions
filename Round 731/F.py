import sys
import math
input = sys.stdin.readline

def sieve(n):
	prime = [-1]*(n+1)
	for i in range(2,n+1):
		if prime[i]==-1:
			for j in range(i,n+1,i):
				if prime[j]==-1:
					prime[j] = i
	return prime

def PrimeFactors(num):
	ans = {}
	while num != 1:
		p = prime[num]
		ans[p] = 1
		while num%p==0:
			num = num//p
	return ans

def solve(ind, p):
	ans = 0
	for i in range(ind, ind+n):
		if p not in pf[i%n]:
			return ans
		else:
			if i not in done:
				done[i] = {p:0}
			else:
				done[i][p] = 0
			ans += 1
	return ans

prime = sieve(1000010)
for nt in range(int(input())):
	n = int(input())
	a = list(map(int,input().split()))
	hcf = a[0]
	for i in a:
		hcf = math.gcd(hcf, i)
	for i in range(n):
		a[i] = a[i]//hcf

	pf = []
	for i in a:
		pf.append(PrimeFactors(i))

	ans = 0
	done = {}
	for i in range(n):
		for j in pf[i]:
			if i not in done:
				done[i] = {}
			if j not in done[i]:
				ans = max(ans, solve(i, j))

	print (ans)







