n=int(input())
l=list(map(int,input().split()))
l.sort()
i,j=0,0
count=0
while i<n and j<n:
	if l[j]-l[i]<=5:
		j+=1
	else:
		i+=1
	if (j-i)>count:
		count=j-i
print (count)