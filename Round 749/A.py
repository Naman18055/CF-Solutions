import sys
input = sys.stdin.readline

for nt in range(int(input())):
	n = int(input())
	a = list(map(int,input().split()))
	s = sum(a)
	if s%2:
		comp = False
		for i in range(2, int(s**0.5)+1):
			if s%i==0:
				comp = True
				break
		if comp:
			print (n)
			print (*[i for i in range(1, n+1)])
		else:
			print (n-1)
			ans = []
			done = 0
			for i in range(1, n+1):
				if a[i-1]%2 and not done:
					done = 1
					continue
				ans.append(i)
			print (*ans)
	else:
		print (n)
		print (*[i for i in range(1, n+1)])
