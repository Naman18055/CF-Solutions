from collections import deque

n, m1, m2 = map(int,input().split())
g1, g2 = [[] for i in range(n)], [[] for i in range(n)]
for i in range(m1):
	u, v = map(int,input().split())
	g1[u-1].append(v-1)
	g1[v-1].append(u-1)
for i in range(m2):
	u, v = map(int,input().split())
	g2[u-1].append(v-1)
	g2[v-1].append(u-1)


parent1 = {}
parent2 = {}

vis = [0]*n
for i in range(n):
	if not vis[i]:
		q = deque()
		q.append(i)
		while q:
			e = q.popleft()
			parent1[e] = i
			for j in g1[e]:
				if not vis[j]:
					vis[j] = 1
					q.append(j)

vis = [0]*n
for i in range(n):
	if not vis[i]:
		q = deque()
		q.append(i)
		while q:
			e = q.popleft()
			parent2[e] = i
			for j in g2[e]:
				if not vis[j]:
					vis[j] = 1
					q.append(j)

def find(u, parent, r):
	# print (u, parent, r)
	if parent[u]==u:
		return u, r
	return find(parent[u], parent, r+1)

# print (parent1)
# print (parent2)

ans = []
for i in range(n):
	for j in range(i+1, n):
		r1, rank1 = find(i, parent1, 1)
		r2, rank2 = find(j, parent1, 1)
		if r1!=r2:
			s1, h1 = find(i, parent2, 1)
			s2, h2 = find(j, parent2, 1)
			if s1!=s2:
				ans.append([i, j])
				if rank1<rank2:
					parent1[r1] = r2
				else:
					parent1[r2] = r1
				if h1<h2:
					parent2[s1] = s2
				else:
					parent2[s2] = s1

print (len(ans))
for i in ans:
	print (i[0]+1, i[1]+1)




