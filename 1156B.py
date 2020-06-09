from collections import Counter

def check(s):
	for i in range(1,len(s)):
		if ord(s[i])==ord(s[i-1])+1 or ord(s[i])+1==ord(s[i-1]):
			return False
	return True

for nt in range(int(input())):
	s=list(input())
	c=Counter(s)
	s=list(set(s))
	n=len(s)
	s.sort()
	if n==1:
		print (s[0]*c[s[0]])
		continue
	new=[]
	for i in range(n//2):
		new.append(s[i])
		new.append(s[n-i-1])
	if n%2:
		new.append(s[n//2])
	if ord(new[-1])==ord(new[-2])+1 or ord(new[-1])+1==ord(new[-2]):
		new=[new[-1]]+new[:-1]
	# print (s,new)
	if check(new):
		ans=[]
		for i in new:
			ans.extend([i]*c[i])
		print ("".join(ans))
	else:
		print ("No answer")