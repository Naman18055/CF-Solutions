for nt in range(int(input())):
	n=int(input())
	l=list(map(int,input().split()))
	if n==1:
		print ("YES")
		continue
	k=l[0]%2
	flag=0
	for i in range(n):
		if l[i]%2!=k:
			print ("NO")
			flag=1
			break
	if flag==0:
		print ("YES")
