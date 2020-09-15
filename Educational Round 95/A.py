for nt in range(int(input())):
	x,y,k = map(int,input().split())
	one = (y*k-1)//(x-1)+1
	count = one+k
	# print (count)
	left = (k-(one*(x-1)-y*k+1)-1)//(x-1)+1
	print (count+left)