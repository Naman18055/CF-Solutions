import sys

def ask_query(typ, l, r, x):
	print ("?", typ, l+1, r+1, x)
	sys.stdout.flush()
	return int(input())

for nt in range(int(input())):
	n = int(input())
	ans = [0]*n
	ind = -1
	for i in range(0, n-1, 2):
		mx = ask_query(1, i, i+1, n-1)
		if mx==n:
			ans[i+1] = n
			ind = i+1
			break
		elif mx==n-1:
			mx = ask_query(1, i+1, i, n-1)
			if mx==n:
				ans[i] = n
				ind = i
				break
	if ind==-1:
		ans[-1] = n
		ind = n-1

	for i in range(n):
		if ans[i]==0:
			ans[i] = ask_query(2, i, ind, 1)
	print ("!",*ans)

