for nt in range(int(input())):
	n = int(input())
	a = list(map(int,input().split()))
	ans = ["0"]*n
	if sorted(a)==[i for i in range(1, n+1)]:
		ans[0] = "1"
	else:
		ans[0] = "0"
	count = [0]*n
	for i in a:
		count[i-1] += 1
	l = 0
	r = n-1
	curr = 1
	ind = -1
	for i in range(n):
		if count[i]:
			minn = i+1
			break
	if min(a)==1:
		ans[-1]="1"
		
	while curr<n:
		if a[l]==curr and count[curr-1]==1 and count[curr]>=1:
			l += 1
			ans[n-1-curr] = "1"
		elif a[r]==curr and count[curr-1]==1 and count[curr]>=1:
			r -= 1
			ans[n-1-curr] = "1"
		else:
			ind = curr
			break
		curr += 1

	print ("".join(ans))