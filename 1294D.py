import sys
input = sys.stdin.readline
q,x = map(int,input().split())
d = {}
for i in range(x):
	d[i] = 0
mex = 0
done = {}
for i in range(q):
	n = int(input())
	n = n%x
	d[n] += 1
	n = n+(d[n]-1)*x
	done[n] = 1
	while mex in done:
		mex += 1
	print (mex)