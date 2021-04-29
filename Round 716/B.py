mod = 10**9+7
for nt in range(int(input())):
	n, k = map(int,input().split())
	print (pow(n, k, mod))