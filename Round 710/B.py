for nt in range(int(input())):
	n, k = map(int,input().split())
	s = input()
	prev = -1
	ans = ["."]*n
	count = 0
	for i in range(n):
		if s[i]=="*":
			if prev == -1:
				ans[i] = "x"
				count += 1
				curr = i
				prev = i
			else:
				if (i-curr)>k:
					ans[prev] = "x"
					count += 1
					curr = prev
				prev = i
	if ans[prev]!="x":
		ans[prev] = "x"
		count += 1
	print (count)