import sys
input = sys.stdin.readline

for nt in range(int(input())):
	n = int(input())
	a = list(map(int,input().split()))
	ans = [0]*n
	ans[-1] = a[-1]
	for i in range(n-2, -1, -1):
		if a[i]+i<n:
			ans[i] = a[i]+ans[a[i]+i]
		else:
			ans[i] = a[i]
	print (max(ans))