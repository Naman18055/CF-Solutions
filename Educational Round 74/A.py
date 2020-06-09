t=int(input())
for nt in range(t):
	x,y=map(int,input().split())
	num=x-y
	if num==1:
		print ("NO")
	else:
		print ("YES")