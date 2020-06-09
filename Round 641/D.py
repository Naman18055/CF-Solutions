import math

class SegTree(object):
	"""Segment Tree Implementation"""
	def __init__(self, n, array):
		self.n = n
		self.array = array
		self.tree = [0]*(2*(2**(math.ceil(math.log(n,2))))+1)

	def construct(self, start, end, node): # Construction of Tree
		if start==end:
			self.tree[node] = self.array[start]
			return self.array[start]
		else:
			self.tree[node]=self.function(self.construct(start, (start+end)//2, 2*node+1),self.construct((start+end)//2+1, end, 2*node+2))
			return self.tree[node]

	def update(self, start, end, node, index, value):
		if start==end and start==index:
			self.tree[node] = value
			return value
		elif index>end or index<start:
			return self.tree[node]
		else:
			self.tree[node] = self.function(self.update(start, (start+end)//2, 2*node+1, index, value),self.update((start+end)//2+1, end, 2*node+2, index, value))
			return self.tree[node]

	def calc(self, start, end, node, low, high): # Calculating for the range value low to high
		if start>=low and end<=high:
			return self.tree[node]
		elif end<low or start>high:
			return 0
		else:
			return self.function(self.calc(start, (start+end)//2, 2*node+1, low, high),self.calc((start+end)//2+1, end, 2*node+2, low, high))

	def function(self,a,b): # Function for filling the tree. Eg - max
		temp=(a[0]+b[0],a[1]+b[1],a[2]+b[2])
		if temp[1]==0:
			return temp
		s=temp[0]+temp[1]+temp[2]
		k=(s+1)//2
		if k>temp[0] and k<temp[0]+temp[1]:
			return (0,s,0)
		return temp

for nt in range(int(input())):
	n,k=map(int,input().split())
	l=list(map(int,input().split()))
	if n==1:
		if k==l[0]:
			print ("yes")
		else:
			print ("no")
		continue
	new=[]
	for i in l:
		if i<k:
			new.append((1,0,0))
		elif i>k:
			new.append((0,0,1))
		else:
			new.append((0,1,0))
	st = SegTree(n,new)
	st.construct(0,n-1,0)
	print (st.tree)
	ans="no"
	temp=(st.tree[0])
	if temp[0]==0 and temp[2]==0:
		ans="yes"
	print (ans)