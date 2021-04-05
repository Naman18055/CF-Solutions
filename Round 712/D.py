import sys

n = int(input())
m = [[0 for i in range(n)] for j in range(n)]
o = []
t = []
for i in range(n):
	for j in range(n):
		if (i+j)%2:
			t.append([i, j])
		else:
			o.append([i, j])

j, k = 0, 0
for i in range(n**2):
	a = int(input())
	if a==1:
		if j<len(t):
			print (2, t[j][0]+1, t[j][1]+1)
			j += 1
		else:
			print (3, o[k][0]+1, o[k][1]+1)
			k += 1
	elif a==2:
		if k<len(o):
			print (1, o[k][0]+1, o[k][1]+1)
			k += 1
		else:
			print (3, t[j][0]+1, t[j][1]+1)
			j += 1
	else:
		if j<len(t):
			print (2, t[j][0]+1, t[j][1]+1)
			j += 1
		else:
			print (1, o[k][0]+1, o[k][1]+1)
			k += 1
	sys.stdout.flush()


