import sys
input = sys.stdin.readline

for nt in range(int(input())):
	x, y, n = map(int,input().split())
	a = list(map(int,input().split()))
	b = list(map(int,input().split()))

	ans = "YES"
	for i in range(n):
		y -= (a[i]*((b[i]-1)//x+1))
	if y + max(a)>0:
		print (ans)
	else:
		print ("NO")

