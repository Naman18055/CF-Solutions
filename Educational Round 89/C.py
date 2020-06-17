for nt in range(int(input())):
	n,m = map(int,input().split())
	mat = []
	for i in range(n):
		mat.append(list(map(int,input().split())))
	mid = []
	if (n+m)%2==0:
		mid = [(n+m-1)//2]
	ans = 0
	count = {}
	for i in range(n):
		for j in range(m):
			if i+j not in count:
				o,z = 0,0
				s = (i,j)
				while s[0]<n and s[1]>=0:
					if mat[s[0]][s[1]]==1:
						o+=1
					else:
						z+=1
					s = (s[0]+1,s[1]-1)
				s = (i-1,j+1)
				while s[0]>=0 and s[1]<m:
					if mat[s[0]][s[1]]==1:
						o+=1
					else:
						z+=1
					s = (s[0]-1,s[1]+1)
				count[(i+j)] = (z,o)
	# print (count)
	for i in count:
		if i not in mid:
			ans += min(count[i][0]+count[n+m-i-2][0],count[i][1]+count[n+m-i-2][1])
			# print (i,ans)

	print (ans//2)

