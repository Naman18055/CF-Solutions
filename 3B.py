import sys
input = sys.stdin.readline
n,v = map(int,input().split())
o,t = [],[]
for i in range(n):
	x,y = map(int,input().split())
	if x==1:
		o.append((y,i+1))
	else:
		t.append((y,i+1))
o.sort(reverse=True)
t.sort(reverse=True)
if len(o)==0:
	ans = 0
	f = []
	for i in range(len(t)):
		if (i+1)*2<=v:
			ans += t[i][0]
			f.append(t[i][1])
	print (ans)
	print (*f)
else:
	p = [o[0][0]]
	for i in range(1,len(o)):
		p.append(p[-1]+o[i][0])
	ans = p[min(len(p)-1,v-1)]
	s = 0
	ind = -1
	for i in range(len(t)):
		if (i+1)*2>v:
			break
		s += t[i][0]
		if (i+1)*2!=v:
			if s+p[min(len(p)-1,v-(i+1)*2-1)]>ans:
				ans = s+p[min(len(p)-1,v-(i+1)*2-1)]
				ind = i
		else:
			if s>ans:
				ans = max(ans,s)
				ind = i
	print (ans)
	f = []
	for i in range(ind+1):
		f.append(t[i][1])
	for i in range(min(len(o),v-(ind+1)*2)):
		f.append(o[i][1])
	print (*f)