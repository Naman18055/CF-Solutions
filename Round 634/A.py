import sys
input = sys.stdin.buffer.readline
def list_input():
	return list(map(int,input().split()))
def mult_input():
	return map(int,input().split())

for nt in range(int(input())):
	n=int(input())
	if n%2==1:
		print (n//2)
	else:
		print (n//2-1)