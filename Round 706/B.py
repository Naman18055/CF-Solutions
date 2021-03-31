for nt in range(int(input())):
	n, k = map(int,input().split())
	a = list(map(int,input().split()))
	if k==0:
		print (len(set(a)))
		continue
	found = True
	a = sorted(list(set(a)))
	for i in range(max(a)):
		if a[i]!=i:
			found = False
			break
	if found:
		print (len(a)+k)
		continue

	m = max(a)+1
	for j in range(max(a)):
		if j not in a:
			m = j
			break
	a.append((m+max(a)-1)//2+1)
	print (len(set(a)))