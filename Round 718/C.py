def fill(d):
	count = a[d]-1
	ans[d][d] = a[d]
	curr = [d, d]
	while count>0:
		while count>0 and curr[1]>0 and ans[curr[0]][curr[1]-1]==0:
			ans[curr[0]][curr[1]-1] = a[d]
			curr[1] -= 1
			count -= 1
		if count>0 and curr[0]<n-1 and ans[curr[0]+1][curr[1]]==0:
			ans[curr[0]+1][curr[1]] = a[d]
			curr[0] += 1
			count -= 1


n = int(input())
a = list(map(int,input().split()))
ans = [[0 for i in range(n)] for j in range(n)]
for i in range(n):
	fill(i)
for i in range(n):
	print (*ans[i][0:i+1])
