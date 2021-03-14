for nt in range(int(input())):
	n, m = map(int,input().split())
	edge = []
	for i in range(n):
		edge.append(list(input()))
	found = 0
	for i in range(n):
		for j in range(n):
			if i==j:
				continue
			if edge[i][j] == edge[j][i]:
				found = [i, j]
	if found:
		print ("YES")
		j = 0
		for i in range(m):
			print (found[j]+1, end=" ")
			j = 1 - j
		print (found[j]+1)
		continue

	if m%2:
		print ("YES")
		for i in range(m+1):
			print (i%2+1, end=" ")
		print ()
		continue

	if n==2:
		print ("NO")
		continue
	print ("YES")

	if m==2:
		if edge[0][1]==edge[1][2]:
			ans = [1, 2, 3]
		elif edge[1][2]==edge[2][0]:
			ans = [2, 3, 1]
		elif edge[2][0]==edge[0][1]:
			ans = [3, 1, 2]
		print (*ans)
		continue

	if edge[0][1] == edge[1][2]:
		i, j, k = 1, 2, 3
	elif edge[1][2] == edge[2][0]:
		i, j, k = 2, 3, 1
	else:
		i, j, k = 3, 1, 2

	if m % 4:
		print(*[i] + [j, i] * (m // 4) + [j, k] * (m // 4 + 1))
	else:
		print(*[j, i] * (m // 4) + [j, k] * (m // 4) + [j])







