import sys
input = sys.stdin.readline


for nt in range(int(input())):
	n = int(input())
	caves = []
	for i in range(n):
		caves.append(list(map(int,input().split()))[1:])
	minn = []
	for i in range(n):
		m = 0
		for j in range(len(caves[i])):
			m = max(m, caves[i][j]+1-j)
		minn.append((m, len(caves[i])))
	minn.sort()
	# print (minn)

	ans = 0
	curr = 0
	for i in minn:
		if i[0]>ans+curr:
			ans = i[0]-curr
		curr += i[1]
	print (ans)

