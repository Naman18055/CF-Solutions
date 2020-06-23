import sys
input = sys.stdin.readline
n,m = map(int,input().split())
a = []
for i in range(n):
	a.append(list(map(int,input().split())))
count = [[1 for i in range(m)] for j in range(n)]
for i in range(1,n):
	for j in range(m):
		if a[i][j]>=a[i-1][j]:
			count[i][j] = count[i-1][j]+1
maxx = []
for i in range(n):
	maxx.append(max(count[i]))
for i in range(int(input())):
	l,r = map(int,input().split())
	if l==r:
		print ("Yes")
		continue
	if maxx[r-1]>=r-l+1:
		print ("Yes")
	else:
		print ("No")