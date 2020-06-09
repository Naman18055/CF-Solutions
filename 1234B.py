import sys
input = sys.stdin.readline
from collections import deque
n,k = map(int,input().split())
a = list(map(int,input().split()))
q = [a[0]]
q = deque(q)
d = {a[0]:1}
for i in range(1,n):
	if a[i] not in d:
		if len(q)==k:
			del d[q.popleft()]
			q.append(a[i])
			d[a[i]] = 1
		else:
			q.append(a[i])
			d[a[i]] = 1
print (len(q))
q = list(q)
print (*(q[::-1]))
