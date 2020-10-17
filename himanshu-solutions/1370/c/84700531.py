import sys
# from collections import deque
# from collections import Counter
from math import sqrt
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
	if(n==1):
		print('FastestFinger')
	elif(n%2==1 or n==2):
		print('Ashishgup')
	else:
		f=True
		for i in range(2,int(sqrt(n)+2)):
			if(n%i==0):
				if((i%2==1 and n//i!=2) or ((n//i)%2==1 and i!=2)):
					f=False
					break
		if(f):
			print("FastestFinger")
		else:
			print("Ashishgup")