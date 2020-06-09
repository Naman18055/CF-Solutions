from copy import copy
for nt in range(int(input())):
	n,m=map(int,input().split())
	s=input()
	p=list(map(int,input().split()))
	d={0:{s[0]:1}}
	for i in range(1,n):
		d[i]=copy(d[i-1])
		if s[i] not in d[i]:
			d[i][s[i]]=1
		else:
			d[i][s[i]]+=1
	#print (d)
	ans=[0]*26
	for i in p:
		for j in range(26):
			if chr(j+97) in d[i-1]:
				ans[j]+=d[i-1][chr(j+97)]
	for i in s:
		ans[ord(i)-97]+=1
	print (*ans)
