def sum(n):
	count=0
	for i in n:
		count+=int(i)
	return count

t=int(input())
for nt in range(t):
	num = (input())
	n = int(num)
	if n==0:
		print ("red")
		continue
	if "0" not in num:
		print ("cyan")
		continue
	if sum(num)%3!=0:
		print ("cyan")
		continue
	flag=0
	for i in num:
		if i=="2" or i=="4" or i=="6" or i=="8":
			print ("red")
			flag=1
			break
	if flag==0:
		if num.count("0")>=2:
			print ("red")
		else:
			print ("cyan")

