import sys
input = sys.stdin.readline
for nt in range(int(input())):
	n = int(input())
	a = list(map(int,input().split()))
	a.sort(reverse = True)
	m = a[0]
	count = 0
	for i in range(n):
		count += 1
		m = min(m,a[i])
		if m>=count:
			ans = count
		else:
			break
	print (ans)