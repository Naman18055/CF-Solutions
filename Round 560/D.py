import math
def SieveOfEratosthenes(n, prime,primesquare, a): 
	for i in range(2,n+1): 
		prime[i] = True
	for i in range((n * n + 1)+1): 
		primesquare[i] = False
	prime[1] = False
	p = 2
	while(p * p <= n): 
		if (prime[p] == True): 
			i = p * 2 
			while(i <= n): 
				prime[i] = False
				i += p 
		p+=1
	j = 0
	for p in range(2,n+1):  
		if (prime[p]==True):  
			a[j] = p 
			primesquare[p * p] = True
			j+=1
def countDivisors(n): 
	if (n == 1): 
		return 1
	prime = [False]*(n + 2) 
	primesquare = [False]*(n * n + 2) 
	a = [0]*n 
	SieveOfEratosthenes(n, prime, primesquare, a) 
	ans = 1
	i=0
	while(1):  
		if(a[i] * a[i] * a[i] > n): 
			break 
		cnt = 1
		while (n % a[i] == 0): # if a[i] is a factor of n 
			n = n / a[i] 
			cnt = cnt + 1 # incrementing power 
		ans = ans * cnt 
		i+=1
	n=int(n) 
	if (prime[n]==True): 
		ans = ans * 2
	elif (primesquare[n]==True): 
		ans = ans * 3
	elif (n != 1): 
		ans = ans * 4
	return ans

t=int(input())
for nt in range(t):
	n=int(input())
	l=list(map(int,input().split()))
	l.sort()
	if n>2:
		lcm=l[0]*l[-1]
		if n==(countDivisors(lcm)-2):
			print (lcm)
		else:
			print (-1)
	else:
		if n==1:
			if (countDivisors(l[0]**2)-2)==1:
				print (l[0]*l[0])
			else:
				print (-1)
		if n==2:
			if (countDivisors(l[0]*l[1])-2)==2:
				print (l[0]*l[1])
			else:
				print (-1)
		
