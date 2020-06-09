n=int(input())
s=input()
ans=[0]*n
removed=[0]*n
for i in range(1,n):
	if ord(s[i])==ord(s[i-1])+1:
		ans[i]=ans[i-1]+1
		if ord(s[i])>ord(s[i-1]):
			removed[i]=1
		else:
			removed[i-1]=1
	elif ord(s[i])==ord(s[i-1])-1:
		change=0
		for j in range(i-1,-1,-1):
			if (ord(s[j])==ord(s[i])+1 and removed[j]==0):
				change+=1
				removed[j]=1
			elif removed[j]==1:
				continue
			else:
				break
		ans[i]=ans[i-1]+change
	else:
		if i>=2:
			index=0
			for j in range(i-1,-1,-1):
				if removed[j]==0:
					index=j
					break
			if abs(ord(s[index])-ord(s[i]))==1:
				ans[i]=ans[i-1]+1
				if ord(s[index])>ord(s[i]):
					removed[index]=1
				else:
					removed[i]=1
			else:
				ans[i]=ans[i-1]
		else:
			ans[i]=ans[i-1]
	#print (ans)
print (ans[-1])