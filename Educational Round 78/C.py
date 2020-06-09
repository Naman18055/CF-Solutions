for nt in range(int(input())):
	n=int(input())
	l=list(map(int,input().split()))
	two,one=0,0
	for i in l:
		if i==1:
			one+=1
		else:
			two+=1
	if one==0 or two==0:
		print (2*n)
		continue
	if one==two:
		print (0)
		continue
	ans=[]
	if True:
		diff=one-two
		d1={}
		prev1,prev2=0,0
		for i in range(n-1,-1,-1):
			if l[i]==1:
				if str(prev1+1-prev2) not in d1:
					d1[str(prev1+1-prev2)]=(n-i)
				prev1+=1
			else:
				if str(prev1-prev2-1) not in d1:
					d1[str(prev1-prev2-1)]=(n-i)
				prev2+=1
		d2={}
		prev1,prev2=0,0
		for i in range(n,2*n):
			if l[i]==1:
				if str(prev1+1-prev2) not in d2:
					d2[str(prev1+1-prev2)]=i-n+1
				prev1+=1
			else:
				if str(prev1-prev2-1) not in d2:
					d2[str(prev1-prev2-1)]=i-n+1
				prev2+=1
		#print (d1,d2)
		if str(diff) in d1:
			ans.append(d1[str(diff)])
		for i in range(n,2*n):
			if l[i]==1:
				diff-=1
			else:
				diff+=1
			if str(diff) in d1:
				ans.append(d1[str(diff)]+i-n+1)
		diff=one-two
		if str(diff) in d2:
			ans.append(d2[str(diff)])
		#print (ans)
		for i in range(n-1,-1,-1):
			if l[i]==1:
				diff-=1
			else:
				diff+=1
			if str(diff) in d2:
				ans.append(d2[str(diff)]+n-i)
		#print (ans)
		print (min(ans))
	# else:
	# 	diff=two-one
	# 	d1={}
	# 	prev1,prev2=0,0
	# 	for i in range(n-1,-1,-1):
	# 		if l[i]==1:
	# 			if str(prev2-prev1-1) not in d1:
	# 				d1[str(prev2-prev1-1)]=(n-i)
	# 			prev1+=1
	# 		else:
	# 			if str(prev2+1-prev1) not in d1:
	# 				d1[str(prev2+1-prev1)]=(n-i)
	# 			prev2+=1
	# 	d2={}
	# 	prev1,prev2=0,0
	# 	for i in range(n,2*n):
	# 		if l[i]==1:
	# 			if str(prev2-prev1-1) not in d2:
	# 				d2[str(prev2-prev1-1)]=(n-i)
	# 			prev1+=1
	# 		else:
	# 			if str(prev2+1-prev1) not in d2:
	# 				d2[str(prev2+1-prev1)]=(n-i)
	# 			prev2+=1
	# 	#print (d1,d2)
	# 	if str(diff) in d1:
	# 		ans.append(d1[str(diff)])
	# 	for i in range(n,2*n):
	# 		if l[i]==1:
	# 			diff+=1
	# 		else:
	# 			diff-=1
	# 		if str(diff) in d1:
	# 			ans.append(d1[str(diff)]+i-n+1)
	# 	if str(diff) in d2:
	# 		ans.append(d2[str(diff)])
	# 	for i in range(n-1,-1,-1):
	# 		if l[i]==1:
	# 			diff+=1
	# 		else:
	# 			diff-=1
	# 		if str(diff) in d2:
	# 			ans.append(d2[str(diff)]+n-i)
	# 	#print (ans)
	# 	print (min(ans))
