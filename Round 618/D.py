n=int(input())
l=[]
for i in range(n):
	a=list(map(int,input().split()))
	l.append(a)
l.append(l[0])
flag=0
for i in range(n//2,0,-1):
	x=[abs(l[i][0]-l[i-1][0]),abs(l[i][1]-l[i-1][1])]
	y=[abs(l[i+n//2][0]-l[i+n//2-1][0]),abs(l[i+n//2][1]-l[i+n//2-1][1])]
	if x!=y:
		print ("NO")
		flag=1
		break
if flag==0:
	print ("YES")
