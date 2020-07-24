def solve(s):
	new = ""
	for i in s:
		if i=="1":
			new += "0"
		else:
			new += "1"
	return new[::-1]

for nt in range(int(input())):
	n = int(input())
	a = input()
	b = input()
	ans = []
	i = 1
	count = 0
	if a[0]!=b[0]:
		ans.append(1)
	while i<n:
		if i+1<n:
			if a[i]!=b[i] and a[i+1]!=b[i+1]:
				if a[i]==a[i+1]:
					ans.append(i+2)
					ans.append(2)
					ans.append(i+2)
					i += 2
				else:
					if i+2>=n or a[i+2]==b[i+2]:
						ans.append(i+2)
						ans.append(1)
						ans.append(2)
						ans.append(1)
						ans.append(i+2)
						i += 3
						continue
					if a[i+2]==a[i]:
						ans.append(i+3)
						ans.append(3)
						ans.append(i+3)
						i += 3
					else:
						ans.append(i+3)
						ans.append(1)
						ans.append(3)
						ans.append(1)
						ans.append(i+3)
						i += 3
			elif a[i]==b[i] and a[i+1]!=b[i+1]:
				i += 1
			elif a[i]!=b[i] and a[i+1]==b[i+1]:
				ans.append(i+1)
				ans.append(1)
				ans.append(i+1)
				i += 2
			else:
				i += 2
		else:
			if a[i]!=b[i]:
				ans.append(i+1)
				ans.append(1)
				ans.append(i+1)
			break

	


	print (len(ans),end = " ")
	print (*ans)



# def solve(s):
# 	new = ""
# 	for i in s:
# 		if i=="1":
# 			new += "0"
# 		else:
# 			new += "1"
# 	return new[::-1]

# for nt in range(int(input())):
# 	n = int(input())
# 	a = input()
# 	b = input()
# 	ans = []
	# for i in range(n-1,-1,-1):
	# 	if a[i]!=b[i]:
	# 		if a[i]==a[0]:
	# 			ans.append(i+1)
	# 			a = solve(a[0:i+1]) + a[i+1:]
	# 		else:
	# 			ans.append(1)
	# 			ans.append(i+1)
	# 			a = solve(a[i]+a[1:i+1]) + a[i+1:]

# 	print (len(ans),end = " ")
# 	print (*ans)