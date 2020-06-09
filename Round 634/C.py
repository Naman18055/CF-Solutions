from collections import Counter
import sys
input = sys.stdin.buffer.readline
def list_input():
	return list(map(int,input().split()))
def mult_input():
	return map(int,input().split())

for nt in range(int(input())):
	n=int(input())
	l=list_input()
	c=Counter(l)
	m=0
	for i in c:
		m=max(m,c[i])
	print (max(min(m,len(c)-1),min(m-1,len(c))))