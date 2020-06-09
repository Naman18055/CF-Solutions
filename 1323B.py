n,m,k=map(int,input().split())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
factors=[]
for i in range(1,int(k**0.5)+1):
	if k%i==0:
		factors.append((i,k//i))
		if i!=k//i:
			factors.append((k//i,i))
# print (factors)
g1,g2=[],[]
count=l1[0]
for i in range(1,n):
	if l1[i]==0 and l1[i-1]==1:
		g1.append(count)
		count=0
	elif l1[i]==1:
		count+=1
if count!=0:
	g1.append(count)
count=l2[0]
for i in range(1,m):
	if l2[i]==0 and l2[i-1]==1:
		g2.append(count)
		count=0
	elif l2[i]==1:
		count+=1
if count!=0:
	g2.append(count)
# print (g1,g2)
ans=0
for i in factors:
	count1=[]
	count2=[]
	for j in g1:
		if j>=i[0]:
			count1.append((j-i[0]+1))
	for j in g2:
		if j>=i[1]:
			count2.append((j-i[1]+1))
	for j in count1:
		for k in count2:
			ans+=j*k
print (ans)