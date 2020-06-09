for nt in range(int(input())):
	n=int(input())
	l=list(map(int,input().split()))
	l.sort()
	m=10**9
	ans=[]
	i=0
	j=n-1
	while len(ans)!=n:
		if i==j:
			ans.append(l[i])
			break
		ans.append(l[i])
		ans.append(l[j])
		i+=1
		j-=1
	print (*(ans[::-1]))