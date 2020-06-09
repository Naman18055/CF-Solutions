n,k=map(int,input().split())
s=input()
l=list(input().split())
d={}
for i in l:
	d[i]=0
l=[]
new = ""
for i in s:
	if i not in d:
		if new!="":
			l.append(new)
		new=""
	else:
		new+=i
if new!="":
	l.append(new)
ans=0
for i in l:
	count = len(i)
	ans += (count*(count+1))//2
print (ans)