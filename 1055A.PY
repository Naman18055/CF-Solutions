n,k = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
if a[0]==0 or (a[k-1]==0 and b[k-1]==0):
	print ("NO")
	exit()
if a[k-1]==1:
	print ("YES")
	exit()
ans = "NO"
for i in range(k,n):
	if a[i]==b[i]==1:
		ans = "YES"
		break
print (ans)