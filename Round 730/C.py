def solve(c, m, p, length):
	c = round(c, 8)
	p = round(p, 8)
	m = round(m, 8)
	# print (length, c, m, p, length)
	if c==0 and m==0:
		return p*length

	ans = 0
	if c==0:
		ans += m * solve(c, max(m-v, 0), p+min(m, v), length + 1)

	elif m==0:
		ans += c * solve(max(c-v, 0), m, p+min(c, v), length + 1)

	else:
		ans += c * solve(max(c-v, 0), m+min(c, v)/2, p+min(c, v)/2, length + 1)
		ans += m * solve(c+min(m, v)/2, max(m-v, 0), p+min(m, v)/2, length + 1)
	return length*p + ans

done = {}
for nt in range(int(input())):
	c, m, p, v = map(float,input().split())
	if (c, m) in done:
		print (done[(c, m)])
	else:
		ans = solve(c, m, p, 1)
		done[(c, m)] = ans
		done[(m, c)] = ans
		print (ans)
