import sys
input = sys.stdin.readline

for nt in range(int(input())):
	n = int(input())
	a = list(map(int,input().split()))
	ans = []
	l = 0
	r = n-1
	turn = 1
	while l<=r:
		if turn:
			ans.append(a[l])
			l += 1
		else:
			ans.append(a[r])
			r -= 1
		turn = 1- turn
	print (*ans)