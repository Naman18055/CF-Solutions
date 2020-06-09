n=int(input())
l=input().split()
ans=0
for i in l:
	temp=""
	for j in i:
		temp+=(j+j)
	ans+=(int(temp)%998244353)
print ((ans*n)%998244353)

