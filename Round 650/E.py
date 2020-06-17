from collections import Counter
import math

def check(b,a):
	count = 0
	for i in range(len(l)):
		count += l[i]//a
	if count>=b:
		return True
	return False

for nt in range(int(input())):
	n,k = map(int,input().split())
	s = input()
	c = Counter(s)
	if len(c)==1:
		print (n)
		continue
	l = []
	for i in c:
		l.append(c[i])
	l.sort(reverse=True)
	for i in range(1,n+1):
		if k%i==0:
			num = i
	ans = num
	# print (num)
	for i in range(num+1,n+1):
		hcf = math.gcd(i,k)
		if check(hcf,i//hcf):
			ans = i
	print (ans)