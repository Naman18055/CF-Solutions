for nt in range(int(input())):
	n, x = map(int,input().split())
	a = list(map(int,input().split()))
	a.sort()
	if a[-1]>x:
		print ("YES")
		print (*a[::-1])
		continue
	if sum(a)==x:
		print ("NO")
		continue
	i = 0
	s = 0
	ans = []
	while i<n:
		if s+a[i]==x:
			ans.append(a[i+1])
			ans.append(a[i])
			s += (a[i]+a[i+1])
			i += 2
		else:
			ans.append(a[i])
			s += a[i]
			i += 1
	print("YES")
	print (*ans)