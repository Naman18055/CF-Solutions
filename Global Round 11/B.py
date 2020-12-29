for nt in range(int(input())):
	n,k = map(int,input().split())
	f = input()
	if "W" not in f:
		if k!=0:
			print (1 + 2*(k-1))
		else:
			print (0)
		continue
	if f.count("L")<=k:
		print (1 + 2*(n-1))
		continue

	s = f.split("W")
	start, end = s[0], s[-1]
	s.pop()
	s.pop(0)
	s.sort()
	ans = 0
	for i in s:
		if len(i)==0:
			continue
		if len(i)<=k:
			ans += 2*len(i)+1
			k -= len(i)
		else:
			ans += 2*k
			k = 0
	ans += k*2


	# print (s, ans)
	for i in range(n):
		if f[i]=="W":
			if i==0 or f[i-1]=="L":
				ans += 1
			else:
				ans += 2

	print (ans)





