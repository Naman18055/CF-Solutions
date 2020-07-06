def check(arr):
	for i in range(1,len(arr)):
		if arr[i][0]==len(arr[i-1][1]):
			if arr[i][1]!=arr[i-1][1]:
				return False
		else:
			if arr[i-1][1] not in arr[i][1]:
				return False
	return True


a = []
for nt in range(int(input())):
	s = input()
	a.append((len(s),s))
a.sort()
if check(a):
	print ("YES")
	for i in a:
		print (i[1])
else:
	print ("NO")