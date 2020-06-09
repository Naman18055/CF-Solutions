import math
for nt in range(int(input())):
	n,k1,k2=map(int,input().split())
	s = input()
	g = []
	count = 0
	for i in range(n):
		if s[i]=="1":
			count += 1
		else:
			if count != 0:
				g.append(count)
				count = 0
	if count!=0:
		g.append(count)
	ans = 0
	for i in g:
		if i==1:
			ans += k1
		else:
			if k2<=2*k1:
				if i%2:
					ans += k2*(i//2) + k1*(i%2)
				else:
					ans += k2*(i//2)
			else:
				ans += k1*i
	print (ans)