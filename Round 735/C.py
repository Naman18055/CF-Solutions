for nt in range(int(input())):
	n, m = map(int,input().split())
	if m<n:
		print (0)
	else:
		m = bin(m+1)[2:]
		n = "0"*(len(m) - len(bin(n)[2:])) + bin(n)[2:]
		ans = ["0"]*len(m)
		for i in range(len(m)):
			if n[i]==m[i]:
				ans[i] = "0"
			else:
				if n[i]=="1" and m[i]=="0":
					break
				else:
					ans[i] = "1"
		# print (n)
		# print (m)
		# print ("".join(ans), maxx, minn)
		print (int("".join(ans), 2))