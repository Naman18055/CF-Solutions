import sys
input = sys.stdin.readline

n, m = map(int,input().split())
grid = []
for i in range(n):
	grid.append(list(input()))
canMove = [1]*m
for i in range(1, m):
	for j in range(1, n):
		if (grid[j-1][i]=="X" and grid[j][i-1]=="X"):
			canMove[i] = 0
canMovePrefix = [0]*m
canMovePrefix[0] = canMove[0]
for i in range(1, m):
	canMovePrefix[i] = canMovePrefix[i-1]+canMove[i]
queries = int(input())
for i in range(queries):
	a, b = map(int,input().split())
	if canMovePrefix[b-1]-canMovePrefix[a-1]!=b-a:
		print ("NO")
	else:
		print ("YES")


