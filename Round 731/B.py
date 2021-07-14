for nt in range(int(input())):
	s = input()
	if "a" not in s:
		print ("NO")
	else:
		ind = s.find("a")
		i = ind - 1
		j = ind + 1
		curr = 98
		ans = "YES"
		while curr != 98 + len(s)-1:
			if i>=0 and s[i]==chr(curr):
				i -= 1
			elif j<len(s) and s[j]==chr(curr):
				j += 1
			else:
				ans = "NO"
				break
			curr += 1
		print (ans)
