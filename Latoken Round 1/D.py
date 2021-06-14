import sys
from collections import deque

def ask_query(ind):
	print ("?", ind+1)
	sys.stdout.flush()
	return list(map(int,input().split()))	

def chain(arr, e):
	dist = 1
	count = {}
	ind = {}
	for i in range(n):
		if arr[i] not in count:
			count[arr[i]] = 1
			ind[arr[i]] = [i]
		else:
			count[arr[i]] += 1
			ind[arr[i]].append(i)
	f = 0
	while f in count and count[f]==1:
		f += 1
	for i in range(1, f+1):
		if i not in ind:
			return 
		for j in ind[i]:
			if (j, e) not in edges:
				edges[(e, j)] = 1
		e = ind[i][0]



n = int(input())
done = {}
graph = [[] for i in range(n)]
edges = {}
qo, qe = [], []
arr = ask_query(0)
o = e = 0
for i in range(n):
	if arr[i]%2:
		o += 1
	else:
		e += 1
done = {0:1}
for i in range(1, n):
	if arr[i]==1:
		edges[(0, i)] = 1
	if arr[i]%2:
		qo.append(i)
	else:
		qe.append(i)
if e<=o:
	q = deque(qe)
else:
	q = deque(qo)



# print (edges, q)
while len(edges)!=n-1:
	e = q.popleft()
	done[e] = 1
	arr = ask_query(e)

	for i in range(n):
		if arr[i]==1 and (e, i) not in edges and (i, e) not in edges:
			edges[(e, i)] = 1
	# print (edges, q)

print ("!")
for i in edges:
	print (i[0]+1, i[1]+1)





