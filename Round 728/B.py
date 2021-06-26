import sys
input = sys.stdin.readline

for nt in range(int(input())):
	n = int(input())
	a = list(map(int,input().split()))
	ans = 0
	for i in range(n):
		for j in range((i+1) + (a[i]-((i+1)*2)%a[i]) - 1, n, a[i]):
			# print (i, j, ans)
			if (a[j]*a[i]) == (i+2+j):
				ans += 1
	print (ans)