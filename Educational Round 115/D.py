import sys
input = sys.stdin.readline

for nt in range(int(input())):
	n = int(input())
	a = []
	topic = {}
	difficulty = {}
	for i in range(n):
		x, y = map(int,input().split())
		a.append([x, y])
		if x in topic:
			topic[x] += 1
		else:
			topic[x] = 1
		if y in difficulty:
			difficulty[y] += 1
		else:
			difficulty[y] = 1
	res = 0
	for i in a:
		res += (topic[i[0]]-1)*(difficulty[i[1]]-1)
	print ((n*(n-1)*(n-2))//6 - res)