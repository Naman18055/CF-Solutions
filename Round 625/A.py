n=int(input())
r=list(map(int,input().split()))
b=list(map(int,input().split()))
flag=0
for i in range(n):
	if r[i]!=b[i]:
		flag=1
		break
if flag==0:
	print (-1)
	exit()
diff1=0
diff2=0
for i in range(n):
	if r[i]!=b[i] and r[i]==1:
		diff1+=1
	elif r[i]!=b[i] and r[i]==0:
		diff2+=1
if diff1>diff2:
	print (1)
else:
	if diff1==0:
		print (-1)
		exit()
	print (diff2//diff1+1)
