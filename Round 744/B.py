import sys
input = sys.stdin.readline

for nt in range(int(input())):
	n = int(input())
	a = list(map(int,input().split()))
	b = sorted(a)
	ans = []
	for i in range(len(b)):
		ind = a[i:].index(b[i])
		for j in range(ind+i, i, -1):
			a[j] = a[j-1]
		a[i] = b[i]
		if ind+1+i!=i+1:
			ans.append([i+1, ind+1+i, ind])
	print (len(ans))
	for i in ans:
		print (*i)

