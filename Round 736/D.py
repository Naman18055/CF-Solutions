import sys
import math
input = sys.stdin.readline

class SegTree(object):
	"""docstring for SegTree"""
	def __init__(self, n, arr):
		self.n = n
		self.arr = arr
		self.tree = [0 for i in range(2*n)]
		self.construct()

	def construct(self): # Construction
		for i in range(self.n):
			self.tree[self.n+i] = self.arr[i]
		for i in range(self.n-1,0,-1):
			self.tree[i] = self.function(self.tree[2*i],self.tree[2*i+1])

	def update(self,index,value):
		start = index+self.n
		self.tree[start] = value
		start = start//2
		while start>0:
			self.tree[start] = self.function(self.tree[2*start],self.tree[2*start+1])
			start = start//2

	def calc(self,low,high): # 0-indexed
		low+=self.n
		high+=self.n
		ans = self.tree[low] # Needs to initialised
		while low<high:
			if low%2:
				ans = self.function(ans, self.tree[low])
				low += 1
			if high%2:
				high -= 1
				ans = self.function(ans, self.tree[high])
			low = low//2
			high = high//2
		return ans
	
	def function(self,a,b): # Function used to construct Segment Tree
		return math.gcd(a, b)


for nt in range(int(input())):
	n = int(input())
	a = list(map(int,input().split()))
	if n==1:
		print (1)
		continue
	d = []
	for i in range(1, n):
		d.append(abs(a[i]-a[i-1]))

	# print (d)
	tree = SegTree(len(d), d)
	l, r = 0, 0
	ans = 0
	while r<n-1:
		hcf = tree.calc(l, r+1)
		# print (l, r, hcf)
		if hcf>1:
			ans = max(r - l + 1, ans)
			r += 1
		else:
			l += 1
			r += 1
	print (ans+1)







