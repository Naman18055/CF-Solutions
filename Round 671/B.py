a = []
for i in range(1,40):
	a.append(2**i-1)
for nt in range(int(input())):
	n = int(input())
	c = 0
	i = 0 
	while c<=n:
		c += (a[i]*(a[i]+1))//2
		i += 1
	print (i-1)