import sys

def ask_query(num):
	print (num)
	sys.stdout.flush()
	return int(input())

for nt in range(int(input())):
	n, k = map(int,input().split())
	curr = 0
	for i in range(n):
		if i==0:
			r = ask_query(0)
		else:
			r = ask_query(i^(i-1))
		if r:
			break
	
