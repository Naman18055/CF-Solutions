import sys
input = sys.stdin.readline

for nt in range(int(input())):
	n,k = map(int,input().split())
	a = sorted(list(set(list(map(int,input().split())))))
	if len(a)<=k:
		print (1)
		continue
	if k==1 and len(a)!=1:
		print (-1)
		continue
	print (1 + (len(a)-k-1)//(k-1)+1)
	
