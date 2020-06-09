t=int(input())
for nt in range(t):
	n,k=map(int,input().split())
	l=list(map(int,input().split()))
	if n>1 and k!=0:
		i=0
		j=k
		m=1000000000
		temp=0
		for lol in range(k+1):
			temp=temp+l[lol]
		temp2=temp//(k+1)
		if max(temp2-l[0],l[k]-temp2)<m:
			m=max(temp2-l[0],l[k]-temp2)
		while j<n-1:
			j+=1
			temp=temp+l[j]-l[i]
			temp2=temp//(k+1)
			if max(temp2-l[0],l[k]-temp2)<m:
				m=max(temp2-l[0],l[k]-temp2)
			i+=1
		print (m)
	else:
		print(l[0])