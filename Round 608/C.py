import sys
input = sys.stdin.readline
n,x,y=map(int,input().split())
l=[]
for i in range(n):
	a,b=map(int,input().split())
	l.append((a,b))
c1,c2,c3,c4=0,0,0,0
l1,l2,l3,l4=(x,y+1),(x+1,y),(x,y-1),(x-1,y)
d={}
for i in range(n):
	if l[i][1]>=l1[1]:
		c1+=1
	if l[i][0]>=l2[0]:
		c2+=1
	if l[i][1]<=l3[1]:
		c3+=1
	if l[i][0]<=l4[0]:
		c4+=1
d[l1]=c1
d[l2]=c2
d[l3]=c3
d[l4]=c4
ans=(max(c1,c2,c3,c4))
print (ans)
for i in d:
	if d[i]==ans:
		print (i[0],end=" ")
		print (i[1])
		exit()
