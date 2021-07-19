import sys
input = sys.stdin.readline

for nt in range(int(input())):
	n = int(input())
	a = list(map(int,input().split()))
	b = list(map(int,input().split()))
	a.sort()
	b.sort()
	c = c2 = n//4
	s1 = sum(a)-sum(a[0:c])
	s2 = sum(b)-sum(b[0:c])
	ans = 0
	while s1<s2:
		s1 += 100
		ans += 1
		if c!=0 and (n+ans)%4!=0:
			s2 += b[c-1]
			c -= 1

		if (n+ans)%4==0:
			s1 -= a[c2]
			c2 += 1

		# print (s1, s2)
	print (ans)




