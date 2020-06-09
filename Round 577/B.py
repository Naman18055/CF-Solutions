n=int(input())
l=list(map(int,input().split()))
s=sum(l)
if s%2==1:
	print ("NO")
else:
	for i in range(n-1):
		s=s-l[i]
		if l[i]>s:
			print ("NO")
			exit(0)
		s=s+l[i]
	print ("YES")