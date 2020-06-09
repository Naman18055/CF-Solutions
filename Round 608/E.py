# n,k=map(int,input().split())
# paths=[]
# for i in range(1,n+1):
# 	j=i
# 	path=[j]
# 	while j!=1:
# 		if j%2==0:
# 			j=j//2
# 		else:
# 			j=j-1
# 		path.append(j)
# 	paths.append(path)
# counts=[]
# for i in range(1,n+1):
# 	count=0
# 	for j in paths:
# 		if i in j:
# 			count+=1
# 	counts.append(count)
# anscount={}
# for i in range(n,0,-1):
# 	for j in range(len(counts)-1,-1,-1):
# 		if counts[j]>=i:
# 			if j+1 not in anscount:
# 				anscount[j+1]=i
# 			else:
# 				anscount[j+1]=max(i,anscount[j+1])
# 			print (n,i,j+1)
# 			break
# ans=[]
# for i in anscount:
# 	ans.append([i,anscount[i]])
# ans.sort()
# for i in ans:
# 	print (i[0],i[1])
n,k=map(int,input().split())
if n%2==0:
	ans=[n]
	m=n
	flag=1
	while m!=2:
		if flag:
			m=m-2
			ans.append(m)
			flag=0
		else:
			m=m//2
			if m%2==1:
				m+=1
			ans.append(m)
			flag=1
	print (ans)
	count=[1]
	flag=1
	num=1
	while len(count)!=len(ans):
		if flag:
			count.append((2**(num)-1)*2)
			num+=1
			flag=0
		else:
			if (ans[len(count)-1]//2)%2==0:
				temp=-1
			else:
				temp=-2
			if n%(ans[len(count)]+1)==0:
				op=1
			else:
				op=0
			count.append(count[temp]+2**(num-1)+op)
			flag=1
	print (count)
	a=0
	p=0
	answer=0
	while a<k:
		answer=ans[p]
		a+=(count[p])
		p+=1
	print (answer)
