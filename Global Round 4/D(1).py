prime = [-1]*(2001)
for i in range(2,2001):
	if prime[i]==-1:
		for j in range(i,2001,i):
			prime[j] = i
n = int(input())
e = []
for i in range(n):
	e.append((i,(i+1)%n))
if prime[n]==n:
	print (len(e))
	for i in e:
		print (i[0]+1,i[1]+1)
else:
	i = 1
	j = n-1
	while prime[n]!=n:
		e.append((i,j))
		i += 1
		j -= 1
		n += 1
	print (len(e))
	for i in e:
		print (i[0]+1,i[1]+1)
