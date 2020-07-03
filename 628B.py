s = input()
ans = 0
if int(s[0])%4==0:
	ans += 1
for i in range(1,len(s)):
	if int(s[i-1]+s[i])%4==0:
		ans += i
	if int(s[i])%4==0:
		ans += 1
print (ans)