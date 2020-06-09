def comp(a,b):
	count=0
	for i in a:
		if i in b:
			count+=1
	if count==2:
		return 0
	elif count==1:
		return 1
	else:
		return 2

# def sum(temp):
# 	s=0
# 	for i in temp:
# 		s+=temp[i]
# 	return s
flag3=0
n,m=map(int,input().split())
l=[]
for i in range(m):
	l.append(list(map(int,input().split())))
x=-1
y=-1
x1=-1
y1=-1
ans=""
flag=0
for i in range(m-1):
	if comp(l[i],l[i+1])==2:
		print ("NO")
		exit(0)
	elif comp(l[i],l[i+1])==1:
		if l[i][0]==l[i+1][0]:
			x=l[i][0]
			x1=l[i][1]
			y1=l[i+1][1]
			break
		elif l[i][0]==l[i+1][1]:
			x=l[i][0]
			x1=l[i][1]
			y1=l[i+1][0]
			break
		elif l[i][1]==l[i+1][0]:
			x=l[i][1]
			x1=l[i][0]
			y1=l[i+1][1]
			break
		else:
			x=l[i][1]
			x1=l[i][0]
			y1=l[i+1][1]
			break
	else:
		continue
if x1!=-1:
	for i in range(m):
		if x1 not in l[i] and y1 not in l[i]:
			flag3=1
			break
	if flag3==0:
		print ("YES")
		exit(0)
if x==-1:
	print ("YES")
	exit(0)
for i in range(m-1):
	if x not in l[i]:
		if comp(l[i],l[i+1])==2:
			print ("NO")
			exit(0)
		elif comp(l[i],l[i+1])==1:
			if l[i][0] in l[i+1]:
				y=l[i][0]
				break
			else:
				y=l[i][1]
				break
		else:
			continue
if y==-1:
	print ("YES")
	exit(0)
for i in range(m):
	if x not in l[i] and y not in l[i]:
		print ("NO")
		exit(0)
print ("YES")
exit(0)
# flag=0
# x=-1
# y=-1
# temp2=[]
# if m==1:
# 	print ("YES")
# else:
# 	for i in range(m-1):
# 		if comp(l[i],l[i+1])==2:
# 			print ("NO")
# 			exit(0)
# 		elif comp(l[i],l[i+1])==1:
# 			if l[i][0] in l[i+1]:
# 				x=l[i][0]
# 				temp=i+1
# 				break
# 			else:
# 				x=l[i][1]
# 				temp=i+1
# 				break
# 		else:
# 			temp2.append(i)
# 	if x==-1:
# 		print ("YES")
# 		exit(0)
# 	for i in range(len(temp2)-1):
# 		if x not in temp2[i]:
# 			if comp(l[temp2[i]],l[temp2[i+1]])==1:
# 				if l[temp2[i]][0] in l[temp2[i+1]]:
# 					y=l[temp2[i]][0]
# 					break
# 				else:
# 					y=l[temp2[i]][1]
# 					break
# 	if y==-1:
# 		temp3=[]
# 		for i in range(temp,m-1):
# 			if x not in l[i]:
# 				if comp(l[i],l[i+1])==1:
# 					if l[i][0] in l[i+1]:
# 						y=l[i][0]
# 						break
# 					else:
# 						y=l[i][1]
# 						break
# 				elif comp(l[i],l[i+1])==2:
# 					print ("NO")
# 					exit(0)
# 				else:
# 					temp3.append(i)
# 	if y==-1:
# 		print ("YES")
# 		exit(0)

# 	for i in range(m):
# 		if x in l[i] or y in l[i]:
# 			continue
# 		else:
# 			print ("NO")
# 			exit(0)
# 	print ("YES")
# if m>1:
# 	if l[0][0] in l[1]:
# 		x=l[0][0]
# 		if l[0][1] in l[1]:
# 			y=l[0][1]
# 			flag=1
# 	elif l[0][1] in l[1]:
# 		x=l[0][1]
# 	else:
# 		print ("NO")
# 		exit(0)
# 	if x==-1:
# 		print ("NO")
# 		exit(0)
# 	temp=[]
# 	#print (x)
# 	if flag==0:	
# 		for i in range(1,m):
# 			#print (l[i])
# 			if x not in l[i]:
# 				temp.append(i)
# 			if len(temp)==2:
# 				#print ("why")
# 				break
# 	#print (temp)
# 	y2=-1
# 	if len(temp)==2:
# 		if l[temp[0]][0] in l[temp[1]]:
# 			y=l[temp[0]][0]
# 			if l[temp[0]][1] in l[temp[1]]:
# 				y2=l[temp[0]][1]
# 		elif l[temp[0]][1] in l[temp[1]]:
# 			y=l[temp[0]][1]
# 		else:
# 			print ("NO")
# 			exit(0)
# 		if y2==-1:
# 			for i in range(temp[1],m):
# 				if x in l[i] or y in l[i]:
# 					continue
# 				else:
# 					print ("NO")
# 					exit(0)
# 			print ("YES")
# 		else:
# 			flag2=0
# 			for i in range(temp[1],m):
# 				if x in l[i]:
# 					continue
# 				elif y in l[i] and y2 not in l[i]:
# 					num=y
# 					temp2=i
# 					flag2=1
# 					break
# 				elif y2 in l[i] and y not in l[i]:
# 					num=y2
# 					temp2=i
# 					flag2=1
# 					break
# 				elif y in l[i] and y2 in l[i]:
# 					continue
# 				else:
# 					print ("NO")
# 					exit(0)
# 			if flag2==1:
# 				for i in range(temp2,m):
# 					if x in l[i] or num in l[i]:
# 						continue
# 					else:
# 						print ("NO")
# 						exit(0)
# 			print ("YES")
# 	else:
# 		print ("YES")
# else:
# 	print ("YES")

