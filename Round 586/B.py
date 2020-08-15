import sys
import math
input = sys.stdin.readline
n = int(input())
mat = []
for i in range(n):
	mat.append(list(map(int,input().split())))
g = mat[0][1]
for i in range(1,n):
	g = math.gcd(g,mat[0][i])
ans = [g]
for i in range(1,n):
	ans.append(mat[0][i]//g)
if n==2:
	print (*ans)
	exit()

if ans[1]*ans[2]!=mat[1][2]:
	diff = mat[1][2]//(ans[1]*ans[2])
	diff = int(diff**0.5)
	g = g//diff
	ans = [g]
	for i in range(1,n):
		ans.append(mat[0][i]//g)
	print (*ans)
else:
	print (*ans)