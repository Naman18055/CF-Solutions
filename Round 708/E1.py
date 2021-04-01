def sieve(n):
	prime = [-1]*(n+1)
	for i in range(2,n+1):
		if prime[i]==-1:
			prime[i] = i
			for j in range(i*i,n+1,i):
				if prime[j]==-1:
					prime[j] = i
	p = [i for i in range(2, n+1) if prime[i]==i]
	return p

def fact(n):
	for i in prime:
		while n%(i*i)==0:
			n = n//(i*i)
	return n

prime = sieve(3500)
for nt in range(int(input())):
	n, k = map(int,input().split())
	a = list(map(int,input().split()))
	for i in range(n):
		a[i] = fact(a[i])
	ans = 0
	d = {}
	for i in range(n):
		if a[i] in d:
			ans += 1
			d = {a[i]:1}
		else:
			d[a[i]] = 1
	ans += 1
	print (ans)