import sys

def ask_query(i):
	print ("?", i)
	sys.stdout.flush()
	return int(input())

n = int(input())
low, high = 1, n
while low<high:
	mid = (low+high)//2
	x = ask_query(mid)
	y = ask_query(mid+1)
	if x<y:
		high = mid
	else:
		low = mid + 1
if low==n:
	print ("!", n)
else:
	x = ask_query(low)
	y = ask_query(low+1)
	if x<y:
		print ("!", low)
	else:
		print ("!", low+1)