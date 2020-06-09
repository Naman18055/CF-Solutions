n,m=map(int,input().split())
l=list(map(int,input().split()))
l2=[]
s=''
for i in l:
	if i not in l2:
		l2.append(i)
	if len(l2)==n:
		print (1,end="")
		l2=[]
	else:
		print (0,end="")
