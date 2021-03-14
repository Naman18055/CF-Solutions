import sys
input = sys.stdin.readline

for nt in range(int(input())):
	n = int(input())
	c = list(map(int,input().split()))
	a = list(map(int,input().split()))
	b = list(map(int,input().split()))
	a.append(c[-1]//2)
	b.append(c[-1]//2)
	maxx = 0
	curr2 = 0
	for i in range(1, n):
		curr = c[i]+1+abs(a[i]-b[i])
		if a[i]!=b[i]:
			curr = max(curr, c[i]+1+curr2-abs(a[i]-b[i]))
		maxx = max(maxx, curr)
		curr2 = curr
	print (maxx)
