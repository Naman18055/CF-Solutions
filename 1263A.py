for nt in range(int(input())):
	l=list(map(int,input().split()))
	l.sort()
	if l[-1]>=l[-2]+l[-3]:
		print (l[-2]+l[-3])
	else:
		print ((l[0]+l[1]+l[2])//2)