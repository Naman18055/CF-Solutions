n=int(input())
l=list(map(int,input().split()))
l.sort()
count=0
for i in range(1,n+1):
	count+=(abs(l[i-1]-i))
print (count)