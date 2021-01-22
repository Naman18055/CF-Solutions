import sys
input = sys.stdin.readline

for nt in range(int(input())):
	n,m = map(int,input().split())
	rows, col = [], []
	for i in range(n):
		rows.append(list(map(int,input().split())))
	for i in range(m):
		col.append(list(map(int,input().split())))
	d = {}
	
	for i in range(n):
		d[rows[i][0]] = i

	for i in range(m):
		if col[i][0] in d:
			c = list(col[i])

	# print ()
	for i in c:
		print (*rows[d[i]])

