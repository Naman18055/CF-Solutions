for nt in range(int(input())):
	n = int(input())
	s = input()
	if "1" not in s:
		print (n)
		continue
	ans = n
	for i in range(n):
		if s[i]=="1":
			ans = max(ans,(i+1)*2,(n-i)*2)
	print (ans)