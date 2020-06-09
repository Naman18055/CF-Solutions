for nt in range(int(input())):
	n,m=map(int,input().split())
	ans=[]
	if n%2 and m%2:
		start="W"
		for i in range(n):
			if start=="B":
				prev="B"
				start="W"
			else:
				prev="W"
				start="B"
			for j in range(m):
				if prev=="B":
					print ("W",end="")
					prev="W"
				else:
					print ("B",end="")
					prev="B"
			print ()
	else:
		ans=[[] for i in range(n)]
		start="W"
		for i in range(n):
			if start=="B":
				prev="B"
				start="W"
			else:
				prev="W"
				start="B"
			for j in range(m):
				if prev=="B":
					ans[i].append("W")
					prev="W"
				else:
					ans[i].append("B")
					prev="B"
		if ans[-1][-1]=="W":
			ans[-1][-1]="B"
		else:
			ans[-1][-2]="B"
		for i in ans:
			for j in i:
				print (j,end="")
			print ()

