for nt in range(int(input())):
	n, k = map(int,input().split())
	s = input()
	if 2*k==n:
		print ("NO")
		continue
	ans = "NO"
	if s[0:k]==s[n-k:][::-1]:
		ans = "YES"
	print (ans)
