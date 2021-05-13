import sys

def ask_query(l, r):
	print ("?", l+1, r+1)
	sys.stdout.flush()
	return int(input())

def check(low, mid):
	return mid - low + 1 - ask_query(low, mid)

d = {}
n, t = map(int,input().split())
for nt in range(t):
	k = int(input())
	low = 0
	high = n-1
	while low<high:
		mid = (low+high)//2
		if (low, mid) not in d:
			count = check(low, mid)
			d[(low, mid)] = count
		count = d[(low, mid)]
		if count>=k:
			high = mid
		else:
			k -= count
			low = mid + 1
		if (low, high) in d:
			d[(low, high)] -= 1
	print ("!", high+1)

