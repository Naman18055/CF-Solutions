for nt in range(int(input())):
	s=input()
	n=len(s)
	if "1" not in s or "0" not in s:
		print (0)
		continue
	if s[0]=="0":
		pref0=[1]
		pref1=[0]
	else:
		pref0=[0]
		pref1=[1]
	for i in range(1,n):
		if s[i]=="0":
			pref0.append(pref0[-1]+1)
			pref1.append(pref1[-1])
		else:
			pref1.append(pref1[-1]+1)
			pref0.append(pref0[-1])
	ans=min(pref0[-1],pref1[-1])
	# print (pref0,pref1)
	# 000111 
	for i in range(1,n):
		ans=min(ans,pref1[i-1]+(pref0[-1]-pref0[i-1]))
	# 111000
	for i in range(1,n):
		ans=min(ans,pref0[i-1]+(pref1[-1]-pref1[i-1]))
	print (ans)
