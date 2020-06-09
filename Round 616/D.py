import sys
input = sys.stdin.readline

def getMid(s, e) : 
	return s + (e -s) // 2; 

def getSumUtil(arr,st, ss, se, qs, qe, si) :
	if (qs <= ss and qe >= se) :
		if st[si]:
			return (st[si],arr[ss])
		else:
			return (False," ")

	if (se < qs or ss > qe) : 
		return (True,"")
	mid = getMid(ss, se); 
	
	ans1 = getSumUtil(arr,st, ss, mid, qs, qe, 2 * si + 1)
	ans2 = getSumUtil(arr,st, mid + 1, se, qs, qe, 2 * si + 2)
	if ans1[0]==False or ans2[0]==False:
		return (False," ")
	else:
		if ans1[1]=="":
			return (True,ans2[1])
		elif ans2[1]=="":
			return (True,ans1[1])
		elif ans1[1]==ans2[1]:
			return (True,ans1[1])
		else:
			return (False," ")

def constructSTUtil(arr, ss, se, st, si) : 
	if (ss == se) : 
		st[si] = True;
		if ss<len(arr):
			return (True,arr[ss])
		else:
			return (st[si]," ")
	mid = getMid(ss, se)
	ans1 = constructSTUtil(arr, ss, mid, st, si * 2 + 1)
	ans2 = constructSTUtil(arr, mid + 1, se, st, si * 2 + 2)
	if ans1[0]==False or ans2[0]==False:
		st[si] = False
		return (False,[" "])
	else:
		if ans1[1][0]==ans2[1][0]:
			st[si] = True
			return (True,ans1[1][0])
		else:
			st[si] = False
			return (False,[" "])

def constructST(arr, n) : 
	x = n
	size=0
	while x>1:
		x=x/2
		size+=1
	max_size = 2**(size)
	max_size = 2*max_size-1
	st = [0] * max_size
	constructSTUtil(arr, 0, n - 1, st, 0)
	return st 


arr = input()
n = len(arr)
q = int(input())
st = constructST(arr, n)
for i in range(q):
	l,r = map(int,input().split())
	if l==r:
		print ("Yes")
	else:
		if (getSumUtil(arr,st, 0, n - 1, l-1, r-1, 0)[0]==True):
			print ("No")
		else:
			print ("Yes")

