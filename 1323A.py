for nt in range(int(input())):
	n=int(input())
	l=list(map(int,input().split()))
	if n==1 and l[0]%2:
		print (-1)
		continue
	if l[0]%2==0:
		print (1)
		print (1)
		continue
	if l[1]%2==0:
		print (1)
		print (2)
		continue
	print (2)
	print (1,2)