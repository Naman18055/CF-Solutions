n, k = map(int,input().split())
s = input()
check = 0
pref = s
s += chr(123)
for i in range(1, n+1):
	if s[i]>s[check]:
		pref = s[0:i-check]
		break
	elif s[i]==s[check]:
		check += 1
	else:
		check = 0

ans = (pref*(k//len(pref)+1))[0:k]
print (ans)
