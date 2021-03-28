import sys
input = sys.stdin.readline

for nt in range(int(input())):
	n = int(input())
	a = list(map(int,input().split()))
	s = 0
	c = 0
	ans = "YES"
	for i in range(n):
		s += i
		c += a[i]
		if c<s:
			ans = "NO"
			break
		
	print (ans)