def calc(a):
	minn1 = min(a[0:2])
	minn2 = min(a[2:])
	return [a[0]-minn1,a[1]-minn1,a[2]-minn2,a[3]-minn2]

for nt in range(int(input())):
	n = int(input())
	s = input()
	d = {}
	ans = 10**18
	state = [0,0,0,0]
	d[tuple(state)] = 0
	for i in range(n):
		if s[i]=="L":
			state[0] += 1
		elif s[i]=="R":
			state[1] += 1
		elif s[i]=="U":
			state[2] += 1
		else:
			state[3] += 1
		if tuple(calc(state)) in d:
			x = i-d[tuple(calc(state))]
			if x<ans:
				ans = x
				res = (d[tuple(calc(state))]+1,i+1)
			d[tuple(calc(state))] = i+1
		else:
			d[tuple(calc(state))] = i+1
		# print (d)
	if ans==10**18:
		print (-1)
	else:
		print (res[0],res[1])
