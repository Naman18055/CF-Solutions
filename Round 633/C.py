import sys
input = sys.stdin.readline
def calc(ans):
	m=l[0]
	for i in range(1,len(l)):
		if l[i]<m:
			if m-l[i]>(2**ans-1):
				return False
		else:
			m=l[i]
	return True

def bs(n):
	low=0
	high=50
	while (low<=high):
		mid=(low+high)//2
		if not calc(mid):
			low=mid+1
		else:
			high=mid-1
	if calc(low):
		return low
	else:
		return low-1

for nt in range(int(input())):
	n=int(input())
	l=list(map(int,input().split()))
	print (bs(n))