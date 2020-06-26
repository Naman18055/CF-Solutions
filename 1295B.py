import sys
input = sys.stdin.readline

def calc(s):
	return s.count("0")-s.count("1")

for nt in range(int(input())):
	n,k = map(int,input().split())
	s = input()
	b = calc(s)
	x = calc(s[0])
	p = [x]
	for i in range(1,n):
		x += calc(s[i])
		p.append(x)
	if b==0 and k in p:
		print (-1)
		continue
	if b==0 and k not in p:
		print (0)
		continue
	ans = 1 if k==0 else 0
	for i in p:
		if ((k-i)*b)>=0 and (k-i)%b == 0:
			ans += 1
	print (ans)
