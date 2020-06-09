n=int(input())
s=0
l=list(map(int,input().split()))
l=sorted(l)
for i in range(0,len(l),2):
	s=s+(l[i+1]-l[i])
print (s)