def calc(s):
	s = s + "#" + s[::-1]
	n = len(s)
	lps = [0]*n
	j = 0
	for i in range(1,n):
		# print (s,i,j,lps)
		while j and s[j]!=s[i]:
			j = lps[j-1]
		if s[j]==s[i]:
			j += 1
			lps[i] = j
	return s[0:lps[-1]]


for nt in range(int(input())):
	s = raw_input()
	n = len(s)
	i = 0
	j = n-1
	ans = ""
	while i<j and s[i]==s[j]:
		ans += s[i]
		i += 1
		j -= 1
	if i==j or i>j:
		print (s)
		continue
	left = ""
	for k in range(i,j+1):
		left += s[k]
	# print (left)
	x = calc(left)
	y = calc(left[::-1])
	if len(x)>len(y):
		maxs = x
	else:
		maxs = y
	
	ans = ans + maxs + ans[::-1]
	print (ans)
