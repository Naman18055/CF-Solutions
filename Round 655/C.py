for nt in range(int(input())):
	n = int(input())
	a = list(map(int,input().split()))
	b = sorted(a)
	if a==b:
		print (0)
		continue
	else:
		flag = []
		for i in range(n):
			if a[i]!=i+1:
				flag.append(i)
		# print (flag)
		if len(flag)!=0:
			if flag[-1] - flag[0] == len(flag)-1:
				print (1)
			else:
				print (2)
		else:
			print (1)