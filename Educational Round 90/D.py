import sys
input = sys.stdin.readline

def maxSubArraySum(a,size): 

	if size==0:
		return 0
	max_so_far = -10**18
	max_ending_here = 0
	   
	for i in range(0, size): 
		max_ending_here = max_ending_here + a[i] 
		if (max_so_far < max_ending_here): 
			max_so_far = max_ending_here 
  
		if max_ending_here < 0: 
			max_ending_here = 0   
	return max_so_far 

for nt in range(int(input())):
	n = int(input())
	a = list(map(int,input().split()))
	if n==1:
		print (a[0])
		continue
	s = 0
	g = []
	g2 = []
	for i in range(0,n-1,2):
		s += a[i]
		g.append(a[i+1]-a[i])
	if n%2:
		s += a[-1]
	for i in range(2,n,2):
		g2.append(a[i-1]-a[i])
	# print (g)
	# print (g2)
	# print (s)
	print (s+max(maxSubArraySum(g,len(g)),maxSubArraySum(g2,len(g2)),0))