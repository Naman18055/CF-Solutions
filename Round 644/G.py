for nt in range(int(input())):
	n,m,a,b=map(int,input().split())
	if n*a != m*b:
		print ("NO")
		continue
	print ("YES")
	if a==m:
		ans = [["1" for i in range(m)] for j in range(n)]
		for i in ans:
			for j in i:
				print (j,end="")
			print ()
		continue
	ans = ["1"*a+"0"*(m-a)]
	for i in range(n-1):
		ans.append(ans[-1][m-a:]+ans[-1][0:m-a])
	for i in ans:
		for j in i:
			print (j,end="")
		print ()