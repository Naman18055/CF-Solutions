t=int(input())
for nt in range(t):
	n=int(input())
	s=input()
	ans=[0]*n
	# stack=[int(s[-1])]
	# flag=0
	# index=[n-1]
	# stacktwo=[10]
	# for i in range(n-2,-1,-1):
	# 	# if int(s[i])>stacktwo[-1]:
	# 	# 	flag=1
	# 	# 	break
	# 	# else:
	# 	if int(s[i])>stack[-1]:
	# 		ans[i]=2
	# 		while len(stack)!=0:
	# 			stack.pop()
	# 			temp=index.pop()
	# 			if ans[temp]==2:
	# 				flag=1
	# 				break
	# 		stack.append(int(s[i]))
	# 		index.append(i)
	# 		#stacktwo.append(int(s[i]))
	# 	else:
	# 		stack.append(int(s[i]))
	# 		index.append(i)
	# for i in index:
	# 	ans[i]=1
	# if flag==1:
	# 	print ("-")
	# else:
	# 	for i in ans:
	# 		print (i,end="")
	# 	print ()


	flag=0
	one=[]
	two=[]
	for i in range(n-1):
		if int(s[i])>int(s[i+1]):
			if ans[i]==1:
				flag=1
				break
			else:
				ans[i]=2
				ans[i+1]=1
				two.append(int(s[i]))
				one.append(int(s[i+1]))
	if flag==1:
		print ("-")
	else:
		if ans.count(0)==n:
			print ("1"*n)
		else:
			#print (one,two)
			nextm1=two[0]
			prev2=one[-1]
			if (one+two)!=sorted(one+two):
				print ("-")
			else:
				nextm2=10
				next1=[-1]*n
				next2=[-1]*n
				for i in range(n-1,-1,-1):
					next1[i]=nextm1
					next2[i]=nextm2
					if ans[i]==1:
						nextm1=int(s[i])
					elif ans[i]==2:
						nextm2=int(s[i])
				prev1=0
				# print (ans)
				# print (next1,next2)
				# firsttwo=int(s[ans.index(2)])
				for i in range(n):
					if ans[i]==0:
						if int(s[i])>=prev1 and int(s[i])<=next1[i]:
							ans[i]=1
							prev1=int(s[i])
						elif int(s[i])>=prev2 and int(s[i])<=next2[i]:
							ans[i]=2
							prev2=int(s[i])
						else:
							flag=1
							break
					elif ans[i]==1:
						prev1=int(s[i])
					elif ans[i]==2:
						prev2=int(s[i])
				if flag==1:
					print ("-")
				else:
					for i in range(n):
						print (ans[i],end="")
					print ()


	# minlist=[-1]*n
	# index=[-1]*n
	# m=int(s[-1])
	# mindex=n-1
	# for i in range(n-2,-1,-1):
	# 	if int(s[i+1])<=m:
	# 		m=int(s[i+1])
	# 		mindex=i+1
	# 	minlist[i]=m
	# 	index[i]=mindex
	# print (minlist)
	# print (index)
	# flag=0
	# prev2=10
	# prev1=10
	# for i in range(n):
	# 	if int(s[i])>minlist[i]:
	# 		if (int(s[i])<prev2):
	# 			flag=1
	# 			break
	# 		else:
	# 			ans[i]=2
	# 			prev2=int(s[i])
	# 	else:
	# 		if (int(s[i])<prev1):
	# 			flag=1
	# 			break
	# 		else:
	# 			ans[i]=1
	# 			prev1=int(s[i])
	# if flag==0:
	# 	print (ans)
	# else:
	# 	print ("-")