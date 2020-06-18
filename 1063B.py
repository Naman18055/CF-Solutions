from collections import deque
import sys
# input = sys.stdin.readline
n,m = map(int,raw_input().split())
r,c = map(int,raw_input().split())
x,y = map(int,raw_input().split())
r,c = r-1,c-1
mat = []
for i in range(n):
	mat.append(raw_input())
q = [(r,c)]
q = deque(q)
ans = 0
dist = [[n*m+1 for i in range(m)] for j in range(n)]
dist[r][c] = 0
while q:
	a,b = q.popleft()
	if a-1>=0 and (dist[a-1][b]>dist[a][b]) and mat[a-1][b]==".":
		dist[a-1][b] = dist[a][b]
		q.append((a-1,b))
	if a+1<n and (dist[a+1][b]>dist[a][b]) and mat[a+1][b]==".":
		dist[a+1][b] = dist[a][b]
		q.append((a+1,b))
	if b-1>=0 and (dist[a][b-1]>dist[a][b]) and mat[a][b-1]==".":
		dist[a][b-1] = dist[a][b]+1
		q.append((a,b-1))
	if b+1<m and (dist[a][b+1]>dist[a][b]) and mat[a][b+1]==".":
		dist[a][b+1] = dist[a][b]+1
		q.append((a,b+1))
for i in range(n):
	for j in range(m):
		if mat[i][j]==".":
			if (dist[i][j]+(j-c))//2<=y and (dist[i][j]-(j-c))//2<=x:
				ans += 1
print (ans)