for nt in range(int(input())):
	n = int(input())
	# n = nt+1
	if not n%2:
		print (n//2,n//2)
	else:
		ind = -1
		for i in range(2,int(n**0.5)+1):
			if n%i==0:
				ind = max(ind,i,n//i)
		if ind==-1:
			print (1,n-1)
		else:
			print (ind,n-ind)