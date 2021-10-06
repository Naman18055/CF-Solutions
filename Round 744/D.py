import sys
import heapq
input = sys.stdin.readline

for nt in range(int(input())):
	n = int(input())
	a = list(map(int,input().split()))
	h = []
	for i in range(n):
		if a[i]!=0:
			h.append([-a[i], i])
	heapq.heapify(h)
	ans = []
	while True:
		if len(h)<=1:
			break
		a1 = heapq.heappop(h)
		a2 = heapq.heappop(h)
		a1[0] += 1
		a2[0] += 1
		ans.append([a1[1]+1, a2[1]+1])
		if a1[0]!=0:
			heapq.heappush(h, a1)
		if a2[0]!=0:
			heapq.heappush(h, a2)



	print (len(ans))
	for i in ans:
		print (*i)

	