n=int(input())
l=list(map(int,input().split()))
neg=0
pos=0
zero=0
for i in l:
	if i<0:
		neg+=1
	elif i>0:
		pos+=1
	else:
		zero+=1
if neg%2==0:
	count=0
	for i in l:
		if i<0:
			count+=(-1-i)
		elif i>0:
			count+=(i-1)
		else:
			count+=1
elif neg%2==1:
	count=0
	if zero>0:
		for i in l:
			if i<0:
				count+=(-1-i)
			elif i>0:
				count+=(i-1)
		count+=(zero)
	else:
		for i in l:
			if i<0:
				count+=(-1-i)
			elif i>0:
				count+=(i-1)
		count+=(2)
print (count)