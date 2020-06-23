def calc(num):
	ans=0
	for i in range(len(l)):
		ans+=(abs((l[i]-1)-(2*i+num)))
	return ans

n=int(input())
l=list(map(int,input().split()))
l.sort()
print (min(calc(0),calc(1)))