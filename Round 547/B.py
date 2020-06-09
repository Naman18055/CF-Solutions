n=int(input())
l=list(map(int,input().split()))
m=0
t=0
for i in range(n-1,-1,-1):
	if l[i]==1:
		t+=1
	else:
		if t>m:
			m=t
		t=0
if t>m:
	m=t
s=0
e=0
for i in l:
	if i==1:
		s+=1
	else:
		break
for i in range(n-1,-1,-1):
	if l[i]==1:
		e+=1
	else:
		break
if s+e>m:
	m=s+e
print (m)