import math
n,m,k = map(int,input().split())
a = list(map(int,input().split()))
i = 1
q = math.ceil(a[0]/k)
diff = 0
ans = 1
count = 1
while i<m:
	# print (i,math.ceil((a[i]-diff)/k),q,diff,ans)
	if (a[i]-diff-1)//k+1==q:
		count += 1
	else:
		ans += 1
		diff += count
		q = math.ceil((a[i]-diff)/k)
		count = 1
	i += 1

print (ans)