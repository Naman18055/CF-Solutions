n,k=map(int,input().split())
l=list(map(int,input().split()))
l2=[]
l3=[]
for i in range(k):
	j=i
	for m in range(len(l)):
		l2.append(l[m])
	while j<len(l):
		l2[j]=0
		j+=k
	l3.append(abs(l2.count(1)-l2.count(-1)))
	l2=[]
print (max(l3))