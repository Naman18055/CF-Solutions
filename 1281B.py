for nt in range(int(input())):
	s,c = input().split()
	if s<c:
		print (s)
		continue
	s = list(s)
	a = sorted(s)
	if a==s or c<=("".join(map(str,a))):
		print ("---")
		continue

	i = 0
	while s[i]==a[i]:
		i += 1
	for j in range(len(s)-1,-1,-1):
		if a[i]==s[j]:
			ind = j
			break
	s[i],s[ind] = s[ind],s[i]
	s = "".join(map(str,s))
	if s>=c:
		print ("---")
	else:
		print (s)


