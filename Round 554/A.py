n,m=map(int,input().split())
c=list(map(int,input().split()))
k=list(map(int,input().split()))
ce,co,ke,ko=0,0,0,0
for i in c:
	if i%2==0:
		ce+=1
	else:
		co+=1
for i in k:
	if i%2==0:
		ke+=1
	else:
		ko+=1
print (min(ke,co)+min(ce,ko))