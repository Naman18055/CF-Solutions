import sys
from collections import Counter
input = sys.stdin.readline

def calc(num):
	low = 0
	high = n
	while low<high:
		mid = (low+high)//2
		if a[mid][0]>num:
			high = mid - 1
		elif a[mid][0]<num:
			low = mid + 1
		else:
			return mid
	if low<len(a) and a[low][0]<=num:
		return low
	else:
		return low-1

class SegTree(object):
	"""docstring for SegTree"""
	def __init__(self, n, arr):
		self.n = n
		self.arr = arr
		self.tree = [0 for i in range(2*n)]

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
		ans = 0 # Needs to initialised
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
		return max(a,b)

final = []
for nt in range(int(input())):
	n,k = map(int,input().split())
	x = list(map(int,input().split()))
	y = list(map(int,input().split()))
	if max(x)-min(x)<=2*k:
		final.append(n)
		continue
	c = Counter(x)
	a = []
	for i in c:
		a.append([i,c[i]])
	a.sort()
	p = [a[0][1]]
	n = len(a)
	for i in range(1,n):
		p.append(p[-1]+a[i][1])

	for i in range(n):
		if a[i][0]-a[0][0]>k:
			ind = i-1
			break

	s = [(p[ind],0,ind)]
	m = p[ind]
	nums = [p[ind]]
	for i in range(1,n):
		j = calc(a[i][0]+k)
		s.append((p[j]-p[i-1],i,j))
		nums.append(p[j]-p[i-1])
		m = max(m,s[-1][0])

	# print (a)
	# print (*s)

	st = SegTree(len(nums),nums)
	st.construct()
	prev = 0
	nxt = 0
	m = 0
	ans = s[0][0]

	for i in range(len(s)):
		while nxt<len(s) and s[nxt][1]<=s[i][2]:
			nxt += 1
		while s[prev][2]<s[i][1]:
			m = max(m,s[prev][0])
			prev += 1

		ans = max(ans,s[i][0]+max(m,st.calc(nxt,len(s))))
	final.append(ans)


	# if nt==260:
	# 	print (n,k,x,y)
	# 	exit()

for i in final:
	print (i)










