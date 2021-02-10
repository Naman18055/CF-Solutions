import sys
input = sys.stdin.readline

def solve(n):
	print ("YES")
	ans = []
	for i in range(0, n-1, 2):
		ans.append([i+1, i+2, i+3])
	for i in range(n-2, -1, -2):
		ans.append([n, i+1, i])
	print (len(ans))
	for i in ans:
		print (*i)



n = int(input())
a = list(map(int,input().split()))

if n%2:
	solve(n)
else:
	x = a[0]
	for i in range(1, n):
		x = x^a[i]
	if x!=0:
		print ("NO")
	else:
		solve(n-1)