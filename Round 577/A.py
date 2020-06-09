n,m=map(int,input().split())
l=[]
for i in range(n):
	l.append(input())
marks=list(map(int,input().split()))
ans=0
for i in range(m):
	temp=[]
	for j in range(n):
		temp.append(l[j][i])
	#print (temp)
	a=temp.count("A")
	b=temp.count("B")
	c=temp.count("C")
	d=temp.count("D")
	e=temp.count("E")
	ans+=(marks[i]*max(a,b,c,d,e))
print (ans)