import math
t=int(input())
for nt in range(t):
	s,i,e=map(int,input().split())
	temp=i+e
	if temp<s:
		print (e+1)
	else:
		print (max(0,(e-(temp-s)//2)))