mod = 10**9+7
for nt in range(int(input())):
	n, k = map(int,input().split())
	num = bin(k)[2:]
	ans = 0
	for i in range(len(num)-1, -1, -1):
		ans = (ans+(int(num[i])*(pow(n, len(num)-1-i, mod))))%mod
	print (ans)
