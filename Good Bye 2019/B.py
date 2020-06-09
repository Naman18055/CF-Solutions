for nt in range(int(input())):
	n=int(input())
	l=list(map(int,input().split()))
	if max(l)-min(l)>=n:
		print ("YES")
		print (1,n)
	else:
		flag=0
		for i in range(1,n):
			if l[i]!=l[i-1]+1 and l[i]!=l[i-1]-1 and l[i]!=l[i-1]:
				print ("YES")
				print (i,i+1)
				flag=1
				break
		if flag==0:
			print ("NO")