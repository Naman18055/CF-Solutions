n,m,k=map(int,input().split())
l=list(map(int,input().split()))
temp=[]
length=max(l)-min(l)+1
for i in range(n-1):
	temp.append(l[i+1]-l[i])
temp.sort(reverse=True)
s=0
for i in range(k-1):
	s=s+temp[i]-1
print (length-s)
