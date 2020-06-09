def diff(s1,s2):
	count=0
	for i in range(m):
		if s1[i]!=s2[i]:
			count+=1
	return count

for nt in range(int(input())):
	n,m = map(int,input().split())
	s = []
	for i in range(n):
		s.append(input())
	# ans = ""
	# count = []
	# for i in range(m):
	# 	a = []
	# 	for j in range(n):
	# 		a.append(s[j][i])
	# 	if len(set(a))>1:
	# 		count.append((i,len(set(a))))
	# 	if len(count)>2:
	# 		ans = -1
	# 		break
	# if ans==-1:
	# 	print (-1)
	# 	continue
	flag = 0
	ans = -1
	for i in range(m):
		for j in range(26):
			a = s[0][0:i]+chr(j+97)+s[0][i+1:]
			f = 0
			for k in s:
				if diff(a,k)>=2:
					f = 1
					break
			if not f:
				flag = 1
				break
		if flag:
			break
	if flag:
		print (a)
	else:
		ans = s[0]
		for k in s:
			if diff(k,s[0])>=2:
				ans = -1
				break
		print (ans)
