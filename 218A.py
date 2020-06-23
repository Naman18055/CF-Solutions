n,k=map(int,input().split())
l=list(map(int,input().split()))
n=2*n+1
count=k
i=1
while count!=0:
	if l[i]-1>l[i+1] and l[i]-1>l[i-1]:
		l[i]-=1
		count-=1
	i+=2
	if i>=n:
		i=1
print (*l)