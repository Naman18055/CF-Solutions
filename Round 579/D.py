s1=input()
s2=input()
mincount=1000000
ans=0
count=0
curr=s2[0]
j=0
temp=[]
for i in range(len(s1)):
	if s1[i]==s2[0]:
		temp.append(i)
#print (temp)
count2=0
mcount2=0
for i in temp:
	for k in range(i,len(s1)):
		count+=1
		if s1[k]==curr:
			j+=1
			if count2>mcount2:
				mcount2=count2
			count2=0
			if j==len(s2):
				mincount=count
				start=i
				end=start+count-1
				#print (start,end)
				tempans=max(start,len(s1)-end-1,mcount2)
				if tempans>ans:
					ans=tempans
				j=0
				count=0
				curr=s2[j]
				break
			else:
				curr=s2[j]
		else:
			count2+=1
print (ans)
		
