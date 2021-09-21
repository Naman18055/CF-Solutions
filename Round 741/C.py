import sys
input = sys.stdin.readline

t = int(input())
for nt in range(t):
	n = int(input())
	s = input()

	if s.count('1') == n:
		print (1, n-1, 2, n)
		continue

	ind = s.find("0")
	if ind<n//2:
		print (ind+1, n, ind+2, n)
	else:
		print (1, ind+1, 1, ind)
