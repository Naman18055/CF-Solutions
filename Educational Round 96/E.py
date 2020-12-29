def mergesort(l,n):
	if n==1:
		return l,0
	else:
		a,ans1=mergesort(l[0:n//2],n//2)
		b,ans2=mergesort(l[n//2:],n-n//2)
		c,ans3=combine(a,n//2,b,n-n//2)
		#print (c,ans1,ans2,ans3)
		return (c,ans1+ans2+ans3)

def combine(l1,n,l2,m):
	i=0
	j=0
	ans=[]
	inversions=0
	while (i<n and j<m):
		if l1[i]<=l2[j]:
			ans.append(l1[i])
			i+=1
		else:
			ans.append(l2[j])
			inversions += n-i
			j+=1
	if i==n:
		for k in range(j,m):
			ans.append(l2[k])
	elif j==m:
		for k in range(i,n):
			ans.append(l1[k])
	return (ans,inversions)

n = int(input())
start = input()
s = start[::-1]
loc = {}
for i in range(n):
	if s[i] in loc:
		loc[s[i]].append(i)
	else:
		loc[s[i]] = [i]
new = {}
for i in loc:
	new[i] = loc[i][::-1]
arr = []
for i in range(n):
	arr.append(new[start[i]].pop())
# print (arr)


print (mergesort(arr, len(arr))[1])


