s = input()
pref = [0]
for i in range(1,len(s)):
	if s[i]==s[i-1]:
		pref.append(pref[-1]+1)
	else:
		pref.append(pref[-1])
for i in range(int(input())):
	l,r = map(int,input().split())
	print (pref[r-1]-pref[l-1])