import sys
input = sys.stdin.readline

for nt in range(int(input())):
	n = int(input())
	a = list(map(int,input().split()))
	# if nt==55:
		# print (*a)
		# continue
	s1, s2 = a[0], a[1]
	x1, x2 = a[0], a[1]
	m1, m2 = a[0]*n, a[1]*n
	c1, c2 = n-1, n-1
	ans = m1 + m2
	for i in range(2, n):
		if i%2:
			s2 += a[i]
			x2 = min(x2, a[i])
			m2 = s2-x2+x2*c2
			c2 -= 1
		else:
			s1 += a[i]
			x1 = min(x1, a[i])
			m1 = s1-x1+x1*c1
			c1 -= 1
		# print (i, m1, s1, x1, c1)
		# print (i, m2, s2, x2)
		ans = min(ans, m1+m2)
	print (ans)



	# o, e = [], []
	# for i in range(n):
	# 	if i%2:
	# 		o.append(a[i])
	# 	else:
	# 		e.append(a[i])
	# minn1 = 10**18
	# s = 0
	# for i in range(len(o)):
	# 	minn1 = min(minn1, (s+(n-i)*o[i]))
	# 	s += o[i]
	# minn2 = 10**18
	# s = 0
	# for i in range(len(e)):
	# 	minn2 = min(minn2, (s+(n-i)*e[i]))
	# 	s += e[i]
	# if minn1==10**18:
	# 	minn1=0
	# if minn2==10**18:
	# 	minn2=0
	# # print (o, e)
	# # print (minn1, minn2)
	# print (minn1+minn2)