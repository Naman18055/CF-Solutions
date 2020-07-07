n,t = map(int,input().split())
a = list(map(int,input().split()))
if t==n:
	print ("YES")
	exit()
vis = [0]*n
curr = 0
for i in range(1):
	if not vis[i]:
		curr = i
		while curr!=n-1:
			vis[curr] = 1
			curr = a[curr]+curr
	# print (vis)
if vis[t-1]:
	print ("YES")
else:
	print ("NO")