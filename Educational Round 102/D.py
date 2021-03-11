import sys
input = sys.stdin.readline


class SegTree(object):
	"""docstring for SegTree"""
	def __init__(self, n, arr):
		self.n = n
		self.arr = arr
		self.tree = [[0, 0, 0] for i in range(2*n)]

	def construct(self): # Construction
		for i in range(self.n):
			if self.arr[i]==1:
				self.tree[self.n+i][1] = self.arr[i]
			else:
				self.tree[self.n+i][0] = self.arr[i]
			self.tree[self.n+i][2] = self.arr[i]
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
		ansl = [0, 0, 0] # Needs to initialised
		ansr = [0, 0, 0]
		while low<high:
			if low%2:
				ansl = self.function(ansl, self.tree[low])
				low += 1
			if high%2:
				high -= 1
				ansr = self.function(self.tree[high], ansr)
			low = low//2
			high = high//2
		return self.function(ansl, ansr)
	
	def function(self,a,b): # Function used to construct Segment Tree
		return [min(a[0], b[0]+a[2]), max(a[1], b[1]+a[2]), b[2]+a[2]]


for nt in range(int(input())):
	n, m = map(int,input().split())
	s = input()
	arr = []
	for i in s:
		if i=="+":
			arr.append(1)
		else:
			arr.append(-1)
	tree = SegTree(n, arr)
	tree.construct()
	# print (tree.tree)
	for i in range(m):
		a, b = map(int,input().split())
		r1 = tree.calc(0, a-1)
		x = r1[2]
		r2 = tree.calc(b, n)
		maxx, minn = x + r2[1], x + r2[0]
		# print (r1, r2)
		print (max(r1[1], maxx) - min(minn, r1[0]) + 1)








