for nt in range(int(input())):
	n = int(input())
	if n<=2:
		print ("".join([str(i) for i in range(9,9-n, -1)]))
		continue

	a = [str(i) for i in range(10)]
	a = ["9", "8", "9"]+a*((n-3)//10)+a[0:(n-3)%10]
	print ("".join(a))