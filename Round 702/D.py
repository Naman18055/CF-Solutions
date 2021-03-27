import sys
input = sys.stdin.readline

def solve(s, e, c):
	if s>e:
		return 
	if s==e:
		ans[s] = c
		return 

	m = a[s:e+1].index(max(a[s:e+1]))+s
	ans[m] = c
	solve(s, m-1, c+1)
	solve(m+1, e, c+1)


for nt in range(int(input())):
	n = int(input())
	a = list(map(int,input().split()))
	ans = [-1]*n
	solve(0, n-1, 0)
	print (*ans)