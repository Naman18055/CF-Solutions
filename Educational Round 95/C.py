import sys
input = sys.stdin.readline
for nt in range(int(input())):
	n = int(input())
	a = list(map(int,input().split()))
	g = []
	count = 0
	for i in a:
		if i:
			count += 1
		else:
			if count:
				g.append(count)
				count = 0
	if count:
		g.append(count)

	if not g:
		print (0)
		continue

	ans = 0
	for i in range(1,len(g)):
		ans += g[i]//3
	if a[0]:
		ans += 1+(g[0]-1)//3
	else:
		ans += g[0]//3
		
	print (ans)

