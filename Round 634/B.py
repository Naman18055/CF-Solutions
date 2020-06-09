import sys
input = sys.stdin.buffer.readline
def list_input():
	return list(map(int,input().split()))
def mult_input():
	return map(int,input().split())

for nt in range(int(input())):
	n,a,b=mult_input()
	ans="a"*(a-b+1)
	for i in range(b-1):
		ans+=(chr(98+i))
	# print (ans)
	s=""
	for i in range(n//a):
		s+=ans
	s+=ans[0:n%a]
	print (s)