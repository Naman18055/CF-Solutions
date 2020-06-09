def calc(a,b):
	return (abs(a[0]-b[0])+abs(a[1]-b[1]))

def moves(a,b):
	return (b[0]-a[0])*"R"+(b[1]-a[1])*"U"

for nt in range(int(input())):
	n = int(input())
	p = []
	for i in range(n):
		p.append(tuple(map(int,input().split())))
	p.sort()
	curr = (0,0)
	i = 0
	ans = ""
	while i<n:
		if p[i][1]<curr[1]:
			ans = -1
			break
		ans += moves(curr,p[i])
		curr = p[i]
		i += 1
	if ans==-1:
		print ("NO")
	else:
		print ("YES")
		print (ans)