mod = 10**9+7
powers = [1]
for i in range(1, 200000+1):
	powers.append((powers[-1]*2)%mod)
for nt in range(int(input())):
	n, k = map(int,input().split())
	add = [1]
	for i in range(k):
		add.append((add[-1]*powers[n])%mod)
	if n%2:
		ans = pow(2, n*k, mod)
		for i in range(k):
			ans -= ((((pow(powers[n-1]+1, i, mod)) * (powers[n-1]-1))%mod) * add[k-i-1])%mod
			ans = ans%mod
		print (ans)
	else:
		ans = pow(2, n*k, mod)
		for i in range(k):
			ans -= ((((pow(powers[n-1]-1, i, mod)) * (powers[n-1]))%mod) * add[k-i-1])%mod
			ans = ans%mod
			# print (k, ans)
		print (ans)





