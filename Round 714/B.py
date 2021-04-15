mod = 10**9+7
import sys
input = sys.stdin.readline


fact = [1, 1]
for i in range(2, 300000):
	fact.append((fact[-1]*i)%mod)
for nt in range(int(input())):
	n = int(input())
	a = list(map(int,input().split()))
	s = a[0]
	for i in range(1, n):
		s = s&a[i]
	if a.count(s)<=1:
		print (0)
		continue


	print (((a.count(s)*(a.count(s)-1))*fact[n-2])%mod)
