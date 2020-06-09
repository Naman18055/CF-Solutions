n=int(input())
l=list(map(int,input().split()))
l.sort()
count=0
colored=[0]*n
for i in range(n):
	if colored[i]==0:
		count+=1
		for j in range(i+1,n):
			if colored[j]==0:
				if l[j]%l[i]==0:
					colored[j]=1
print (count)
