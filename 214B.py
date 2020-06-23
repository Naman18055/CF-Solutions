n=int(input())
ans=list(map(int,input().split()))
if 0 not in ans:
	print (-1)
	exit()
ans.sort(reverse=True)
if ans.count(0)==n:
	print (0)
elif not sum(ans)%3:
	print (''.join(map(str,ans)))
else:
	flag=0
	x=sum(ans)%3
	for i in range(n-1,-1,-1):
		if ans[i]%3:
			if x==ans[i]%3:
				flag=1
				index=i
				break
	if flag:
		l=[]
		for i in range(n):
			if i!=index:
				l.append(ans[i])
		if l.count(0)==len(l):
			print (0)
		else:
			print (''.join(map(str,l)))
	else:
		index=[]
		for i in range(n-1,-1,-1):
			if ans[i]%3:
				index.append(i)
		if len(index)==1:
			print (-1)
		else:
			l=[]
			for i in range(n):
				if i==index[0] or i==index[1]:
					continue
				else:
					l.append(ans[i])
			if l.count(0)==len(l):
				print (0)
			else:
				print (''.join(map(str,l)))
