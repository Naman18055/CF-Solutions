for nt in range(int(input())):
	n,k = map(int,input().split())
	s = list(input())
	o,z = 0,0
	for i in range(k):
		if s[i]=="1":
			o += 1
		elif s[i]=="0":
			z += 1
	if o>k//2 or z>k//2:
		print ("NO")
		continue
	ans = "YES"
	for i in range(k,n):
		if s[i]=="?" and s[i-k]!="?":
			s[i] = s[i-k]
		if s[i]!="?" and s[i-k]!="?" and s[i]!=s[i-k]:
			ans = "NO"
			break
		if s[i]=="1":
			o += 1
		elif s[i]=="0":
			z += 1
		if s[i-k]=="1":
			o -= 1
		elif s[i-k]=="0":
			z -= 1
		if o>k//2 or z>k//2:
			ans = "NO"
			break
	print (ans)