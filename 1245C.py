mod = 10**9+7
v = [1,1]
s = input()
if "w" in s or "m" in s:
	print (0)
	exit()
length = len(s)
u,n = [],[]
for i in range(1,length):
	if (s[i]=="u" or s[i]=="n") and s[i]==s[i-1]:
		v.append((v[-1]+v[-2])%mod)
	else:
		v.append(v[-1])
print (v[-1])