n=int(input())
s=input()
l=[]
for i in range(n):
	temp=(list(map(int,input().split())))
	new=[temp[1],temp[0]]
	l.append(new)
if s.count("1")==n:
	print (n)
else:
	on=[[0 for i in range(1000)] for j in range(n)]
	for i in range(n):
		if s[i]=="1":
			for j in range(1000):
				if j<l[i][0]:
					on[i][j]=1
				else:
					temp=j-l[i][0]
					if (temp//l[i][1])%2==1:
						on[i][j]=1
		else:
			for j in range(1000):
				if j<l[i][0]:
					on[i][j]=0
				else:
					temp=j-l[i][0]
					if (temp//l[i][1])%2==0:
						on[i][j]=1
	ans=0
	#print (on)
	for i in range(1000):
		count=0
		for j in range(n):
			if on[j][i]==1:
				count+=1
		if count>ans:
			#print (i)
			ans=count
	print (ans)
