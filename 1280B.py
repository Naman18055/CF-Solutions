def ifp(s):
	flag = 1
	for i in mat:
		if s in i:
			flag = 0
			break
	if flag:
		return False
	return True

def check3():
	if "A" in mat[0] or "A" in mat[-1]:
		return True
	flag1 = 0
	flag2 = 0
	for i in range(r):
		if mat[i][0]=="A":
			flag1 = 1
		if mat[i][-1]=="A":
			flag2 = 1
	if flag1 or flag2:
		return True
	return False

for nt in range(int(input())):
	r,c = map(int,input().split())
	mat = []
	for i in range(r):
		mat.append(input())
	if not ifp("A"):
		print ("MORTAL")
		continue
	if not ifp("P"):
		print (0)
		continue
	if "P" not in mat[0] or "P" not in mat[-1]:
		print (1)
		continue
	flag1 = 0
	flag2 = 0
	for i in range(r):
		if "P"==mat[i][0]:
			flag1 = 1
		if "P"==mat[i][-1]:
			flag2 = 1
	if not flag1 or not flag2:
		print (1)
		continue
	if mat[0][0] == "A" or mat[0][-1]=="A" or mat[-1][0]=="A" or mat[-1][-1]=="A":
		print (2)
		continue
	flag = 0
	for i in range(r):
		if "P" not in mat[i]:
			flag = 1
			break
	for i in range(c):
		flag2 = 0
		for j in range(r):
			if mat[j][i]=="P":
				flag2 = 1
				break
		if not flag2:
			flag = 1
			break
	if flag:
		print (2)
		continue
	if check3():
		print (3)
		continue
	print (4)