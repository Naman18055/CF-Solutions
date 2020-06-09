a=input()
b=input()
n=len(b)
count=0
temp=a[0:n]
tempcount=0
for i in range(n):
	if temp[i]==b[i]:
		tempcount+=1
	if tempcount%2==0:
		count+=1
for i in range(len(a)-n):