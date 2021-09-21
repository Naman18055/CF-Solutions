def isComp(num):
	num = int(num)
	for i in range(2, num):
		if num%i==0:
			return True
	return False

for nt in range(int(input())):
	n = int(input())
	s = input()
	ans = False
	for i in range(n):
		if s[i]=="8":
			ans = True
			print (1)
			print (8)
			break
		elif s[i]=="4":
			ans = True
			print (1)
			print (4)
			break
		elif s[i]=="6":
			ans = True
			print (1)
			print (6)
			break
		elif s[i]=="9":
			ans = True
			print (1)
			print (9)
			break
		elif s[i]=="1":
			ans = True
			print (1)
			print (1)
			break
	if ans:
		continue

	if n==2:
		print (2)
		print (s)
		continue

	for i in range(n):
		for j in range(i+1, n):
			if isComp(s[i]+s[j]):
				ans = True
				print (2)
				print (s[i]+s[j])
				break
		if ans:
			break



