import sys

def ask_query(l, r):
	if l==r:
		return -1
	print ("?", l, r)
	sys.stdout.flush()
	return int(input())

n = int(input())
s = True
low = 0
high = n-1
s = ask_query(1, n)
p = ask_query(1, s)
if p==s:
	low = 0
	high = s-2
	while low<high:
		mid = (low+high)//2
		p = ask_query(mid+1, s)
		if p==s:
			low = mid + 1
		else:
			high = mid - 1

	if ask_query(low+1, s)==s:
		print ("!", low+1)
	else:
		print ("!", low)
else:
	low = s
	high = n-1
	while low<high:
		mid = (low+high)//2
		p = ask_query(s, mid+1)
		if p==s:
			high = mid - 1
		else:
			low = mid + 1
	if ask_query(s, low+1)==s:
		print ("!", low+1)
	else:
		print ("!", low+2)





