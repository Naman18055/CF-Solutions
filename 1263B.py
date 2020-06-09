for i in range(int(input())):
	n = int(input())
	p = []
	ans = 0
	for i in range(n):
		p.append(input())
	for i in range(n):
		if p[i] in p[i+1:]:
			ans+=1
			j=0
			while p[i] in p[i+1:]+p[:i]:
				p[i]=p[i][:3]+str(j)
				j+=1
	print(ans)
	for i in range(n):
		print(p[i])