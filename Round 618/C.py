n=int(input())
l=list(map(int,input().split()))
counter={}
for i in l:
	if str(i) in counter:
		counter[str(i)]+=1
	else:
		counter[str(i)]=1
new=[]
last=[]
count=[]
for i in counter:
	if counter[i]==1:
		new.append(int(i))
	else:
		for j in range(counter[i]):
			last.append(i)
new.sort(reverse=True)
for i in new:
	print (i,end=" ")
for i in range(len(last)):
	print (last[i],end=" ")
print ()