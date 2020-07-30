n = int(input())
s = input()
ans = [0]*10
for k in s:
	if k=="L":
		i = 0
		while i<n and ans[i]==1:
			i += 1
		ans[i] = 1
	elif k=="R":
		j = 9
		while j>=0 and ans[j]==1:
			j -= 1
		ans[j] = 1
	else:
		ans[int(k)] = 0
	# print (ans)
print ("".join(map(str,ans)))