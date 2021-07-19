mod = 998244353
import sys
input = sys.stdin.readline

def ncr(n, r):
	return ((fact[n]*pow(fact[r]*fact[n-r], mod-2, mod))%mod)

fact = [1, 1]
for i in range(2, 100010):
	fact.append((fact[-1]*i)%mod)
for nt in range(int(input())):
	n = int(input())
	s = input()
	i = 0
	o, z = 0, 0
	while i<n:
		if s[i]=="0":
			z += 1
			i += 1
		elif s[i]=="1" and s[i+1]=="1":
			o += 1
			i += 2
		else:
			i += 1
	# print (z+o, o)
	print (ncr(z+o, o))