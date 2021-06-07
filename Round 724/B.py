import sys
input = sys.stdin.readline

for nt in range(int(input())):
	n = int(input())
	s = input()
	ans = -1
	for i in range(97, 123):
		c = chr(i)
		if c not in s:
			ans = c
			break
	if ans!=-1:
		print (ans)
		continue
	flag = False
	for i in range(97, 123):
		for j in range(97, 123):
			c = chr(i)+chr(j)
			if c not in s:
				ans = c
				flag = True
				break
		if flag:
			break
	if ans!=-1:
		print (ans)
		continue
	for i in range(97, 123):
		for j in range(97, 123):
			for k in range(97, 123):
				c = chr(i)+chr(j)+chr(k)
				if c not in s:
					ans = c
					flag = True
					break
			if flag:
				break
		if flag:
			break
	print (ans)
