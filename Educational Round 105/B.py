for nt in range(int(input())):
	n, u, r, d, l = map(int,input().split())
	for mask in range(16):
		rU, rR, rD, rL = u, r, d, l
		if mask & 1:
			rU -= 1
			rL -= 1
		if mask & 2:
			rL -= 1
			rD -= 1
		if mask & 4:
			rD -= 1
			rR -= 1
		if mask & 8:
			rR -= 1
			rU -= 1
		if min(rU, rR, rD, rL) >= 0 and max(rU, rR, rD, rL) <= n-2:
			print("YES")
			break
	else:
		print("NO")