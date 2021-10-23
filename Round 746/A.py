import sys
input = sys.stdin.readline

for nt in range(int(input())):
	n, h = map(int,input().split())
	a = sorted(list(map(int,input().split())))
	if h<=a[-1]:
		print (1)
		continue
	t = h/(a[-1]+a[-2])
	print (int(t)*2 + min(2, (h%(a[-1]+a[-2])-1)//a[-1]+1))

