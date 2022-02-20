for nt in range(int(input())):
	n = int(input())
	a = input()
	b = input()
	ans = "YES"
	for i in range(n):
		if a[i]=="1" and b[i]=="1":
			ans = "NO"
			break
	print (ans)

