for nt in range(int(input())):
	n, m = map(int,input().split())
	a = list(map(int,input().split()))
	b = list(map(int,input().split()))
	c = list(map(int,input().split()))
	s = {}
	arr = []
	for i in range(n):
		if a[i]!=b[i]:
			arr.append([a[i], b[i], i])
		else:
			s[a[i]] = i
	loc = {}
	for i in range(len(arr)):
		if arr[i][1] not in loc:
			loc[arr[i][1]] = [arr[i][2]]
		else:
			loc[arr[i][1]].append(arr[i][2])
	if len(arr)>m:
		print ("NO")
		continue

	ans = "YES"
	v = []
	# print (loc)
	for i in range(m):
		if c[i] not in loc:
			if c[i] in s:
				v.append(s[c[i]])
				continue
			if i==m-1:
				ans = "NO"
				break
			v.append(-1)
		else:
			if not loc[c[i]]:
				v.append(s[c[i]])
				continue
			v.append(loc[c[i]][-1])
			s[c[i]] = loc[c[i]].pop()

	for i in loc:
		if loc[i]:
			ans = "NO"
			break
	if v[-1]==-1:
		ans = "NO"
	else:
		ind = v[-1]
	if ans=="NO":
		print (ans)
		continue

	for i in range(m):
		if v[i]==-1:
			v[i] = ind

	print (ans)
	for i in v:
		print (i+1, end=" ")
	print ()






