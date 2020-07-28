import sys
input = sys.stdin.readline

def solve1d(a):
	a.sort()
	for i in range(0,len(a)-1,2):
		print (a[i][-1]+1,a[i+1][-1]+1)
	if len(a)%2:
		return a[-1]
	return False


def solve2d(start,end):
	d = {}
	for i in range(start,end+1):
		if coor[i][1] not in d:
			d[coor[i][1]] = [[coor[i][0],coor[i][2],coor[i][3]]]
		else:
			d[coor[i][1]].append([coor[i][0],coor[i][2],coor[i][3]])

	left = []
	for i in d:
		x = solve1d(d[i])
		if x:
			left.append([i,x[1],x[-1]])
	left.sort()
	for i in range(0,len(left)-1,2):
		print (left[i][-1]+1,left[i+1][-1]+1)
	if len(left)%2:
		return left[-1]
	return False

def solve3d():
	coor.sort(key = lambda x:x[2])
	prev = 0
	# print (coor)
	left = []
	for i in range(1,n):
		if coor[i][2]!=coor[prev][2]:
			x = solve2d(prev,i-1)
			if x:
				left.append([x[1],x[-1]])
			prev = i
	x = solve2d(prev,n-1)
	if x:
		left.append([x[1],x[-1]])
	left.sort()
	for i in range(0,len(left),2):
		print (left[i][-1]+1,left[i+1][-1]+1)
	



n = int(input())
coor = []
for i in range(n):
	coor.append(list(map(int,input().split())))
	coor[-1].append(i)
solve3d()