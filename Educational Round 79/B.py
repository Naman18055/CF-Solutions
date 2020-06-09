for nt in range(int(input())):
	n,s=map(int,input().split())
	l=list(map(int,input().split()))
	if sum(l)<=s:
		print (0)
	else:
		loc=0
		total=0
		ans=0
		counts=0
		for i in range(n):
			total+=l[i]
			if total>s:
				total-=l[i]
				loc=i
				counts=i
				count=i
				break
		#print (total,count)
		count=max(count-1,0)
		for i in range(n):
			if i<loc:
				total=max(total-l[i],0)
				if total<=s:
					while total<=s and loc<n:
						total+=l[loc]
						count+=1
						loc+=1
					if total>s:
						count-=1
						loc-=1
						total-=l[loc]
				if count>counts:
					counts=count
					ans=i+1
				#print (total,count)
				total+=l[i]
			else:
				count+=1
				loc+=1
				while total<=s and loc<n:
					total+=l[loc]
					count+=1
					loc+=1
				if total>s:
					count-=1
					loc-=1
					total-=l[loc]
				if count>counts:
					counts=count
					ans=i+1
				#print (total,count)
				break
		print (ans)

			
