n=int(input())
a=list(map(int,input().split()))
p=[a[0]]
for i in range(1,n):
	p.append(a[i]^p[i-1])
c=[{0:1},{}]
for i in range(n):
	if i%2:
		if p[i] in c[0]:
			c[0][p[i]]+=1
		else:
			c[0][p[i]]=1
	else:
		if p[i] in c[1]:
			c[1][p[i]]+=1
		else:
			c[1][p[i]]=1

ans=0
# print (p)
# print (c)
for i in range(2):
	for j in c[i]:
		if c[i][j]>=2:
			ans+=(c[i][j]*(c[i][j]-1))//2
print (ans)