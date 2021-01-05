for nt in range(int(input())):
	n,l = map(int,input().split())
	a = list(map(int,input().split()))
	t1, t2 = [0, a[0]], [0, l-a[-1]]
	s = 2
	for i in range(1,n):
		t1.append(t1[-1] + (a[i]-a[i-1])/s)
		s += 1
	t1.append(t1[-1] + (l-a[-1])/s)
	s = 2
	for i in range(n-2,-1,-1):
		t2.append(t2[-1] + (a[i+1]-a[i])/s)
		s += 1
	t2.append(t2[-1] + a[0]/s)
	t2 = t2[::-1]
	# print (*t1)
	# print (*t2)

	i = 0
	flag = -1
	while True:
		if t1[i]>t2[i]:
			break
		if t1[i]==t2[i]:
			flag = i
			break
		i += 1
	if flag!=-1:
		print (t1[flag])
		continue
	i -= 1
	s1 = i+1
	s2 = n-i+1

	# print (i, s1, s2)
	if t1[i]<=t2[i+1]:
		if i==n:
			d = (l-a[-1]-(t2[i+1]-t1[i])*s1)
		elif i==0:
			d = (a[i]-(t2[i+1]-t1[i])*s1)
		else:
			d = (a[i]-a[i-1]-(t2[i+1]-t1[i])*s1)
		print ((t2[i+1]) + (d)/(s1+s2))
	else:
		if i==n:
			d = (l-a[-1]-(-t2[i+1]+t1[i])*s2)
		elif i==0:
			d = (a[i]-(-t2[i+1]+t1[i])*s2)
		else:
			d = (a[i]-a[i-1]-(-t2[i+1]+t1[i])*s2)
		print (t1[i]+(d/(s1+s2)))
