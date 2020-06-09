for nt in range(int(input())):
	n,p,k=map(int,input().split())
	l=list(map(int,input().split()))
	l.sort()
	arr=[]
	prefix=[]
	last=-1
	for i in range(k):
		if i==0:
			prefix.append(l[0])
		else:
			prefix.append(prefix[-1]+l[i])
		if last==-1 and prefix[-1]>p:
			last=i
	for i in range(k-1):
		new=[i]
		for j in range(i+k,n,k):
			new.append(l[j])
		arr.append(new)
	new=[]
	for i in range(k-1,n,k):
		new.append(l[i])
	# for j in range(i+1,n):
	# 	new.append(l[j])
	arr.append(new)
	#print (arr)
	counts=[]
	for i in range(len(arr)):
		count=0
		total=0
		for j in range(len(arr[i])):
			if j==0 and i!=k-1:
				count+=prefix[arr[i][0]]
				if count>p:
					total=last
				else:
					total=arr[i][0]+1
			else:
				count+=arr[i][j]
			if count>p:
				break
			else:
				if total==0 or j!=0:
					if arr[i][0]+1+j<=i and i!=k-1:
						total+=1
					else:
						total+=k
		#print (count,total)
		counts.append(total)
	print (max(counts))