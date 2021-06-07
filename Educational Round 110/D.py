import sys
import io, os
input = sys.stdin.readline
 
k = int(input())
s = list(str(input().rstrip()))

def final():
	if s[-1]=="0":
		return c[-1][0]
	elif s[-1]=="1":
		return c[-1][1]
	else:
		return c[-1][0] + c[-1][1]

# k = int(input())
# s = list(input())
n = 2**k - 1
match_num = [0 for i in range(n)]
rnd_start = {}
rnd = [0 for i in range(n)]
curr = k-1
m = 1
for i in range(n):
	match_num[i] = m-1
	rnd[i] = curr+1
	if 2**curr == m:
		m = 0
		curr -= 1
		rnd_start[curr+2] = i-(2**(curr+1))+1
	m += 1
# print (match_num)
# print (rnd_start)
# print (rnd)

c = [[0, 0] for i in range(n)]
for i in range(2**(k-1)):
	c[i][0] = c[i][1] = 1
for i in range(2**(k-1), n):
	match = rnd_start[rnd[i]+1]+match_num[i]*2
	if s[match]=="0":
		c[i][0] = c[match][0]
	elif s[match]=="1":
		c[i][0] = c[match][1]
	else:
		c[i][0] = c[match][0] + c[match][1]
	match += 1
	if s[match]=="0":
		c[i][1] = c[match][0]
	elif s[match]=="1":
		c[i][1] = c[match][1]
	else:
		c[i][1] = c[match][0] + c[match][1]
# print (c)


for q in range(int(input())):
	ind, v = input().split()
	ind = int(ind)
	if s[ind-1]==v:
		print (final())
		continue

	ind -= 1
	if True:
		prev = s[ind]
		s[ind] = v
		curr = ind
		for i in range(rnd[ind]-1):
			match = rnd_start[rnd[curr]-1] + match_num[curr]//2
			if s[curr]=="0":
				c[match][match_num[curr]%2] = c[curr][0]
			elif s[curr]=="1":
				c[match][match_num[curr]%2] = c[curr][1]
			else:
				c[match][match_num[curr]%2] = c[curr][0] + c[curr][1]
			curr = match
		# print (final(), c)
		# s[ind] = prev
		# curr = ind
		# for i in range(rnd[ind]-1):
		# 	match = rnd_start[rnd[curr]-1] + match_num[curr]//2
		# 	if s[curr]=="1":
		# 		c[match][match_num[curr]%2] = c[curr][0]
		# 	elif s[curr]=="0":
		# 		c[match][match_num[curr]%2] = c[curr][1]
		# 	else:
		# 		c[match][match_num[curr]%2] = c[curr][0] + c[curr][1]
		# 	curr = match
	print (final())


