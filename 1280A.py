mod = 10**9+7
for nt in range(int(input())):
	x = int(input())
	s = input()
	n = len(s)
	ans = n
	for i in range(x):
		if len(s)<x:
			s += ((int(s[i])-1)*s[i+1:])
			ans = len(s)
		else:
			ans += ((int(s[i])-1)*(ans-i-1))
		ans = ans%mod
		# print (s,ans)
	print (ans)