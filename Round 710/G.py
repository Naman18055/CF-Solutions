for nt in range(int(input())):
	s = input()
	n = len(s)
	vis = [0]*26
	d = {}
	for i in range(n):
		d[s[i]] = i
	ans = []
	stack = []
	for i in range(n):
		if not vis[ord(s[i])-97]:
			while stack and s[i]>stack[-1] and i<d[stack[-1]]:
				vis[ord(stack.pop())-97] = 0
			stack.append(s[i])
			vis[ord(s[i])-97] = 1
	print ("".join(stack))


