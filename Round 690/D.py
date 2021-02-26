import sys
input = sys.stdin.readline

def check(num):
	i = 0
	s = 0
	while i<n:
		s += a[i]
		if s>num:
			return False
		elif s==num:
			s = 0
		i += 1
	return True

for nt in range(int(input())):
	n = int(input())
	a = list(map(int,input().split()))
	s = sum(a)
	m = max(a)
	fac = [1, s]
	for i in range(2, int(s**0.5)+1):
		if s%i==0:
			fac.append(i)
			if s//i != i:
				fac.append(s//i)
	fac.sort()
	for i in fac:
		# print (i, check(i))
		if check(i):
			ans = i
			break
	print (n-s//ans)


