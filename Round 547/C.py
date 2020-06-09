n=int(input())
p=list(map(int,input().split()))
ans=[]
l=[0]
for i in p:
	l.append(l[-1]+i)
if True:
	x=1-(min(l))
	d={}
	d[x]=0
	temp=x
	ans.append(x)
	for i in range(n-1):
		temp=temp+p[i]
		ans.append(temp)
		d[temp]=0
	for i in range(1,n+1):
		if i not in d:
			flag=1
			print (-1)
			exit(0)
	for i in ans:
		print (i,end=" ")








# index=[]
# for i in range(n-2):
# 	if l[i]<0 and l[i+1]>0:
# 		index.append(i+1)
# if l[n-2]<0:
# 	index.append(n-1)
# if l[0]>0:
# 	index.append(0)
# # index=[n-1]
# s=0
# f1=0
# f2=0
# f=0

# flag=len(index)
# #print (index,flag)
# while flag>0:
# 	f1=0
# 	#print (index,flag)
# 	ans=[0 for i in range(n)]
# 	#print (ans)
# 	ans[index[flag-1]]=1
# 	#print (ans)
# 	#print (index)
# 	for i in range(index[flag-1],n-1):
# 		ans[i+1]=l[i]+ans[i]
# 	#print (ans)
# 	for i in range(index[flag-1],0,-1):
# 		ans[i-1]=ans[i]-l[i-1]
# 	#print (ans)
# 	for i in ans:
# 		if i<1 or i>n:
# 			f1=1
# 			break
# 	if len(set(ans))!=n:
# 		f1=1
# 	if f1!=1:
# 		for i in ans:
# 			print (i,end=" ")
# 		f=1
# 		break
# 	flag-=1
# if f==0:
# 	print (-1)

# # for i in range(n-2,-1,-1):
# # 	s+=l[i]
# # 	if s>0:
# # 		index.append(i)
