import sys
input = sys.stdin.readline

for nt in range(int(input())):
	n = int(input())
	a = list(map(int,input().split()))
	ans1 = [1 if i%2 else a[i] for i in range(n)]
	ans2 = [a[i] if i%2 else 1 for i in range(n)]
	s = 0
	for i in range(n):
		s += 2*(abs(ans1[i]-a[i]))
	if s<=sum(a):
		print (*ans1)
	else:
		print (*ans2)