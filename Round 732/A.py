import sys
input = sys.stdin.readline

for nt in range(int(input())):
	n = int(input())
	a = list(map(int,input().split()))
	b = list(map(int,input().split()))
	if sum(a)!=sum(b):
		print (-1)
		continue

	count = 0
	for i in range(n):
		if a[i]>b[i]:
			count += a[i]-b[i]

	ans = [[-1, -1] for i in range(count)]
	l = 0
	r = 0
	for i in range(n):
		if a[i]>b[i]:
			for j in range(a[i]-b[i]):
				ans[l][0] = i+1
				l += 1
		else:
			for j in range(b[i]-a[i]):
				ans[r][1] = i+1
				r += 1
	print (len(ans))
	for i in ans:
		print (*i)