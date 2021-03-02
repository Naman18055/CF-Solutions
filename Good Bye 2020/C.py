import random
for nt in range(int(input())):
	s = list(input())
	n = len(s)
	if n==1:
		print (0)
		continue

	i = 0
	ans = 0
	curr = 0
	while i<n-1:
		if s[i]==s[i+1]:
			ans += 1
			s[i+1] = curr
		elif i<n-2 and s[i:i+3]==s[i:i+3][::-1]:
			ans += 1
			s[i+2] = curr
			i += 1
		else:
			i += 1
			
		curr = str(int(curr)+1)
	print (ans)
