n,k = map(int,input().split())
a = list(map(int,input().split()))
a.sort()
ans = 0
prev = 0
for i in range(n-1):
	ans += max((a[i]-prev*k-1)//k + 1,0)
	prev = max((a[i]-prev*k-1)//k + 1,0)
	# print (ans,prev)
ans += max((a[-1]-prev*k-1)//(2*k) + 1,0)
print (ans)