import sys
input = sys.stdin.readline

for nt in range(int(input())):
	n = int(input())
	a = list(map(int,input().split()))
	indeg = [0]*n
	left = []
	ans = []
	for i in a:
		indeg[i-1] += 1
	for i in range(n):
		if not indeg[i]:
			left.append(i)

	# print (indeg)
	# print (left)
	for i in range(n):
		if indeg[a[i]-1]>1 and left and left[-1]!=i:
			ans.append(left.pop()+1)
			indeg[a[i]-1] -= 1
		else:
			ans.append(a[i])

	c = 0
	for i in range(n):
		if a[i]==ans[i]:
			c += 1
	print (c)
	print(*ans)
