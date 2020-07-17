import heapq
import sys
from collections import Counter
input = sys.stdin.readline
push = heapq.heappush
pop = heapq.heappop
n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = {}
for i in range(n):
	if a[i] not in c:
		c[a[i]] = [b[i]]
	else:
		c[a[i]].append(b[i])

s = sorted(set(a))[::-1]
heap = []
heapq.heapify(heap)
ans = 0
sums = 0
while s:
	e = s.pop()
	if not heap and len(c[e])<=1:
		continue
	for i in c[e]:
		push(heap,-i)
		sums += i
	while heap and (not s or (e+1)!=s[-1]):
		x = pop(heap)
		sums += x
		ans += sums
		e += 1
	if heap:
		x = pop(heap)
		ans += (sums+x)
		sums += x
	# print (e,sums,ans)

print (ans)