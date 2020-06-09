def calc(n):
	return n*(n+1)//2

n,m=map(int,input().split())
ans=0
mod=1000000007
for i in range(1,n+1):
	count1,count2=0,0
	for j in range(m-1):
		count1+=calc(i-j)
	for j in range(m-1):
		count2+=calc(n-i+1-j)
	print (count1,count2)
	ans+=((count1*count2)%mod)
print (ans%mod)