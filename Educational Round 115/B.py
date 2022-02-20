def complete(a, b):
	c = set()
	for i in a:
		c.add(i)
	for i in b:
		c.add(i)
	if len(c)==n:
		return True

for nt in range(int(input())):
	n = int(input())
	s = []
	for i in range(n):
		s.append(list(map(int,input().split())))
	days = {}
	for i in range(5):
		students = set()
		for j in range(n):
			if s[j][i]==1:
				students.add(j)
		if len(students)>=n//2:
			days[str(i)] = students
	flag = False
	# print (days)
	for i in days:
		for j in days:
			if i==j:
				continue
			if complete(days[i], days[j]):
				flag = True
				break
	if flag:
		print ("YES")
	else:
		print ("NO")

	