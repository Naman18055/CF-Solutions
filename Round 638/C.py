from collections import Counter

def mult_input():
	return map(int,input().split())

def list_input():
	return list(map(int,input().split()))

for nt in range(int(input())):
	n,k=mult_input()
	s=list(input())
	c=Counter(s)
	ans=[[] for i in range(k)]
	s.sort()
	if c[s[0]]<k:
		print (s[k-1])
		continue
	elif c[s[0]]==k:
		j=0
		for i in range(k):
			ans[i].append(s[j])
			j+=1
		if j==len(s):
			print ("".join(map(str,ans[0])))
			continue
		if s[j]!=s[-1]:
			for i in range(j,n):
				ans[0].append(s[i])
			print ("".join(map(str,ans[0])))
		else:
			count=0
			for i in range(j,n):
				ans[count%k].append(s[i])
				count+=1
			print ("".join(map(str,ans[0])))
	else:
		j=0
		for i in range(k):
			ans[i%k].append(s[j])
			j+=1
		if j==len(s):
			print ("".join(map(str,ans[0])))
			continue
		if s[j]==s[-1]:
			count=0
			for i in range(j,n):
				ans[count%(k)].append(s[i])
				count+=1
		else:
			for i in range(j,n):
				ans[0].append(s[i])
		print ("".join(map(str,ans[0])))