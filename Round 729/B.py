import math

for nt in range(int(input())):
	n, a, b = map(int,input().split())
	if a==1:
		if (n-1)%b==0:
			print ("Yes")
		else:
			print ("No")
		continue

	if int(math.log(n, a))==math.log(n, a):
		print ("Yes")
		continue
	i = 0
	ans = "No"
	while a**i<=n:
		if (n-a**i)%b==0:
			ans = "Yes"
			break
		i += 1

	print (ans)
