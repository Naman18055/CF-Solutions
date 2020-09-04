import sys
input = sys.stdin.readline
sys.setrecursionlimit(300000)

def rec(arr):
	m = min(arr)
	s = []
	ans = m
	for i in arr:
		x = i-m
		if x!=0:
			s.append(x)
		else:
			if s:
				ans += rec(s)
				s = []
	if s:
		ans += rec(s)
	return min(len(arr),ans)


n = int(input())
a = list(map(int,input().split()))
print (rec(a))
