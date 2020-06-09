# def calc(a,b):
# 	if b[0]<=a[1] and b[0]>=a[0]:
# 		return 0
# 	if b[0]>a[1]:
# 		return b[0]-a[1]
# 	if b[0]<a[0]:
# 		if b[1]<a[0]:
# 			return a[0]-b[1]
# 		else:
# 			return 0

def inter(a,b):
	if b[0]>a[0] and b[0]>a[1]:
		return -1
	if b[0]>=a[0] and b[1]<=a[1]:
		return (b[0],b[1])
	if b[0]>=a[0] and b[1]>a[1]:
			return (b[0],a[1])
	if b[0]<a[0] and b[1]<a[0]:
		return -1
	if b[0]<=a[0] and b[1]>=a[1]:
		return (a[0],a[1])
	if b[0]<=a[0] and b[1]<a[1]:
			return (a[0],b[1])


for nt in range(int(input())):
	n,m=map(int,input().split())
	l=[]
	for i in range(n):
		l.append(list(map(int,input().split())))
	flag=0
	if min(abs(l[0][1]-m),abs(l[0][2]-m))<=l[0][0]:
		new=inter((m-l[0][0],m+l[0][0]),(l[0][1],l[0][2]))
		if new==-1:
			print("NO")
			continue
		else:
			min_temp=new[0]
			max_temp=new[1]
	else:
		print ("NO")
		continue
	for i in range(1,n):
		diff = l[i][0]-l[i-1][0]
		#print (min_temp-diff,max_temp+diff)
		if min(abs(m-l[i][1]),abs(m+l[i][2]))<=l[0][0] and (min_temp-diff>=l[i][1] or max_temp+diff<=l[i][2]):
			new=inter((min_temp-diff,max_temp+diff),(l[i][1],l[i][2]))
			if new==-1:
				flag=1
				break
			else:
				min_temp=new[0]
				max_temp=new[1]
		else:
			flag=1
			break
		#print (min_temp,max_temp)
	if flag==1:
		print ("NO")
	else:
		print ("YES")
