def sieve(n):
	prime = [-1]*(n+1)
	for i in range(2,n+1):
		if prime[i]==-1:
			for j in range(i,n+1,i):
				prime[j] = i
	return prime


prime = sieve(100000)
for nt in range(int(input())):
	n = int(input())
	if n==1:
		print (6)
		continue
	elif n==2:
		print (15)
		continue
	a1, a2 = -1, -1
	for i in range(n+1, 100000):
		if prime[i]==i:
			if a1==-1:
				a1 = i
			elif a2==-1 and (i-a1)>=n:
				a2 = i
		if a1!=-1 and a2!=-1:
			break

	print (a1*a2)
