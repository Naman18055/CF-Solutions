for nt in range(int(input())):
	n = int(input())
	a = list(map(int,input().split()))
	b = list(map(int,input().split()))
	d = []
	for i in range(n):
		d.append(b[i]-a[i])
	s = set(d)
	if len(s)==1:
		if d[0]<0:
			print ('NO')
			continue
		print ("YES")
		continue
	if len(s)>2:
		print ("NO")
		continue
	if 0 not in s:
		print ("NO")
		continue
	start,end = -1,-1
	for i in range(n):
		if d[i]!=0:
			start = i
			break
	for i in range(n-1,-1,-1):
		if d[i]!=0:
			end = i
			break
	if 0 in d[start:end] or d[start]<0:
		print ("NO")
	else:
		print ("YES")