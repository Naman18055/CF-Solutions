def change(a, b):
	a = str(a)
	b = str(b)
	if len(a)==a.count("9"):
		return len(a)+1
	ans = 0
	for i in range(len(a)):
		if a[i]!=b[i]:
			ans += 1
	return ans


for nt in range(int(input())):
	l, r = map(int,input().split())
	l = "0"*(len(str(r))-len(str(l))) + str(l)
	r = str(r)
	ans = 0
	for i in range(1, len(l)+1):
		ans += int(r[0:i]) - int(l[0:i])
	print (ans)
	# freq = {}
	# while l!=r:
	# 	ans = change(l, l+1)
	# 	if ans not in freq:
	# 		freq[ans] = 1
	# 	else:
	# 		freq[ans] += 1
	# 	l += 1
	# print (freq)