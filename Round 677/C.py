def check(ind):
	ans = 1
	curr = a[ind]
	l,r = ind-1, ind+1
	while l>=0 or r<=n-1:
		if l>=0 and a[l]<curr:
			l -= 1
			curr += 1
		elif r<=n-1 and a[r]<curr:
			r += 1
			curr += 1
		else:
			ans = 0
			break
	return ans



for nt in range(int(input())):
	n = int(input())
	a = list(map(int,input().split()))
	if check(0):
		print (1)
	elif check(n-1):
		print (n)
	else:
		if len(a)>2:
			ans = -1
			m = max(a[1:-1])
			for i in range(1,n-1):
				if a[i]==m and (a[i+1]<m or a[i-1]<m):
					ans = i+1
					break
			print (ans)
		else:
			print (-1)