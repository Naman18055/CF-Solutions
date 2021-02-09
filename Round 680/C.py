def sieve(n):
	prime = [-1]*(n+1)
	for i in range(2,n+1):
		if prime[i]==-1:
			for j in range(i,n+1,i):
				prime[j] = i
	return prime

prime = sieve(100010)
for nt in range(int(input())):
	p,q = map(int,input().split())
	if p>q:
		if p%q!=0:
			print (p)
		else:
			primes = []
			for i in range(2,int(q**0.5)+2):
				if q%i==0:
					primes.append(i)
					if q//i!=1:
						primes.append(q//i)
			ans = 1
			if not primes:
				primes.append(q)
			# print (primes)
			for i in primes:
				k = 1
				while p%(i**k)==0:
					# print (p//(i**k))
					if (p//(i**k))%q!=0:
						ans = max(ans, p//(i**k))
						break
					k += 1
			print (ans)

	elif p==q:
		num = -1
		for i in range(2,int(p**0.5)+1):
			if p%i==0:
				num = i
				break
		if num==-1:
			print (1)
		else:
			print (p//num)
	else:
		print (p)