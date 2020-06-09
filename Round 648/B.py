import sys
input = sys.stdin.readline
for nt in range(int(input())):
	n = int(input())
	a = list(map(int,input().split()))
	b = list(map(int,input().split()))
	if sorted(a)!=a:
		if 1 not in b or 0 not in b:
			print ("NO")
			continue
	print ("YES")
