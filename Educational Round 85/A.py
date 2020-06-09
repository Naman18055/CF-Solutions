for nt in range(int(input())):
	n=int(input())
	l=[]
	for i in range(n):
		l.append(list(map(int,input().split())))
	flag="YES"
	if l[0][0]<l[0][1]:
		print ("NO")
		continue
	for i in range(1,n):
		if l[i][0]<l[i][1]:
			flag="NO"
			break
		if l[i][0]<l[i-1][0] or l[i][1]<l[i-1][1]:
			flag="NO"
			break
		if l[i][0]-l[i-1][0]<l[i][1]-l[i-1][1]:
			flag="NO"
			break
	print (flag)