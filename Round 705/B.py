def check(num):
	hr = str(num//m)
	mn = str(num%m)
	hr, mn = clean(hr+":"+mn).split(":")
	hrm = mnm = ""
	for i in hr:
		if int(i) in not_mir:
			return False
		hrm += str(mir[int(i)])
	for i in mn:
		if int(i) in not_mir:
			return False
		mnm += str(mir[int(i)])
	hrm = hrm[::-1]
	mnm = mnm[::-1]
	# print (hr, mn, hrm, mnm)
	if int(hrm)>=m:
		return False
	if int(mnm)>=h:
		return False
	return True



def clean(ans):
	s = ans.split(":")
	if len(s[0])==1:
		s[0] = "0"+s[0]
	if len(s[1])==1:
		s[1] = "0"+s[1]
	return ":".join(s)

not_mir = {3, 4, 6, 7, 9}
mir = {0: 0, 1: 1, 8: 8, 2: 5, 5: 2}
for nt in range(int(input())):
	h, m = map(int,input().split())
	s = list(map(int, input().split(":")))
	ans = "00:00"
	for i in range(s[0]*m+s[1], h*m):
		# print (i, i//m, i%m)
		if check(i):
			ans = str(i//m)+":"+str(i%m)
			break
	print (clean(ans))