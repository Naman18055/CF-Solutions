import sys
input = sys.stdin.readline

for nt in range(int(input())):
	n = int(input())
	a = list(map(int,input().split()))
	b = list(map(int,input().split()))
	la, lb = {}, {}
	for i in range(n):
		la[a[i]] = i
		lb[b[i]] = i

	minn = ans = 10**18
	for i in range(2, 2*n+1, 2):
		minn = min(minn, la[i-1])
		ans = min(ans, lb[i]+minn)

	print (ans)
