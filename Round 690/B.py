for nt in range(int(input())):
	n = int(input())
	a = input()
	s = "2020"
	ans = "NO"
	for i in range(5):
		if a[0:i]==s[0:i] and a[n-4+i:]==s[i:]:
			ans = "YES"
			break
	print (ans)