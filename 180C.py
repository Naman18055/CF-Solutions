s = input()
a,ans = 0,0
for i in range(len(s)):
	if ord(s[i])>=97:
		ans = min(a+1,ans)
		a += 1
	else:
		ans = min(a,ans+1)
print (ans)