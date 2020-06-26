n,m = map(int,input().split())
x,y = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
a.sort()
b.sort(reverse=True)
if a[x-1]<b[y-1]:
	print ("YES")
else:
	print ("NO")