from collections import Counter
n=int(input())
l=list(map(int,input().split()))
d=Counter(l)
d=d.most_common()
temp=d[0][0]
j=l.index(temp)
count=0
ans=[]
for i in range(j-1,-1,-1):
	if l[i]<temp:
		count+=1
		ans.append([1,i+1,i+2])
	elif l[i]>temp:
		ans.append([2,i+1,i+2])
		count+=1
for i in range(j+1,n):
	if l[i]<temp:
		count+=1
		ans.append([1,i+1,i])
	elif l[i]>temp:
		count+=1
		ans.append([2,i+1,i])
print (count)
for i in ans:
	for j in i:
		print (j,end=" ")
	print()
