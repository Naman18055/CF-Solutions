res = []
for nt in range(int(input())):
	n,t,a,b = map(int,input().split())
	diff = list(map(int,input().split()))
	time = list(map(int,input().split()))
	count = diff.count(0)
	new = [(time[i],diff[i]) for i in range(n)]
	new.sort()

	ans = 0
	curr = 0
	k = 0
	c = 0
	# print (new)
	while k<len(new) and curr<=t:
		d = new[k][0] - curr
		# print (d,c,curr,ans)
		if d>0:
			x = d//a
			if x<=count:
				if d%a==0:
					ans = max(ans,c+x-1)
				else:
					ans = max(ans,c+x)
			else:
				y = (d-count*a)//b
				if (d-count*a)%b==0:
					ans = max(ans,c+y+count-1)
				else:
					ans = max(ans,c+y+count)

		if new[k][1]:
			curr += b
		else:
			curr += a
			count -= 1
		c += 1
		k += 1

	if curr<=t:
		ans = max(ans,c)
	print (min(ans,n))
