import sys
from collections import deque
input = sys.stdin.readline

for nt in range(int(input())):
	n = int(input())
	a = list(map(int,input().split()))
	q = deque()
	q.append(a[0])
	for i in a[1:]:
		if i>q[-1]:
			q.append(i)
		elif i<q[0]:
			q.appendleft(i)
		else:
			q.append(i)
	print (*q)