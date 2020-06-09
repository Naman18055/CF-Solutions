for nt in range(int(input())):
	n = int(input())
	m = []
	for i in range(n):
		m.append(input())
	ans = "YES"
	for i in range(n):
		for j in range(n):
			if m[i][j]=="1":
				if j==n-1 or i==n-1:
					continue
				if j!=n-1 and m[i][j+1]=="1":
					continue
				if i!=n-1 and m[i+1][j]=="1":
					continue
				ans="NO"
	print (ans)