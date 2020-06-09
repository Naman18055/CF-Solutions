n=int(input())
s=input()
count=0
prev=s[0]
groups=[1]
for i in range(1,n):
	if prev==s[i]:
		groups[-1]+=1
	else:
		prev=s[i]
		groups.append(1)
# print (groups)
for i in range(0,len(groups)-1):
	count+=(groups[i]+groups[i+1]-1)
print ((n*(n-1)//2)-count)