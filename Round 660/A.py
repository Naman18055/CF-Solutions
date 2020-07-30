# def sieve(n):
# 	prime = [-1]*(n+1)
# 	for i in range(2,n+1):
# 		if prime[i]==-1:
# 			for j in range(i,n+1,i):
# 				prime[j] = i
# 	return prime

# primes = sieve(200010)
for nt in range(int(input())):
	n = int(input())
	if n<31:
		print ("NO")
		continue
	start = [6,10,14,15]
	print ("YES")
	if n-sum(start[0:-1]) in start:
		print (6,10,15,n-31)
	else:
		print (*start[0:-1],n-sum(start[0:-1]))

