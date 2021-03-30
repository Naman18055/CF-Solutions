import sys
input = sys.stdin.readline

mod = 10**9+7
import math

def sieve(n):
	prime = [-1]*(n+1)
	for i in range(2,n+1):
		if prime[i]==-1:
			prime[i] = i
			for j in range(i*i,n+1,i):
				if prime[j]==-1:
					prime[j] = i
	return prime

def find_pf(ind, num):
	global hcf
	while num!=1:
		v = values[num]
		c = 0
		while values[num]==v:
			num = num//v
			c += 1

		prev = 0
		if v in pf[ind]:
			prev = pf[ind][v]
			pf[ind][v] += c
		else:
			pf[ind][v] = c

		for i in range(prev+1, prev+c+1):
			if v in count:
				if len(count[v])<i:
					count[v].append(1)
				else:
					count[v][i-1] += 1
			else:
				count[v] = [1]
			if count[v][i-1]==n:
				hcf = (hcf*v)%mod




values = sieve(300000)
n, q = map(int,input().split())
a = list(map(int,input().split()))
# hcf = a[0]
# for i in range(n):
# 	hcf = math.gcd(hcf, a[i])
hcf=1
pf = [{} for i in range(n)]
count = {}
for i in range(n):
	find_pf(i, a[i])
# print ("Initial", pf)
for i in range(q):
	i, x = map(int,input().split())
	find_pf(i-1, x)
	# print (pf)
	# print (count)
	print (hcf)


