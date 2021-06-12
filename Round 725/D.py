import math
def sieve(n):
	prime = [-1]*(n+1)
	for i in range(2,n+1):
		if prime[i]==-1:
			for j in range(i,n+1,i):
				prime[j] = i
	return prime


arr = sieve(50000)
prime = []
for i in range(2, len(arr)):
	if arr[i]==i:
		prime.append(i)

for nt in range(int(input())):
	a, b, k = map(int,input().split())
	if a==b:
		m = 0
	elif math.gcd(a, b)==a or math.gcd(a, b)==b:
		m = 1
	else:
		m = 2
	n = 0
	for i in prime:
		s = 0
		while a%i == 0:
			a = a//i
			s += 1
		n += s
	if a!=1:
		n += 1

	for i in prime:
		s = 0
		while b%i==0:
			b = b//i
			s += 1
		n += s
	if b!=1:
		n += 1

	# print(m, n)
	if k>=m and k<=n:
		if k==1:
			if m==1:
				print ("YES")
			else:
				print ("NO")
		else:
			print ("YES")
	else:
		print ("NO")



