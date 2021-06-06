for nt in range(int(input())):
	n = int(input())
	ans = "NO"
	for i in range(11):
		k = n-111*i
		if k>=0 and k%11==0:
			ans = "YES"
	print (ans)

