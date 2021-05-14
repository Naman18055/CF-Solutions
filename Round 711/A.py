import math
def check(num):
	s = sum(list(map(int, list(str(num)))))
	if math.gcd(num, s)>1:
		return True
	return False

for nt in range(int(input())):
	n = int(input())
	for i in range(n, n+100):
		if check(i):
			print (i)
			break
