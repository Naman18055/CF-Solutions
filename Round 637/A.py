import math
def mult_input():
	return map(int,input().split())

def list_input():
	return list(map(int,input().split()))

for nt in range(int(input())):
	n,a,b,c,d=mult_input()
	x=a-b
	y=a+b
	# print (n*x,n*y)
	if n*x>c+d or n*y<c-d:
		print ("No")
	else:
		print ("Yes")
