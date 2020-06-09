h,w=map(int,input().split())
hr=list(map(int,input().split()))
hc=list(map(int,input().split()))
count=0
flag=0
for i in range(h):
	for j in range(w):
		if j>hr[i] and i>hc[j]:
			count+=1
		if j==hr[i] and i<hc[j]:
			#print (i,j)
			flag=1
			break
		if j<hr[i] and i==hc[j]:
			#print (i,j)
			flag=1
			break
	if flag==1:
		break
if flag==1:
	print (0)
else:
	print (pow(2,count,1000000007))
