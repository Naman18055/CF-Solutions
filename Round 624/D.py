for nt in range(int(input())):
	a,b,c=map(int,input().split())
	ans=10**9
	for i in range(1,10010):
		for j in range(i,10010,i):
			count=0
			if j%i==0:
				count+=(abs(a-i))
				count+=abs(b-j)
				count+=min(c%j,j-c%j)
				if count<ans:
					ans=count
					if c%j<j-c%j:
						values=[i,j,c-c%j]
					else:
						values=[i,j,c+(j-c%j)]
			#print(i,j,count)
	print (ans)
	print (*values)

	# 	count=0
	# 	count+=abs(a-i)
	# 	temp1,temp2=0,0
	# 	temp1+=b%i
	# 	temp2+=i-b%i
	# 	nb=b-b%i
	# 	if nb!=0:
	# 		temp1+=min(c%nb,nb-c%nb)
	# 		if temp1+count<ans:
	# 			ans=temp1+count
	# 			nb=b-b%i
	# 			if c%nb<nb-c%nb:
	# 				values=[i,b-b%i,c-c%nb]
	# 			else:
	# 				values=[i,b-b%i,c+(nb-c%nb)]
	# 	nb=b+temp2
	# 	if nb!=0:
	# 		temp2+=min(c%nb,nb-c%nb)
	# 		if temp2+count<ans:
	# 			ans=temp2+count
	# 			nb=b+(i-b%i)
	# 			if c%nb<nb-c%nb:
	# 				values=[i,b-b%i,c-c%nb]
	# 			else:
	# 				values=[i,b-b%i,c+(nb-c%nb)]
	# print (ans)
	# print (*values)
		