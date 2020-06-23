n,l,r,x = map(int,input().split())
c = list(map(int,input().split()))
count = 0
for i in range(2**n):
	b = bin(i)[2:]
	b = "0"*(n-len(b))+b
	minn,maxx = 10**18,0
	s = 0
	for j in range(n):
		if b[j]=="1":
			minn = min(minn,c[j])
			maxx = max(maxx,c[j])
			s += c[j]
	if s>=l and s<=r and maxx-minn>=x:
		count += 1
print (count)