# Python3 implementation of the approach 
from bisect import bisect_left as lower_bound 

# Function to return the sum of arr[0..index] 
# This function assumes that the array is 
# preprocessed and partial sums of array elements 
# are stored in BITree[] 
def getSum(BITree, index): 

	# Initialize result 
	s = 0

	# Traverse ancestors of BITree[index] 
	while index > 0: 

		# Add current element of BITree to sum 
		s += BITree[index] 

		# Move index to parent node in getSum View 
		index -= index & (-index) 

	return s 

# Updates a node in Binary Index Tree (BITree) 
# at given index in BITree. The given value 'val' 
# is added to BITree[i] and all of its ancestors in tree. 
def updateBIT(BITree, n, index, val): 

	# Traverse all ancestors and add 'val' 
	while index <= n: 

		# Add 'val' to current node of BI Tree 
		BITree[index] += val 

		# Update index to that of parent in update View 
		index += index & (-index) 

# Converts an array to an array with values 
# from 1 to n and relative order of smaller 
# and greater elements remains same. 
# For example, {7, -90, 100, 1} is 
# converted to {3, 1, 4, 2 } 
def convert(arr, n): 

	# Create a copy of arrp[] in temp and 
	# sort the temp array in increasing order 
	temp = [0] * n 
	for i in range(n): 
		temp[i] = arr[i] 

	temp.sort() 

	# Traverse all array elements 
	for i in range(n): 

		# lower_bound() Returns pointer to the first element 
		# greater than or equal to arr[i] 
		arr[i] = lower_bound(temp, arr[i]) + 1

# Function to find smaller_right array 
def findElements(arr, n): 

	BIT = [0] * (n + 1) 

	# To store smaller elements in right side 
	# and greater elements on left side 
	smaller_right = [0] * n 
	greater_left = [0] * n 

	# Find all left side greater elements 
	for i in range(n): 

		# Get count of elements greater than arr[i] 
		greater_left[i] = i - getSum(BIT, arr[i]) 

		# Add current element to BIT 
		updateBIT(BIT, n, arr[i], 1) 

	return greater_left

n=int(input())
x=list(map(int,input().split()))
arr=list(map(int,input().split()))
convert(arr,n)
print (l)
x.sort()
ans1 = 0
ans2 = 0
d = 0
s=0
prev=0
for i in range(n): 
	ans1 += (x[i] * i - d) 
	d += x[i]

	
print (max(ans1,0))