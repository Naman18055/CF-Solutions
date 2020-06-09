def check(num):
	if a<=num and c<=num:
		if num-a+num-c+num>=b:
			return True
		return False
	elif a>num and c>num:
		return False
	else:
		if a>num:
			if a<=2*num and (2*num-a+num-c)>=b:
				return True
			return False
		else:
			if c<=2*num and (2*num-c+num-a)>=b:
				return True
			return False 


for nt in range(int(input())):
	a,b,c=map(int,input().split())
	low=0
	high=10**18
	while (low<high):
		mid=(low+high)//2
		if check(mid):
			high=mid-1
		else:
			low=mid+1
		# print (low,high)
	if check(low):
		print (low)
	else:
		print (low+1)