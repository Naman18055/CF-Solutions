for nt in range(int(input())):
	h, w = map(int,input().split())
	ans = [[0 for i in range(w)] for j in range(h)]
	for i in range(0, w, 2):
		ans[0][i] = 1
	for i in range(0, h, 2):
		ans[i][0] = 1
	for i in range(2, h-2, 2):
		ans[i][-1] = 1
	for i in range(2, w, 2):
		ans[-1][i] = 1
	for i in range(h):
		print ("".join(map(str, ans[i])))
	print ()

