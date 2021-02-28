for nt in range(int(input())):
	a = list(map(int,input().split()))
	if sum(a)%9==0 and min(a)>=sum(a)//9:
		print ("YES")
	else:
		print ("NO")