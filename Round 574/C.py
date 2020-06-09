n=int(input())
if n>=3:
	row1=list(map(int,input().split()))
	row2=list(map(int,input().split()))
	i=0
	if row1[i]>row2[i]:
		incl=row1[0]
		flag=2
	elif row1[0]<row2[0]:
		incl=row2[0]
		flag=1
	else:
		incl=row1[0]
		flag=0
	excl=0
	for i in range(1,n):
		if flag==0:
			if row1[i]>row2[i]:
				incl=row1[0]
				flag=2
			elif row1[0]<row2[0]:
				incl=row2[0]
				flag=1
			else:
				incl=row1[0]
				flag=0
		