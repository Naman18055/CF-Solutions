def count1(s,pat):
	count = 0
	for i in range(len(s)-6): 
		if s[i:i+7]==pat:
			count += 1
	return count


for nt in range(int(input())):
	n = int(input())
	s = input()
	if count1(s,"abacaba")>=2:
		print ("No")
		continue
	elif count1(s,"abacaba")==1:
		print ("Yes")
		ans = ""
		for i in range(n):
			if s[i]=="?":
				ans += "z"
			else:
				ans += s[i]
		print (ans)
		continue

	string = "abacaba"
	ans = 0
	for i in range(n-6):
		temp = ""
		flag = 0
		for j in range(7):
			if s[i+j]=="?":
				temp += string[j]
			else:
				if s[i+j]!=string[j]:
					flag = 1
					break
				else:
					temp += s[i+j]
		if flag:
			continue
		else:
			new = s[0:i]+temp+s[i+7:]
			if count1(new,"abacaba")==1:
				ans = 1
				break
	if ans:
		ans = ""
		for i in new:
			if i=="?":
				ans += "z"
			else:
				ans += i
		print ("Yes")
		print (ans)
	else:
		print ("No")


