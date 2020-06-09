n=int(input())
b=list(map(int,input().split()))
ans=[b[0]]
m=b[0]
for i in range(1,n):
	ans.append(m+b[i])
	m=max(m,ans[-1])
print (*ans)