for nt in range(int(input())):
	n = int(input())
	if n%7==0:
		print (0,0,n//7)
		continue
	if n%5==0:
		print (0,n//5,0)
		continue
	if n%3==0:
		print (n//3,0,0)
		continue
	flag = 0
	for i in range(200):
		if n-5*i<=0:
			break
		if (n-5*i)%3==0:
			print ((n-5*i)//3,i,0)
			flag = 1
			break
	if not flag:
		print (-1)