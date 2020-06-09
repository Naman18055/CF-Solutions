n,m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
x1,x2 = a[0],b[0]
for i in range(1,n):
	x1 ^= a[i]
for i in range(1,m):
	x2 ^= b[i]
if x1!=x2:
	print ("NO")
	exit()
ans = [[0 for i in range(m)] for j in range(n)]
ans[0][0] = a[0]^x2^b[0]
for i in range(1,m):
	ans[0][i] =  b[i]
for i in range(1,n):
	ans[i][0] = a[i]
print ("YES")
for i in range(n):
	print (*ans[i])