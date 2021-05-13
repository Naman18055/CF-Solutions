for i in range(int(input())):
	n = input()
	ans = (len(n)-1)*9
	ans += int(n[0])
	if int(n[0]*len(n))>int(n):
		ans -= 1
	print (ans)
