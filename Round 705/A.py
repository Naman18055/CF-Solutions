for nt in range(int(input())):
	n, k = map(int,input().split())
	ans = []
	for i in range((k-1)//2+1, k):
		ans.append(i)
	for i in range(k+1, n+1):
		ans.append(i)
	print (len(ans))
	print (*ans)