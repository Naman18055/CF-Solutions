# import sys
# input = sys.stdin.readline

def check(s):
	stack = []
	ans = 1
	for i in range(n):
		if s[i]=="M":
			if not stack:
				ans = 0
				break
			else:
				stack.pop()
		else:
			stack.append("T")
	return ans

for nt in range(int(input())):
	n = int(input())
	s = input()
	m = s.count("M")
	t = n - m
	if t!=2*m:
		print ("NO")
		continue
	stack = []
	if check(s) and check(s[::-1]):
		print ("YES")
	else:
		print ("NO")