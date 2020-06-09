import math
def mult_input():
	return map(int,input().split())

def list_input():
	return list(map(int,input().split()))

for nt in range(int(input())):
	n=int(input())
	a=0
	for i in range(n//2-1):
		a+=2**(i+1)
	a+=2**n
	b=2**(n+1)-2 -a
	print (abs(b-a))