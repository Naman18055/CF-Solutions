n, mod = map(int,input().split())
if n==1:
	print (1)
	exit()
fact = [{} for i in range(n+1)]
for i in range(1, n+1):
	for j in range(i, n+1, i):
		fact[j][i] = 1

ans = [0]*n
ans[0] = 1
ans[1] = 2

for i in range(2, n):
	ans[i] = (2*ans[i-1]) % mod
	for j in fact[i+1]:
		if j==i+1:
			continue
		if j==1:
			ans[i] = (ans[i] + ans[j-1]) % mod
			continue
		ans[i] = (ans[i] + (ans[j-1] - ans[j-2])) % mod
print (ans[-1]%mod)
