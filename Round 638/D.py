import sys
input = sys.stdin.readline

def bs(num):
	low=num
	high=2*num
	while low<high:
		mid=(low+high)//2
		if mass+2*mid>n:
			high=mid-1
		else:
			low=mid+1
	if mass+2*low>n:
		return low-1
	else:
		return low

for nt in range(int(input())):
	n=int(input())
	bac=1
	mass=1
	ans=[]
	while mass!=n:
		if (n-mass)>=bac and (n-mass)<=2*bac:
			ans.append(n-mass-bac)
			break
		m=bs(bac)
		# print (m,bac,mass)
		ans.append(m-bac)
		bac=m
		mass+=m
	print (len(ans))
	print (*ans)