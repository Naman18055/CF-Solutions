def construct(num):
	ans = ""
	for i in range(num):
		ans += "("
	for i in range(num):
		ans += ")"
	return ans

for nt in range(int(input())):
	n = int(input())
	ans = []
	for i in range(n):
		s = construct(i+1)
		for i in range(2*n-len(s)):
			if i%2==0:
				s += "("
			else:
				s += ")"
		ans.append(s)
	for i in ans:
		print (i)
