for nt in range(int(input())):
	n=int(input())
	if n==2 or n==3:
		print (-1)
		continue
	if n==4:
		print (3,1,4,2)
		continue
	if n%2:
		for i in range(1,n-3,2):
			print (i,end=" ")
		print (i+3,i+1,i+4,i+2,end=" ")
		for j in range(i-1,0,-2):
			print (j,end=" ")
		print ()
	else:
		for i in range(2,n-3,2):
			print (i,end=" ")
		print (i+3,i+1,i+4,i+2,end=" ")
		for j in range(i-1,0,-2):
			print (j,end=" ")
		print ()