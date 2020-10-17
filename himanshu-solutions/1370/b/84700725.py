import sys
# from collections import deque
# from collections import Counter
# from math import sqrt
# from math import log
# from math import ceil

# alpha=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# mod=10**9+7
# mod=998244353

fast_reader=sys.stdin.readline
fast_writer=sys.stdout.write

def input():
	return fast_reader().strip()

def print(*argv):
	fast_writer(' '.join((str(i)) for i in argv))
	fast_writer('\n')

#____________________________________________________________________________________________________________________________________

for _ in range(int(input())):
	n=int(input())
	l=list(map(int, input().split()))
	ev=[]
	od=[]
	for i in range(2*n):
		if(l[i]%2==0):
			ev.append(i+1)
		else:
			od.append(i+1)
	c=0
	for i in range(0,len(ev)-1,2):
		if(c==n-1):
			break
		print(ev[i],ev[i+1])
		c+=1
	for i in range(0,len(od)-1,2):
		if(c==n-1):
			break
		print(od[i],od[i+1])
		c+=1