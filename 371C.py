import sys
input = sys.stdin.readline
def find(count,p1,p2,p3,n1,n2,n3,b,s,c,r):
	if (max(0,count*b-n1)*p1+max(0,count*s-n2)*p2+max(0,count*c-n3)*p3)<=r:
		return True
	return False

def calc(p1,p2,p3,n1,n2,n3,b,s,c,r):
	low=0
	high=10**18
	while low<=high:
		# print (low,high)
		mid=(low+high)//2
		if find(mid,p1,p2,p3,n1,n2,n3,b,s,c,r):
			low=mid+1
		else:
			high=mid-1
	if find(low,p1,p2,p3,n1,n2,n3,b,s,c,r):
		# if find(low+1,p1,p2,p3,n1,n2,n3,b,s,c,r):
		# 	return low+1
		return low
	else:
		return low-1

s=input()
n1,n2,n3=map(int,input().split())
p1,p2,p3=map(int,input().split())
b,s,c=s.count("B"),s.count("S"),s.count("C")
r=int(input())
# count=min(n1//b,n2//s,n3//c)
print (calc(p1,p2,p3,n1,n2,n3,b,s,c,r))