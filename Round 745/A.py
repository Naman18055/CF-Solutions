mod = 10**9+7
fact = [1, 1]
for i in range(2, 300010):
	fact.append((fact[-1]*i)%mod)

for nt in range(int(input())):
	n = int(input())*2
	print ((fact[n]*pow(2, mod-2, mod))%mod)


