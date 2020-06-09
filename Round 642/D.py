from collections import deque
import heapq
for nt in range(int(input())):
	n=int(input())
	if n==1:
		print (1)
		continue
	if n==2:
		print (1,2)
		continue
	if n%2:
		ans=[1]*n
		flag=1
		k=0
		for i in range(2,n+1,2):
			ans[k]=i
			ans[k+n//2+1]=i+1
			# print (ans)
			k+=1
		print (*ans)
	else:
		ans=[-1]*n
		q2=[]
		ans[n//2-1]=1
		q2.append([-n//2,n//2])
		q2.append([-n//2+1,0])
		heapq.heapify(q2)
		flag=1
		k=2
		while len(q2)!=0:
			# print (ans,q2)
			if True:
				group = heapq.heappop(q2)
				print (group)
				group[0] = -1*group[0]
				if group[0]==1:
					ans[group[1]]=k
				elif group[0]==2:
					ans[group[1]+group[0]//2-1]=k
					q2.append([-group[0]//2,group[1]+1])
				elif group[0]%2:
					ans[group[1]+group[0]//2]=k
					heapq.heappush(q2,([-1*(group[0]//2),group[1]]))
					heapq.heappush(q2,([-1*(group[0]//2),(group[1]+group[0]//2+1)]))
				else:
					ans[group[1]+group[0]//2-1]=k
					heapq.heappush(q2,([-1*(group[0]//2),(group[1]+group[0]//2)]))
					heapq.heappush(q2,([-1*(group[0]//2-1),(group[1])]))
			k+=1
			# q2.sort(key=lambda x:(x[0],-x[1]),reverse=True)
			# q2.sort(reverse=True)
		for i in range(n):
			if ans[i]==-1:
				ans[i]=k
				k+=1
		print (*ans)
			

