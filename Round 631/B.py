def check(temp):
	vis=[-1]*temp
	# print (temp)
	for i in range(temp):
		if l[i]-1 <len(vis) and l[i]-1>=0:
			vis[l[i]-1]=1
	vis2=[-1]*(len(l)-temp)
	for i in range(temp,len(l)):
		if l[i]-1 < len(vis2) and l[i]-1>=0:
			vis2[l[i]-1]=1
	if -1 in vis or -1 in vis2:
		return False
	return True

for nt in range(int(input())):
	n=int(input())
	l=list(map(int,input().split()))
	v=[-1]*n
	ans=[]
	s=sum(l)
	s1=l[0]
	s2=s-s1
	for i in range(1,n):
		if s1==(i*(i+1))//2 and s2==((n-i)*(n-i+1))//2:
			if check(i):
				ans.append(i)
		s1+=l[i]
		s2-=l[i]
	print (len(ans))
	for i in ans:
		print (i,n-i)
