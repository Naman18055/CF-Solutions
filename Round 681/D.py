for nt in range(int(input())):
	n = int(input())
	a = list(map(int,input().split()))
	if n==1:
		print ("YES")
		continue
	p, s = [a[0]], [a[-1]]
	for i in range(1, n):
		p.append(min(a[i], p[-1]))
	for i in range(n-2, -1, -1):
		s.append(min(a[i], s[-1]))
	s = s[::-1]
	ans = "YES"
	for i in range(1,n-1):
		if a[i]>p[i-1]+s[i+1]:
			ans = "NO"
			break
	if ans=="NO":
		print (ans)
		continue
	new = [a[0]]
	for i in range(1, n):
		if a[i]==a[i-1]:
			continue
		new.append(a[i])

	if len(new)==1:
		print ("YES")
		continue
	high, low = 0, 0
	if new[0]>new[1]:
		high += 0
	else:
		low += new[0]
	if new[-1]>new[-2]:
		high += 0
	else:
		low += new[-1]
	n = len(new)
	for i in range(1,n-1):
		if new[i]>new[i-1] and new[i]>new[i+1]:
			high += new[i]
		if new[i]<new[i-1] and new[i]<new[i+1]:
			low += new[i]
	if high>low:
		print ("NO")
	else:
		print ("YES")





