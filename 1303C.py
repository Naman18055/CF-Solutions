def cycledetected(root):
	stack=[root]
	vis=[0]*26
	while len(stack)!=0:
		element = stack.pop()
		vis[element] = 1
		flag=0
		for i in graph[element]:
			if vis[i]==1 and flag:
				return True
			elif vis[i]==1 and not flag:
				flag=1
			else:
				stack.append(i)
	return False

for nt in range(int(input())):
	s=input()
	n=len(s)
	if n==1:
		print ("YES")
		print ("abcdefghijklmnopqrstuvwxyz")
		continue
	if n==2:
		print ("YES")
		ans=s
		for i in range(97,123):
			if chr(i) not in ans:
				ans+=chr(i)
		print (ans)
		continue
	graph=[[] for i in range(26)]
	curr=ord(s[0])-97
	ans='YES'
	for i in range(1,n):
		if ord(s[i])-97 in graph[curr]:
			curr=ord(s[i])-97
		elif ord(s[i])-97 not in graph[curr]:
			if len(graph[curr])>=2:
				ans="NO"
				break
			else:
				graph[curr].append(ord(s[i])-97)
				graph[ord(s[i])-97].append(curr)
				curr=ord(s[i])-97
	if ans=="NO":
		print (ans)
		continue
	root=-1
	for i in range(26):
		if len(graph[i])==1:
			root=i
			break
	if root==-1:
		root=ord(s[0])-97
	if cycledetected(root):
		print ("NO")
		continue
	print ("YES")
	stack=[root]
	ans=chr(root+97)
	vis=[0]*26
	# print (ans)
	while len(stack)!=0:
		element = stack.pop()
		vis[element] = 1
		for i in graph[element]:
			if vis[i]==0:
				stack.append(i)
				ans+=(chr(i+97))
		# print (ans)
	for i in range(97,123):
		if chr(i) not in ans:
			ans+=chr(i)
	print (ans)



