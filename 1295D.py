import math

def sieve(n):
	prime = [-1]*(n+1)
	for i in range(2,n+1):
		if prime[i]==-1:
			for j in range(i,n+1,i):
				prime[j] = i
	return prime


def totient(n):
	m = n
	primes = []
	i = 1
	while n>1 and i<int(n**0.5)+1:
		if n%i==0 and p[i]==i:
			primes.append(i)
			while n%i==0:
				n = n//i
		i += 1
	if n!=1:
		primes.append(n)
	if len(primes)==0:
		return n-1
	ans = m
	for i in primes:
		ans = ans//i
	for i in primes:
		ans = ans*(i-1)
	return ans

	
p = sieve(100000)
for nt in range(int(input())):
	a,m = map(int,input().split())
	g = math.gcd(a,m)
	m1 = m//g
	print (totient(m1))