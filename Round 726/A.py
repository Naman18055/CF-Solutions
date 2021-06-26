import sys
input = sys.stdin.readline

for nt in range(int(input())):
	n = int(input())
	a = list(map(int,input().split()))
	am = sum(a)/n
	if am==1:
		print (0)
		continue
	if am<1:
		print (1)
		continue
	if am>1:
		print (sum(a)-n)