n = int(input())
s = input()
t = input()
if s==t:
	print(0)
	exit()
if s.count("1")!=t.count("1"):
	print (-1)
	exit()
d = []
e = []
for i in range(n):
	if s[i]!=t[i]:
		d.append(s[i])
		e.append(t[i])
e.extend(e)
# def KMPSearch(pat, txt): 
# 	M = len(pat) 
# 	N = len(txt) 
# 	lps = [0]*M 
# 	j = 0 
# 	computeLPSArray(pat, M, lps) 
# 	i = 0 
# 	while i < N: 
# 		if pat[j] == txt[i]: 
# 			i += 1
# 			j += 1

# 		if j == M: 
# 			return i-j
# 			j = lps[j-1] 
# 		elif i < N and pat[j] != txt[i]: 
# 			if j != 0: 
# 				j = lps[j-1] 
# 			else: 
# 				i += 1
# 	return -1

# def computeLPSArray(pat, M, lps): 
# 	len = 0
# 	lps[0]
# 	i = 1
# 	while i < M: 
# 		if pat[i]== pat[len]: 
# 			len += 1
# 			lps[i] = len
# 			i += 1
# 		else: 
# 			if len != 0: 
# 				len = lps[len-1] 
# 			else: 
# 				lps[i] = 0
# 				i += 1

# ans = KMPSearch(d, e) 
# print (ans)

def kmp(pattern, text):
	failure = get_failure_array(pattern)
	ans = 10**18
	i, j = 0, 0  # index into text, pattern
	while i < len(text) and j<len(pattern):
		if pattern[j] == text[i]:
			if j == (len(pattern) - 1):
				ans = min(ans,i-j)
			else:
				if (len(pattern)-1-j)%2==0:
					ans = min(ans,i-j + ((len(pattern)-1)-j)//2)
			j += 1
		elif j > 0:
			j = failure[j - 1]
			continue
		i += 1
	return ans


def get_failure_array(pattern):
	failure = [0]
	i = 0
	j = 1
	while j < len(pattern):
		if pattern[i] == pattern[j]:
			i += 1
		elif i > 0:
			i = failure[i - 1]
			continue
		j += 1
		failure.append(i)
	return failure

ans = kmp(d, e)
print (ans)
