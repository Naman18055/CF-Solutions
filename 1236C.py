n = int(input())
ans = [[] for i in range(n)]
for i in range(0,n**2,2*n):
	for j in range(n):
		ans[j%n].append(i+j+1)
for i in range(n,n**2,2*n):
	for j in range(n-1,-1,-1):
		ans[j%n].append(i+(n-j))
for i in ans:
	print (*i)