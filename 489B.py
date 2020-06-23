n=int(input())
b=list(map(int,input().split()))
m=int(input())
g=list(map(int,input().split()))
b.sort()
g.sort()
i=0
j=0
count=0
while i<n and j<m:
	if abs(b[i]-g[j])<=1:
		count+=1
		i+=1
		j+=1
	elif b[i]>g[j]:
		j+=1
	elif g[j]>b[i]:
		i+=1
print (count)