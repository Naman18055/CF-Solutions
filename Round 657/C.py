import sys
input = sys.stdin.readline
test = int(input())
for nt in range(test):
	n,m = map(int,input().split())
	a = []
	b = []
	for i in range(m):
		x,y = map(int,input().split())
		a.append((x,i))
		b.append((y,x,i))
	a.sort(reverse=True)
	b.sort(reverse=True)
	i = 0
	ans = 0
	s = 0
	done = {}
	for j in range(m):
		while n and i<m and a[i][0]>b[j][0]:
			n -= 1
			s += a[i][0]
			done[a[i][1]] = 1
			i += 1

		if n:
			if b[j][2] not in done:
				ans = max(ans,s + b[j][1] + b[j][0]*(n-1))
			else:
				ans = max(ans,b[j][0]*(n) + s)
		else:
			ans = max(ans,s)
	print (ans)
	if nt!=test-1:
		input()
