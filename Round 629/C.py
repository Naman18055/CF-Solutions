for nt in range(int(input())):
	n=int(input())
	x=input()
	ans1=""
	ans2=""
	flag=0
	for i in range(n):
		if x[i]=="2":
			if not flag:
				ans1+="1"
				ans2+="1"
			else:
				ans1+="0"
				ans2+="2"
		elif x[i]=="1":
			if not flag:
				ans1+="1"
				ans2+="0"
				flag=1
			else:
				ans1+="0"
				ans2+="1"
		else:
			ans1+="0"
			ans2+="0"
	print (ans1)
	print (ans2)