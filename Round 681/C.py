import sys
input = sys.stdin.readline

for nt in range(int(input())):
	n = int(input())
	a = list(map(int,input().split()))
	b = list(map(int,input().split()))
	new = [[a[i], b[i]] for i in range(n)]
	new.sort()
	# print (new)
	ans = min(new[-1][0], sum([new[i][1] for i in range(n)]))
	s = 0
	for i in range(n-1, -1, -1):
		s += new[i][1]
		ans = min(ans, max(new[i-1][0], s))
	print (ans)



