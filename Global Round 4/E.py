s = input()
n = len(s)
i = 0
j = n-1
ans = [-1]*n
while i<j:
	if s[i]!=s[j]:
		if s[i+1]==s[j-1]:
			ans[i+1] = ans[j-1] = s[i+1]
			i+=2
			j-=2
		else:
			if s[i]==s[j-1]:
				ans[i] = ans[j-1] = s[i]
				i += 1
				j -= 2
			elif s[i+1]==s[j]:
				ans[i+1] = ans[j] = s[j]
				i += 2
				j -= 1
	else:
		ans[i] = ans[j] = s[i]
		i += 1
		j -= 1

a = ""
for i in ans:
	if i!=-1:
		a += i
if len(ans)<n//2:
	print ("IMPOSSIBLE")
	exit()
print (a)