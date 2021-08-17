import sys
input = sys.stdin.readline

for nt in range(int(input())):
	n = int(input())
	a = list(map(int,input().split()))
	if a[0]==1:
		print (*([n+1]+[i for i in range(1, n+1)]))
	elif a[-1]==0:
		print (*([i for i in range(1, n+2)]))
	else:
		found = False
		for i in range(n-1):
			if a[i]==0 and a[i+1]==1:
				found = True
				ind = i
				break
		if found:
			print (*([i for i in range(1, ind+2)]+[n+1]+[i for i in range(ind+2, n+1)]))
		else:
			print (-1)