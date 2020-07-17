import sys
import math
sys.setrecursionlimit(100000)

def solve(start,end,c):
	n = len(s)
	if start==end:
		if ord(s[start])==c:
			return 0
		else:
			return 1
	
	if start==0:
		count1 = (end-start+1)//2-count[c-97][(start+end)//2]
	else:
		count1 = (end-start+1)//2-(count[c-97][(start+end)//2] - count[c-97][start-1])
	count2 = (end-start+1)//2-(count[c-97][end] - count[c-97][(start+end)//2])
	# print (start,end,c,count1,count2)

	return min(count2+solve(start,(start+end)//2,c+1),count1+solve((start+end)//2+1,end,c+1))

for nt in range(int(input())):
	n = int(input())
	s = list(input())
	count = [[0 for i in range(n)] for j in range(26)]
	for i in range(n):
		if i>0:
			for j in range(26):
				count[j][i]	= count[j][i-1]
		count[ord(s[i])-97][i] += 1

	# for i in count:
		# print (*i)

	print (solve(0,n-1,97))
