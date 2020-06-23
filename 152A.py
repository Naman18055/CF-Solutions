n,m=map(int,input().split())
l=[]
for i in range(n):
	l.append(list(map(int,list(input()))))
success=[-1]*n
count=0
for i in range(m):
	m=-1
	best=[]
	for j in range(n):
		if l[j][i]>m:
			m=l[j][i]
			best=[]
			best.append(j)
		elif l[j][i]==m:
			best.append(j)
	for j in best:
		success[j]=1
print (success.count(1))

