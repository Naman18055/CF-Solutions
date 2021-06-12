import sys
input = sys.stdin.readline

for nt in range(int(input())):
	n = int(input())
	a = list(map(int,input().split()))
	s = sum(a)
	if s%n!=0:
		print (-1)
		continue
	v = s//n
	ans = 0
	for i in a:
		if i>v:
			ans += 1
	print (ans)