import sys
input = sys.stdin.readline

for nt in range(int(input())):
	n = int(input())
	s = input()
	ans = 10**18
	for char in range(97, 123):
		i = 0
		j = n-1
		flag = False
		count = 0
		while i<j:
			if s[i]==s[j]:
				i += 1 
				j -= 1
			else:
				if s[i]==chr(char):
					count += 1
					i += 1
				elif s[j]==chr(char):
					count += 1
					j -= 1
				else:
					flag = True
					break
		if not flag:
			ans = min(ans, count)
	if ans==10**18:
		print (-1)
	else:
		print (ans)


