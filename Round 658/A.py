for nt in range(int(input())):
	n,m = map(int,input().split())
	a = set(list(map(int,input().split())))
	b = set(list(map(int,input().split())))
	flag = 0
	for i in a:
		if i in b:
			flag = i
			break
	if flag:
		print ("YES")
		print (1,i)
		continue
	print ("NO")
