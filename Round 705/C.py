from collections import Counter

def calc(c, l):
	s = 0
	r = [0]*26
	for i in range(26):
		s += (k-c[i]%k)%k
		r[i] = (k-c[i]%k)%k
	if s>l:
		return -1
	ans = "a"*(l-s)
	for i in range(26):
		ans += (chr(i+97))*r[i]
	return ans

for nt in range(int(input())):
	n, k = map(int,input().split())
	s = input()
	if n%k!=0:
		print (-1)
		continue
	c = [0]*26
	for i in s:
		c[ord(i)-97] += 1
	ans = True
	for i in c:
		if i%k!=0:
			ans = False
	if ans:
		print (s)
		continue


	found = False
	for i in range(n-1, -1, -1):
		c[ord(s[i])-97] -= 1
		for j in range(ord(s[i])+1, 123):
			c[j-97] += 1
			suff = calc(c, n-i-1)
			if suff!=-1:
				found = True
				suff = s[0:i]+chr(j)+suff
				break
			c[j-97] -= 1
		if found:
			break
	print (suff)

